#!/usr/bin/env python3
"""
Demo script for Improved Entity Scraper
Shows the enhanced entity name and address separation
"""

import pandas as pd
from scraper import EntityScraper

def demo_entity_separation():
    """Demonstrate entity and address separation"""
    print("🎯 Entity-Address Separation Demo")
    print("=" * 50)
    
    scraper = EntityScraper()
    
    # Sample data that would come from a table
    sample_data = [
        "Dr. Manpreets Global Eye Hospital SCF 36, SST Nagar, Rajpura road, Patiala Punjab- 147001",
        "Max Super-Specialty Hospital Near Civil Hospital, Phase-VI, Mohali, Punjab-160055",
        "Amar Hospital Bank Colony, ITO Road, Patiala Punjab- 147001",
        "GARG EYE HOSPITAL Passey Road, Near Gurudwara Dukhniwaran Sahib, Patiala, Punjab",
        "Behgal Institute of IT & Radiation Technology and Behgal Hospital F-431, 435, 436, Industrial area, Phase 8b, Mohali, Punjab."
    ]
    
    print("📋 Original Data (Mixed Entity Names and Addresses):")
    print("-" * 50)
    for i, text in enumerate(sample_data, 1):
        print(f"{i}. {text}")
    
    print("\n🔍 Separated Results:")
    print("-" * 50)
    
    separated_data = []
    for i, text in enumerate(sample_data, 1):
        entity_name, address = scraper.separate_entity_and_address(text)
        
        if entity_name and address:
            separated_data.append({
                'Entity_Name': entity_name,
                'Address': address
            })
            print(f"{i}. ✅ Entity: {entity_name}")
            print(f"   📍 Address: {address}")
        else:
            print(f"{i}. ❌ Failed to separate")
    
    # Create DataFrame
    if separated_data:
        df = pd.DataFrame(separated_data)
        print(f"\n📊 DataFrame Created with {len(df)} rows:")
        print(df.to_string(index=False))
        
        # Show data quality metrics
        print(f"\n📈 Data Quality Metrics:")
        print(f"   - Average Entity Name Length: {df['Entity_Name'].str.len().mean():.1f} characters")
        print(f"   - Average Address Length: {df['Address'].str.len().mean():.1f} characters")
        print(f"   - Success Rate: {(len(separated_data)/len(sample_data)*100):.1f}%")
    
    return separated_data

def demo_column_detection():
    """Demonstrate intelligent column detection"""
    print("\n🔍 Intelligent Column Detection Demo")
    print("=" * 50)
    
    scraper = EntityScraper()
    
    # Test different table structures
    test_cases = [
        {
            'name': "Clear Headers",
            'headers': ["Hospital Name", "Location", "Contact", "Rating"],
            'sample_rows': [
                ["Apollo Hospital", "123 Main St, Bangalore", "080-123456", "4.5"],
                ["Fortis Hospital", "456 Park Road, Mumbai", "022-789012", "4.2"]
            ]
        },
        {
            'name': "Generic Headers",
            'headers': ["Name", "Address", "Phone"],
            'sample_rows': [
                ["Dr. Manpreets Global Eye Hospital SCF 36, SST Nagar, Rajpura road, Patiala Punjab- 147001", "Contact info", "1234567890"],
                ["Max Super-Specialty Hospital Near Civil Hospital, Phase-VI, Mohali, Punjab-160055", "Contact info", "0987654321"]
            ]
        },
        {
            'name': "No Headers",
            'headers': ["Column_1", "Column_2", "Column_3"],
            'sample_rows': [
                ["Hospital A", "123 Street, City", "Other info"],
                ["Hospital B", "456 Road, Town", "Other info"]
            ]
        }
    ]
    
    for test_case in test_cases:
        print(f"\n📋 {test_case['name']}:")
        print(f"   Headers: {test_case['headers']}")
        
        entity_col, address_col = scraper.identify_entity_and_address_columns(
            test_case['headers'], 
            test_case['sample_rows']
        )
        
        print(f"   ✅ Entity Column: {entity_col} ({test_case['headers'][entity_col]})")
        print(f"   ✅ Address Column: {address_col} ({test_case['headers'][address_col]})")

def main():
    """Main demonstration function"""
    print("🚀 Improved Entity Scraper Demonstration")
    print("=" * 60)
    print("This demo shows the enhanced capabilities of the Entity Scraper:")
    print("1. Smart entity name and address separation")
    print("2. Intelligent column detection")
    print("3. Better data quality and organization")
    print()
    
    try:
        # Demo entity separation
        separated_data = demo_entity_separation()
        
        # Demo column detection
        demo_column_detection()
        
        print("\n🎉 Demo completed successfully!")
        print("\n✅ Key Improvements:")
        print("   - Entity names and addresses are now properly separated")
        print("   - Column detection is more intelligent")
        print("   - Data quality is significantly better")
        print("   - Output is clean and organized")
        print("\n💡 Ready to use with the Streamlit app!")
        
    except Exception as e:
        print(f"\n💥 Error during demo: {str(e)}")
        print("Please check that all dependencies are installed.")

if __name__ == "__main__":
    main()
