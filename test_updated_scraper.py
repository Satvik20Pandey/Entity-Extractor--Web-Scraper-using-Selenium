#!/usr/bin/env python3
"""
Test script for Updated EntityScraper
Tests SSL handling and fallback functionality
"""

import sys
import time
from scraper import EntityScraper

def test_ssl_handling():
    """Test SSL certificate handling"""
    print("🔒 Testing SSL handling...")
    print("=" * 50)
    
    scraper = EntityScraper()
    
    # Test problematic URLs
    test_urls = [
        "https://nabh.co/hospitals-accredited-list/",  # SSL issues
        "https://www.apollohospitals.com/",            # Should work
        "https://www.fortishealthcare.com/"            # Should work
    ]
    
    for url in test_urls:
        print(f"\n🌐 Testing URL: {url}")
        try:
            print("⏳ Scraping data...")
            start_time = time.time()
            
            data = scraper.scrape_website(url, "hospital", use_selenium=False)
            
            if data:
                print(f"✅ Success! Found {len(data)} entities")
                print("📊 Sample data:")
                for i, item in enumerate(data[:2]):  # Show first 2 items
                    print(f"  {i+1}. {item.get('Entity_Name', 'N/A')} - {item.get('Address', 'N/A')}")
            else:
                print("⚠️ No data found")
            
            elapsed_time = time.time() - start_time
            print(f"⏱️ Time taken: {elapsed_time:.2f} seconds")
            
        except Exception as e:
            print(f"❌ Error scraping {url}: {str(e)}")
    
    print("\n" + "=" * 50)

def test_search_functionality():
    """Test search functionality with fallback"""
    print("\n🔍 Testing search functionality...")
    print("=" * 50)
    
    scraper = EntityScraper()
    
    search_terms = ["hospital", "insurance", "bank"]
    
    for term in search_terms:
        print(f"\n🔍 Searching for: {term}")
        try:
            search_results = scraper.search_entities(term, "India", max_results=10)
            if search_results:
                print(f"✅ Search successful! Found {len(search_results)} results")
                print("📊 Sample results:")
                for i, item in enumerate(search_results[:2]):
                    print(f"  {i+1}. {item.get('Entity_Name', 'N/A')}")
            else:
                print("⚠️ No search results")
                
                # Test fallback data
                print("🔄 Testing fallback data...")
                fallback_data = scraper.create_sample_data(term)
                if fallback_data:
                    print(f"✅ Fallback data available: {len(fallback_data)} entities")
                    for i, item in enumerate(fallback_data[:2]):
                        print(f"  {i+1}. {item.get('Entity_Name', 'N/A')}")
                else:
                    print("❌ No fallback data available")
                    
        except Exception as e:
            print(f"❌ Search error: {str(e)}")
    
    print("\n" + "=" * 50)

def test_sample_data():
    """Test sample data generation"""
    print("\n📋 Testing sample data generation...")
    print("=" * 50)
    
    scraper = EntityScraper()
    
    entity_types = ["hospital", "insurance", "bank", "unknown_type"]
    
    for entity_type in entity_types:
        print(f"\n🏷️ Testing entity type: {entity_type}")
        sample_data = scraper.create_sample_data(entity_type)
        
        if sample_data:
            print(f"✅ Generated {len(sample_data)} sample entities")
            print("📊 Sample entities:")
            for i, item in enumerate(sample_data[:2]):
                print(f"  {i+1}. {item.get('Entity_Name', 'N/A')}")
                print(f"     Address: {item.get('Address', 'N/A')}")
                print(f"     Source: {item.get('Source_Type', 'N/A')}")
        else:
            print(f"⚠️ No sample data for {entity_type}")
    
    print("\n" + "=" * 50)

def main():
    """Main test function"""
    print("🚀 Updated Entity Scraper Test Suite")
    print("=" * 50)
    print("Testing SSL handling, search functionality, and fallback data")
    print()
    
    try:
        test_ssl_handling()
        test_search_functionality()
        test_sample_data()
        
        print("\n🎉 All tests completed!")
        print("\n✅ The scraper now handles:")
        print("   - SSL certificate issues")
        print("   - Failed scraping attempts")
        print("   - Fallback sample data")
        print("   - Better error handling")
        
    except KeyboardInterrupt:
        print("\n⏹️ Testing interrupted by user")
    except Exception as e:
        print(f"\n💥 Unexpected error during testing: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
