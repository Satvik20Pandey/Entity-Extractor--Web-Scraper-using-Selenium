#!/usr/bin/env python3
"""
Demo script for Entity Extractor
This script demonstrates the scraping functionality with sample data
"""

import pandas as pd
from datetime import datetime
import json

def create_demo_data():
    """Create sample data to demonstrate the application"""
    
    # Sample hospital data
    hospitals = [
        {
            'Entity_Name': 'Apollo Hospitals Enterprise Ltd',
            'Address': 'Apollo Hospitals, 154/11, Bannerghatta Road, Bangalore 560076',
            'Source_URL': 'https://www.apollohospitals.com/',
            'Source_Type': 'Table_Data'
        },
        {
            'Entity_Name': 'Fortis Healthcare Limited',
            'Address': 'Fortis Hospital, 154/9, Bannerghatta Road, Bangalore 560076',
            'Source_URL': 'https://www.fortishealthcare.com/',
            'Source_Type': 'Table_Data'
        },
        {
            'Entity_Name': 'Manipal Hospitals',
            'Address': 'Manipal Hospital, 98, HAL Airport Road, Bangalore 560017',
            'Source_URL': 'https://www.manipalhospitals.com/',
            'Source_Type': 'Table_Data'
        },
        {
            'Entity_Name': 'Narayana Health',
            'Address': 'Narayana Health, 258/A, Bommasandra Industrial Area, Bangalore 560099',
            'Source_URL': 'https://www.narayanahealth.org/',
            'Source_Type': 'Table_Data'
        },
        {
            'Entity_Name': 'Columbia Asia Hospitals',
            'Address': 'Columbia Asia Hospital, 26/1, Bannerghatta Road, Bangalore 560029',
            'Source_URL': 'https://www.columbiaasia.com/',
            'Source_Type': 'Table_Data'
        }
    ]
    
    # Sample insurance company data
    insurance = [
        {
            'Entity_Name': 'Life Insurance Corporation of India',
            'Address': 'LIC Building, Yogakshema, Jeevan Bima Marg, Mumbai 400021',
            'Source_URL': 'https://www.lic.in/',
            'Source_Type': 'Structured_Data'
        },
        {
            'Entity_Name': 'HDFC Life Insurance Company',
            'Address': 'HDFC Life, HDFC Standard Life Building, Mumbai 400051',
            'Source_URL': 'https://www.hdfclife.com/',
            'Source_Type': 'Structured_Data'
        },
        {
            'Entity_Name': 'ICICI Prudential Life Insurance',
            'Address': 'ICICI Prudential, ICICI PruLife Towers, Mumbai 400018',
            'Source_URL': 'https://www.iciciprulife.com/',
            'Source_Type': 'Structured_Data'
        },
        {
            'Entity_Name': 'SBI Life Insurance Company',
            'Address': 'SBI Life, Natraj, Mumbai 400021',
            'Source_URL': 'https://www.sbilife.co.in/',
            'Source_Type': 'Structured_Data'
        },
        {
            'Entity_Name': 'Max Life Insurance Company',
            'Address': 'Max Life, Max House, Okhla Phase III, New Delhi 110020',
            'Source_URL': 'https://www.maxlifeinsurance.com/',
            'Source_Type': 'Structured_Data'
        }
    ]
    
    # Sample bank data
    banks = [
        {
            'Entity_Name': 'State Bank of India',
            'Address': 'SBI Central Office, State Bank Bhavan, Mumbai 400001',
            'Source_URL': 'https://www.sbi.co.in/',
            'Source_Type': 'List_Item'
        },
        {
            'Entity_Name': 'HDFC Bank Limited',
            'Address': 'HDFC Bank House, HDFC Bank Building, Mumbai 400001',
            'Source_URL': 'https://www.hdfcbank.com/',
            'Source_Type': 'List_Item'
        },
        {
            'Entity_Name': 'ICICI Bank Limited',
            'Address': 'ICICI Bank Tower, ICICI Bank Building, Mumbai 400001',
            'Source_URL': 'https://www.icicibank.com/',
            'Source_Type': 'List_Item'
        },
        {
            'Entity_Name': 'Axis Bank Limited',
            'Address': 'Axis Bank House, Axis Bank Building, Mumbai 400001',
            'Source_URL': 'https://www.axisbank.com/',
            'Source_Type': 'List_Item'
        },
        {
            'Entity_Name': 'Kotak Mahindra Bank',
            'Address': 'Kotak Mahindra Bank, Kotak Mahindra Bank Building, Mumbai 400001',
            'Source_URL': 'https://www.kotak.com/',
            'Source_Type': 'List_Type'
        }
    ]
    
    return {
        'hospitals': hospitals,
        'insurance': insurance,
        'banks': banks
    }

def save_demo_data():
    """Save demo data to files for testing"""
    
    demo_data = create_demo_data()
    
    # Save as JSON
    with open('demo_data.json', 'w', encoding='utf-8') as f:
        json.dump(demo_data, f, indent=2, ensure_ascii=False)
    
    # Save as Excel
    with pd.ExcelWriter('demo_data.xlsx', engine='openpyxl') as writer:
        for category, data in demo_data.items():
            df = pd.DataFrame(data)
            df.to_excel(writer, sheet_name=category.title(), index=False)
    
    # Save as CSV
    for category, data in demo_data.items():
        df = pd.DataFrame(data)
        df.to_csv(f'demo_{category}.csv', index=False, encoding='utf-8')
    
    print("✅ Demo data saved successfully!")
    print("📁 Files created:")
    print("   - demo_data.json")
    print("   - demo_data.xlsx")
    print("   - demo_hospitals.csv")
    print("   - demo_insurance.csv")
    print("   - demo_banks.csv")

def show_demo_stats():
    """Display statistics about the demo data"""
    
    demo_data = create_demo_data()
    
    print("\n📊 Demo Data Statistics")
    print("=" * 40)
    
    total_entities = 0
    for category, data in demo_data.items():
        count = len(data)
        total_entities += count
        print(f"{category.title()}: {count} entities")
    
    print(f"\nTotal Entities: {total_entities}")
    
    # Show sample entries
    print("\n🔍 Sample Entries:")
    print("-" * 40)
    
    for category, data in demo_data.items():
        print(f"\n{category.title()}:")
        for i, item in enumerate(data[:2]):  # Show first 2 entries
            print(f"  {i+1}. {item['Entity_Name']}")
            print(f"     Address: {item['Address']}")
            print(f"     Source: {item['Source_URL']}")

def main():
    """Main demo function"""
    
    print("🎯 Entity Extractor - Demo Script")
    print("=" * 40)
    print("This script demonstrates the scraping functionality")
    print("with sample data for hospitals, insurance companies, and banks.")
    print()
    
    # Show demo statistics
    show_demo_stats()
    
    print("\n💾 Saving demo data to files...")
    save_demo_data()
    
    print("\n🎉 Demo completed successfully!")
    print("\nYou can now:")
    print("1. Run 'streamlit run app.py' to start the web interface")
    print("2. Use the demo data files for testing")
    print("3. Try scraping real websites with the tool")

if __name__ == "__main__":
    main()
