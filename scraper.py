import requests
import pandas as pd
from bs4 import BeautifulSoup
import time
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent
import logging
import urllib3
import ssl
import platform
import os

# Disable SSL warnings and certificate verification for problematic sites
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class EntityScraper:
    def __init__(self):
        self.ua = UserAgent()
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': self.ua.random,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        })
        
    def setup_selenium_driver(self):
        """Setup Chrome driver with options for web scraping"""
        try:
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--ignore-ssl-errors")
            chrome_options.add_argument("--ignore-certificate-errors")
            chrome_options.add_argument(f"--user-agent={self.ua.random}")
            chrome_options.add_argument("--window-size=1920,1080")
            
            # Fix for Windows architecture detection
            if platform.system() == "Windows":
                # Force 64-bit ChromeDriver for Windows
                os.environ['WDM_ARCHITECTURE'] = '64'
                os.environ['WDM_PLATFORM'] = 'win64'
                
                # Clear any cached drivers to force fresh download
                cache_dir = os.path.expanduser("~/.wdm/drivers/chromedriver")
                if os.path.exists(cache_dir):
                    try:
                        import shutil
                        shutil.rmtree(cache_dir)
                        logger.info("Cleared ChromeDriver cache to fix architecture issue")
                    except Exception as e:
                        logger.warning(f"Could not clear cache: {e}")
            
            try:
                # Try to get ChromeDriver with proper architecture
                driver_path = ChromeDriverManager().install()
                logger.info(f"ChromeDriver installed at: {driver_path}")
                
                service = Service(driver_path)
                driver = webdriver.Chrome(service=service, options=chrome_options)
                logger.info("ChromeDriver setup successful")
                return driver
                
            except Exception as e:
                logger.error(f"ChromeDriver setup failed: {e}")
                
                # Fallback: try to use system ChromeDriver if available
                try:
                    logger.info("Trying system ChromeDriver as fallback...")
                    driver = webdriver.Chrome(options=chrome_options)
                    logger.info("System ChromeDriver fallback successful")
                    return driver
                except Exception as fallback_error:
                    logger.error(f"System ChromeDriver fallback also failed: {fallback_error}")
                    return None
                    
        except Exception as e:
            logger.error(f"Error setting up Selenium driver: {e}")
            return None
    
    def clean_text(self, text):
        """Clean and normalize text data"""
        if not text:
            return ""
        text = str(text).strip()
        text = re.sub(r'\s+', ' ', text)  # Remove extra whitespace
        text = re.sub(r'[^\w\s\-.,()&]', '', text)  # Remove special characters except common ones
        return text
    
    def extract_address_from_text(self, text):
        """Extract address-like information from text"""
        if not text:
            return ""
        
        # Common address patterns
        address_patterns = [
            r'\d+\s+[A-Za-z\s]+(?:Street|Road|Avenue|Lane|Drive|Boulevard|Colony|Nagar|Area|Sector|Phase)',
            r'[A-Za-z\s]+(?:Street|Road|Avenue|Lane|Drive|Boulevard|Colony|Nagar|Area|Sector|Phase)\s+\d+',
            r'\d+\s+[A-Za-z\s]+(?:Floor|Building|Complex|Mall|Plaza)',
            r'[A-Za-z\s]+(?:District|State|City|PIN|Postal Code)',
            r'\d{6}',  # PIN codes
        ]
        
        for pattern in address_patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            if matches:
                return self.clean_text(matches[0])
        
        return self.clean_text(text)
    
    def separate_entity_and_address(self, text):
        """Separate entity name from address in a single text"""
        if not text:
            return "", ""
        
        text = str(text).strip()
        
        # Common patterns to separate entity name from address
        separators = [
            r'([^,]+?)(?:,|Near|Opposite|Behind|In front of|At|Located at|Address:?|Location:?)(.+)',
            r'([^,]+?)(?:,|Near|Opposite|Behind|In front of|At|Located at|Address:?|Location:?)(.+)',
            r'([^,]+?)(?:,|Near|Opposite|Behind|In front of|At|Located at|Address:?|Location:?)(.+)',
        ]
        
        for pattern in separators:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                entity_name = match.group(1).strip()
                address = match.group(2).strip()
                
                # Validate that we have meaningful separation
                if len(entity_name) > 3 and len(address) > 5:
                    return entity_name, address
        
        # If no pattern match, try to split by common delimiters
        delimiters = [', Near', ', Opposite', ', Behind', ', In front of', ', At', ', Located at', ', Address:', ', Location:']
        
        for delimiter in delimiters:
            if delimiter in text:
                parts = text.split(delimiter, 1)
                if len(parts) == 2:
                    entity_name = parts[0].strip()
                    address = delimiter + parts[1].strip()
                    
                    if len(entity_name) > 3 and len(address) > 5:
                        return entity_name, address
        
        # Fallback: split by first comma if it looks like it separates name and address
        if ',' in text:
            parts = text.split(',', 1)
            if len(parts) == 2:
                entity_name = parts[0].strip()
                address = parts[1].strip()
                
                # Check if the second part looks like an address
                if any(keyword in address.lower() for keyword in ['road', 'street', 'colony', 'nagar', 'area', 'sector', 'phase', 'punjab', 'delhi', 'mumbai', 'bangalore']):
                    if len(entity_name) > 3 and len(address) > 5:
                        return entity_name, address
        
        # If all else fails, return the original text as entity name and empty address
        return text, ""
    
    def identify_entity_and_address_columns(self, headers, sample_rows):
        """Intelligently identify which columns contain entity names and addresses"""
        entity_col = None
        address_col = None
        
        # Keywords that suggest entity names
        entity_keywords = ['name', 'entity', 'hospital', 'company', 'organization', 'institution', 'center', 'clinic', 'bank', 'insurance', 'school', 'college', 'university']
        
        # Keywords that suggest addresses
        address_keywords = ['address', 'location', 'place', 'area', 'street', 'road', 'city', 'state', 'district', 'pin', 'postal', 'area', 'colony', 'nagar']
        
        # First pass: check headers for exact matches
        for col_idx, header in enumerate(headers):
            header_lower = header.lower()
            
            # Check for entity name column
            if entity_col is None:
                for keyword in entity_keywords:
                    if keyword in header_lower:
                        entity_col = col_idx
                        break
            
            # Check for address column
            if address_col is None:
                for keyword in address_keywords:
                    if keyword in header_lower:
                        address_col = col_idx
                        break
        
        # Second pass: analyze content if headers didn't help
        if entity_col is None or address_col is None:
            for col_idx in range(len(headers)):
                if entity_col is None:
                    # Check if this column contains entity-like data
                    sample_text = ' '.join([str(row[col_idx]) for row in sample_rows[:5] if col_idx < len(row)])
                    if any(keyword in sample_text.lower() for keyword in entity_keywords):
                        entity_col = col_idx
                
                if address_col is None:
                    # Check if this column contains address-like data
                    sample_text = ' '.join([str(row[col_idx]) for row in sample_rows[:5] if col_idx < len(row)])
                    if any(keyword in sample_text.lower() for keyword in address_keywords):
                        address_col = col_idx
        
        # Third pass: if still not found, use content analysis
        if entity_col is None or address_col is None:
            for col_idx in range(len(headers)):
                if col_idx < len(sample_rows[0]) if sample_rows else 0:
                    sample_text = ' '.join([str(row[col_idx]) for row in sample_rows[:3] if col_idx < len(row)])
                    
                    # Check for entity patterns (shorter, organization-like names)
                    if entity_col is None and len(sample_text) < 100:
                        if any(keyword in sample_text.lower() for keyword in ['hospital', 'clinic', 'center', 'institute', 'company', 'bank']):
                            entity_col = col_idx
                    
                    # Check for address patterns (longer, location-like text)
                    if address_col is None and len(sample_text) > 50:
                        if any(keyword in sample_text.lower() for keyword in ['road', 'street', 'colony', 'nagar', 'area', 'sector', 'phase', 'punjab', 'delhi', 'mumbai']):
                            address_col = col_idx
        
        # Fallback: use first and second columns if we couldn't identify
        if entity_col is None:
            entity_col = 0
        if address_col is None:
            address_col = min(1, len(headers) - 1)
        
        # Ensure we don't have the same column for both
        if entity_col == address_col and len(headers) > 1:
            address_col = 1 if entity_col == 0 else 0
        
        return entity_col, address_col
    
    def scrape_table_data(self, soup, url):
        """Extract data from HTML tables with focus on entity names and addresses"""
        tables = soup.find_all('table')
        all_data = []
        
        logger.info(f"Found {len(tables)} tables on the page")
        
        for table_idx, table in enumerate(tables):
            try:
                logger.info(f"Processing table {table_idx + 1}")
                
                # Find headers
                headers = []
                header_row = table.find('thead')
                if header_row:
                    headers = [self.clean_text(th.get_text()) for th in header_row.find_all(['th', 'td'])]
                else:
                    # Try to find headers in first row
                    first_row = table.find('tr')
                    if first_row:
                        headers = [self.clean_text(th.get_text()) for th in first_row.find_all(['th', 'td'])]
                
                # If no headers found, create generic ones
                if not headers:
                    max_cols = max(len(row.find_all(['td', 'th'])) for row in table.find_all('tr'))
                    headers = [f'Column_{i+1}' for i in range(max_cols)]
                
                logger.info(f"Table headers: {headers}")
                
                # Extract rows
                rows = table.find_all('tr')[1:] if header_row else table.find_all('tr')
                logger.info(f"Found {len(rows)} data rows")
                
                # Get sample rows for column identification
                sample_rows = []
                for row in rows[:10]:  # First 10 rows for analysis
                    cells = row.find_all(['td', 'th'])
                    row_data = [self.clean_text(cell.get_text()) for cell in cells]
                    if row_data:
                        sample_rows.append(row_data)
                
                # Identify entity and address columns
                entity_col, address_col = self.identify_entity_and_address_columns(headers, sample_rows)
                logger.info(f"Identified columns - Entity: {entity_col} ({headers[entity_col]}), Address: {address_col} ({headers[address_col]})")
                
                # Extract data from identified columns
                for row_idx, row in enumerate(rows):
                    cells = row.find_all(['td', 'th'])
                    if len(cells) > max(entity_col, address_col):
                        entity_text = self.clean_text(cells[entity_col].get_text()) if entity_col < len(cells) else ""
                        address_text = self.clean_text(cells[address_col].get_text()) if address_col < len(cells) else ""
                        
                        # If we have the same text in both columns, try to separate them
                        if entity_text == address_text and entity_text:
                            entity_name, address = self.separate_entity_and_address(entity_text)
                        else:
                            entity_name = entity_text
                            address = address_text
                        
                        # Only add if we have meaningful data
                        if entity_name and len(entity_name) > 2 and address and len(address) > 5:
                            all_data.append({
                                'Entity_Name': entity_name,
                                'Address': address,
                                'Source_URL': url,
                                'Table_Index': table_idx + 1,
                                'Row_Index': row_idx + 1
                            })
                            logger.debug(f"Added: {entity_name} - {address}")
                        
            except Exception as e:
                logger.error(f"Error processing table {table_idx}: {e}")
                continue
        
        logger.info(f"Total entities extracted from tables: {len(all_data)}")
        return all_data
    
    def scrape_list_data(self, soup, url):
        """Extract data from list elements (ul, ol, div lists)"""
        list_data = []
        
        # Look for common list patterns
        list_selectors = [
            'ul li', 'ol li', '.list-item', '.item', '.entry', '.hospital-item', 
            '.company-item', '.entity-item', '[class*="list"]', '[class*="item"]'
        ]
        
        for selector in list_selectors:
            try:
                items = soup.select(selector)
                for item in items:
                    item_text = self.clean_text(item.get_text())
                    if item_text and len(item_text) > 10:  # Filter out very short items
                        # Try to extract entity name and address from the text
                        lines = item_text.split('\n')
                        if len(lines) >= 2:
                            entity_name = lines[0].strip()
                            address = ' '.join(lines[1:]).strip()
                            
                            if entity_name and len(entity_name) > 2 and address and len(address) > 5:
                                list_data.append({
                                    'Entity_Name': entity_name,
                                    'Address': address,
                                    'Source_URL': url,
                                    'Source_Type': 'List_Item'
                                })
            except Exception as e:
                continue
        
        return list_data
    
    def scrape_structured_data(self, soup, url):
        """Extract structured data from JSON-LD, microdata, etc."""
        structured_data = []
        
        # Look for JSON-LD structured data
        json_ld_scripts = soup.find_all('script', type='application/ld+json')
        for script in json_ld_scripts:
            try:
                import json
                data = json.loads(script.string)
                if isinstance(data, dict):
                    if data.get('@type') in ['Organization', 'Hospital', 'LocalBusiness']:
                        entity_name = data.get('name', '')
                        address = data.get('address', {}).get('streetAddress', '')
                        
                        if entity_name and address:
                            structured_data.append({
                                'Entity_Name': entity_name,
                                'Address': address,
                                'Source_URL': url,
                                'Source_Type': 'Structured_Data'
                            })
            except Exception as e:
                continue
        
        return structured_data
    
    def scrape_website(self, url, entity_type="", use_selenium=False):
        """Main scraping function focused on entity names and addresses"""
        all_data = []
        
        try:
            if use_selenium:
                driver = self.setup_selenium_driver()
                if driver:
                    try:
                        logger.info(f"Using Selenium to scrape: {url}")
                        driver.get(url)
                        time.sleep(3)  # Wait for page to load
                        
                        # Scroll to load dynamic content
                        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                        time.sleep(2)
                        
                        page_source = driver.page_source
                        soup = BeautifulSoup(page_source, 'html.parser')
                    finally:
                        driver.quit()
                else:
                    logger.warning("Selenium driver setup failed, falling back to regular requests")
                    use_selenium = False
            
            if not use_selenium:
                logger.info(f"Using regular requests to scrape: {url}")
                # Try with SSL verification disabled for problematic sites
                try:
                    response = self.session.get(url, timeout=30, verify=True)
                    response.raise_for_status()
                except (requests.exceptions.SSLError, requests.exceptions.ConnectionError):
                    # Retry without SSL verification
                    logger.info(f"Retrying {url} without SSL verification")
                    response = self.session.get(url, timeout=30, verify=False)
                    response.raise_for_status()
                
                soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract data using multiple methods
            table_data = self.scrape_table_data(soup, url)
            list_data = self.scrape_list_data(soup, url)
            structured_data = self.scrape_structured_data(soup, url)
            
            all_data.extend(table_data)
            all_data.extend(list_data)
            all_data.extend(structured_data)
            
            logger.info(f"Total data extracted: {len(all_data)} items")
            
            # Process and clean the data
            processed_data = self.process_scraped_data(all_data, entity_type)
            
            return processed_data
            
        except Exception as e:
            logger.error(f"Error scraping {url}: {e}")
            return []
    
    def process_scraped_data(self, raw_data, entity_type):
        """Process and clean scraped data to focus on entity names and addresses"""
        processed_data = []
        
        for item in raw_data:
            processed_item = {}
            
            # Extract entity name and address
            entity_name = item.get('Entity_Name', '')
            address = item.get('Address', '')
            
            # Clean and validate the data
            if entity_name and len(entity_name) > 2:
                processed_item['Entity_Name'] = self.clean_text(entity_name)
            else:
                continue  # Skip if no valid entity name
            
            if address and len(address) > 5:
                processed_item['Address'] = self.clean_text(address)
            else:
                # Try to extract address from other fields
                for key, value in item.items():
                    if key not in ['Entity_Name', 'Source_URL', 'Table_Index', 'Row_Index', 'Source_Type']:
                        potential_address = self.extract_address_from_text(value)
                        if potential_address and len(potential_address) > 5:
                            processed_item['Address'] = potential_address
                            break
                
                if 'Address' not in processed_item:
                    continue  # Skip if no valid address
            
            # Add source information
            processed_item['Source_URL'] = item.get('Source_URL', '')
            processed_item['Source_Type'] = item.get('Source_Type', 'Table_Data')
            
            processed_data.append(processed_item)
        
        logger.info(f"Processed data: {len(processed_data)} valid entities")
        return processed_data
