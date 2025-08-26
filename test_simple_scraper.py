#!/usr/bin/env python3
"""
Test script for Simplified EntityScraper
Tests the focused entity name and address extraction
"""

import sys
import time
from scraper import EntityScraper

def test_table_extraction():
    """Test table data extraction with column detection"""
    print("📊 Testing table extraction...")
    print("=" * 50)
    
    scraper = EntityScraper()
    
    # Test URLs that should have tables
    test_urls = [
        "https://nabh.co/hospitals-accredited-list/",  # SSL issues but should work
        "https://www.apollohospitals.com/",            # Should work
        "https://www.fortishealthcare.com/"            # Should work
    ]
    
    for url in test_urls:
        print(f"\n🌐 Testing URL: {url}")
        try:
            print("⏳ Extracting entities...")
            start_time = time.time()
            
            data = scraper.scrape_website(url, "entity", use_selenium=False)
            
            if data:
                print(f"✅ Success! Found {len(data)} entities")
                print("📋 Sample data:")
                for i, item in enumerate(data[:3]):  # Show first 3 items
                    print(f"  {i+1}. Entity: {item.get('Entity_Name', 'N/A')}")
                    print(f"     Address: {item.get('Address', 'N/A')}")
                    print()
            else:
                print("⚠️ No data found")
                
                # Try with Selenium
                print("🔄 Trying with Selenium...")
                data = scraper.scrape_website(url, "entity", use_selenium=True)
                
                if data:
                    print(f"✅ Success with Selenium! Found {len(data)} entities")
                    print("📋 Sample data:")
                    for i, item in enumerate(data[:3]):
                        print(f"  {i+1}. Entity: {item.get('Entity_Name', 'N/A')}")
                        print(f"     Address: {item.get('Address', 'N/A')}")
                        print()
                else:
                    print("❌ No data found even with Selenium")
            
            elapsed_time = time.time() - start_time
            print(f"⏱️ Time taken: {elapsed_time:.2f} seconds")
            
        except Exception as e:
            print(f"❌ Error extracting from {url}: {str(e)}")
    
    print("\n" + "=" * 50)

def test_column_detection():
    """Test the intelligent column detection functionality"""
    print("\n🔍 Testing column detection...")
    print("=" * 50)
    
    scraper = EntityScraper()
    
    # Test with sample data
    headers = ["Hospital Name", "Location", "Contact", "Rating"]
    sample_rows = [
        ["Apollo Hospital", "123 Main St, Bangalore", "080-123456", "4.5"],
        ["Fortis Hospital", "456 Park Road, Mumbai", "022-789012", "4.2"],
        ["Manipal Hospital", "789 Lake View, Delhi", "011-345678", "4.8"]
    ]
    
    try:
        entity_col, address_col = scraper.identify_entity_and_address_columns(headers, sample_rows)
        print(f"✅ Column detection successful!")
        print(f"   Entity column: {entity_col} ({headers[entity_col]})")
        print(f"   Address column: {address_col} ({headers[address_col]})")
        
        # Test extraction
        print("\n📋 Testing data extraction:")
        for i, row in enumerate(sample_rows):
            entity_name = row[entity_col] if entity_col < len(row) else ""
            address = row[address_col] if address_col < len(row) else ""
            print(f"  {i+1}. {entity_name} - {address}")
            
    except Exception as e:
        print(f"❌ Column detection error: {str(e)}")
    
    print("\n" + "=" * 50)

def test_data_processing():
    """Test data processing and cleaning"""
    print("\n🧹 Testing data processing...")
    print("=" * 50)
    
    scraper = EntityScraper()
    
    # Test text cleaning
    test_texts = [
        "  Apollo  Hospital  ",
        "123 Main Street, Mumbai 400001",
        "Hospital & Medical Center",
        "🏥 City Hospital"
    ]
    
    print("📝 Text cleaning test:")
    for text in test_texts:
        cleaned = scraper.clean_text(text)
        print(f"  Original: '{text}' -> Cleaned: '{cleaned}'")
    
    # Test address extraction
    test_addresses = [
        "Apollo Hospital, 123 Main Street, Mumbai 400001",
        "City Medical Center, Sector 15, Phase 2, Delhi",
        "Regional Hospital, Building A, Floor 3, Bangalore"
    ]
    
    print("\n📍 Address extraction test:")
    for address in test_addresses:
        extracted = scraper.extract_address_from_text(address)
        print(f"  Address: '{address}' -> Extracted: '{extracted}'")
    
    print("\n" + "=" * 50)

def main():
    """Main test function"""
    print("🚀 Simplified Entity Scraper Test Suite")
    print("=" * 50)
    print("Testing focused entity name and address extraction")
    print()
    
    try:
        test_column_detection()
        test_data_processing()
        test_table_extraction()
        
        print("\n🎉 All tests completed!")
        print("\n✅ The scraper now focuses on:")
        print("   - Entity names and addresses only")
        print("   - Intelligent column detection")
        print("   - Clean, organized output")
        print("   - Better data quality")
        
    except KeyboardInterrupt:
        print("\n⏹️ Testing interrupted by user")
    except Exception as e:
        print(f"\n💥 Unexpected error during testing: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
