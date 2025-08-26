#!/usr/bin/env python3
"""
Test script for EntityScraper
Run this to test the scraping functionality
"""

import sys
import time
from scraper import EntityScraper

def test_scraper():
    """Test the EntityScraper functionality"""
    print("🔍 Testing Entity Scraper...")
    print("=" * 50)
    
    # Initialize scraper
    scraper = EntityScraper()
    print("✅ Scraper initialized successfully")
    
    # Test URL scraping
    test_urls = [
        "https://nabh.co/hospitals-accredited-list/",
        "https://www.example.com"  # Fallback test
    ]
    
    for url in test_urls:
        print(f"\n🌐 Testing URL: {url}")
        try:
            print("⏳ Scraping data...")
            start_time = time.time()
            
            # Try with regular requests first
            data = scraper.scrape_website(url, "hospital", use_selenium=False)
            
            if data:
                print(f"✅ Success! Found {len(data)} entities")
                print("📊 Sample data:")
                for i, item in enumerate(data[:3]):  # Show first 3 items
                    print(f"  {i+1}. {item.get('Entity_Name', 'N/A')} - {item.get('Address', 'N/A')}")
            else:
                print("⚠️ No data found with regular requests")
                
                # Try with Selenium
                print("🔄 Trying with Selenium...")
                data = scraper.scrape_website(url, "hospital", use_selenium=True)
                
                if data:
                    print(f"✅ Success with Selenium! Found {len(data)} entities")
                    print("📊 Sample data:")
                    for i, item in enumerate(data[:3]):
                        print(f"  {i+1}. {item.get('Entity_Name', 'N/A')} - {item.get('Address', 'N/A')}")
                else:
                    print("❌ No data found even with Selenium")
            
            elapsed_time = time.time() - start_time
            print(f"⏱️ Time taken: {elapsed_time:.2f} seconds")
            
        except Exception as e:
            print(f"❌ Error scraping {url}: {str(e)}")
    
    # Test search functionality
    print("\n🔍 Testing search functionality...")
    try:
        search_results = scraper.search_entities("hospital", "India", max_results=10)
        if search_results:
            print(f"✅ Search successful! Found {len(search_results)} results")
        else:
            print("⚠️ Search returned no results")
    except Exception as e:
        print(f"❌ Search error: {str(e)}")
    
    print("\n" + "=" * 50)
    print("🎉 Testing completed!")

def test_text_processing():
    """Test text processing functions"""
    print("\n🧹 Testing text processing...")
    
    scraper = EntityScraper()
    
    # Test text cleaning
    test_texts = [
        "  Apollo  Hospital  ",
        "123 Main Street, Mumbai",
        "Hospital & Medical Center",
        "🏥 City Hospital"
    ]
    
    for text in test_texts:
        cleaned = scraper.clean_text(text)
        print(f"Original: '{text}' -> Cleaned: '{cleaned}'")
    
    # Test address extraction
    test_addresses = [
        "Apollo Hospital, 123 Main Street, Mumbai 400001",
        "City Medical Center, Sector 15, Phase 2, Delhi",
        "Regional Hospital, Building A, Floor 3, Bangalore"
    ]
    
    for address in test_addresses:
        extracted = scraper.extract_address_from_text(address)
        print(f"Address: '{address}' -> Extracted: '{extracted}'")

if __name__ == "__main__":
    print("🚀 Entity Scraper Test Suite")
    print("=" * 50)
    
    try:
        test_text_processing()
        test_scraper()
    except KeyboardInterrupt:
        print("\n⏹️ Testing interrupted by user")
    except Exception as e:
        print(f"\n💥 Unexpected error: {str(e)}")
        sys.exit(1)
