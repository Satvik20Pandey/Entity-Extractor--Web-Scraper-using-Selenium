import streamlit as st
import pandas as pd
import time
from scraper import EntityScraper
import io
import base64
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go

# Page configuration
st.set_page_config(
    page_title="Entity Extractor - Web Scraping Tool",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern UI
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        color: white;
        text-align: center;
    }
    
    .search-container {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 2rem;
    }
    
    .results-container {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 2rem;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        margin: 1rem 0;
    }
    
    .stButton > button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.5rem 2rem;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    
    .url-input {
        border: 2px solid #e0e0e0;
        border-radius: 10px;
        padding: 0.5rem;
        transition: border-color 0.3s ease;
    }
    
    .url-input:focus {
        border-color: #667eea;
        outline: none;
    }
    
    .success-message {
        background: #d4edda;
        color: #155724;
        padding: 1rem;
        border-radius: 10px;
        border: 1px solid #c3e6cb;
        margin: 1rem 0;
    }
    
    .error-message {
        background: #f8d7da;
        color: #721c24;
        padding: 1rem;
        border-radius: 10px;
        border: 1px solid #f5c6cb;
        margin: 1rem 0;
    }
    
    .info-message {
        background: #d1ecf1;
        color: #0c5460;
        padding: 1rem;
        border-radius: 10px;
        border: 1px solid #bee5eb;
        margin: 1rem 0;
    }
    
    .warning-message {
        background: #fff3cd;
        color: #856404;
        padding: 1rem;
        border-radius: 10px;
        border: 1px solid #ffeaa7;
        margin: 1rem 0;
    }
    
    .extraction-info {
        background: #e2e3e5;
        color: #383d41;
        padding: 1rem;
        border-radius: 10px;
        border: 1px solid #d6d8db;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'scraper' not in st.session_state:
    st.session_state.scraper = EntityScraper()
if 'scraped_data' not in st.session_state:
    st.session_state.scraped_data = pd.DataFrame()
if 'is_scraping' not in st.session_state:
    st.session_state.is_scraping = False

def download_excel(df, filename="scraped_data.xlsx"):
    """Create and download Excel file"""
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Scraped_Data', index=False)
    output.seek(0)
    
    b64 = base64.b64encode(output.read()).decode()
    href = f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="{filename}">Download Excel File</a>'
    return href

def create_visualizations(df):
    """Create interactive visualizations for the scraped data"""
    if df.empty:
        return
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Entity name length distribution
        if 'Entity_Name' in df.columns:
            name_lengths = df['Entity_Name'].str.len()
            fig_length = px.histogram(
                x=name_lengths,
                title="Entity Name Length Distribution",
                nbins=20,
                color_discrete_sequence=['#667eea']
            )
            fig_length.update_layout(height=400)
            st.plotly_chart(fig_length, use_container_width=True)
    
    with col2:
        # Address length distribution
        if 'Address' in df.columns:
            address_lengths = df['Address'].str.len()
            fig_address = px.histogram(
                x=address_lengths,
                title="Address Length Distribution",
                nbins=20,
                color_discrete_sequence=['#764ba2']
            )
            fig_address.update_layout(height=400)
            st.plotly_chart(fig_address, use_container_width=True)

def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🔍 Entity Extractor</h1>
        <p>Extract Entity Names and Addresses from Website Tables</p>
        <p>Simply paste a website URL and get accurate entity data</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar
    st.sidebar.markdown("## ⚙️ Settings")
    
    # Scraping options
    st.sidebar.markdown("### Scraping Options")
    use_selenium = st.sidebar.checkbox("Use Selenium (for dynamic websites)", value=False)
    
    # Example URLs
    st.sidebar.markdown("### 📋 Example URLs to Try")
    example_urls = {
        "🏥 NABH Hospitals": "https://nabh.co/hospitals-accredited-list/",
        "🏥 Apollo Hospitals": "https://www.apollohospitals.com/",
        "🏦 RBI Banks": "https://rbi.org.in/",
        "🛡️ IRDAI Insurance": "https://www.irdai.gov.in/"
    }
    
    for label, url in example_urls.items():
        if st.sidebar.button(label, key=f"example_{url}"):
            st.session_state.example_url = url
            st.rerun()
    
    # Main content
    tab1, tab2, tab3 = st.tabs(["🌐 Website Scraping", "📊 Results", "📈 Analytics"])
    
    with tab1:
        st.markdown('<div class="search-container">', unsafe_allow_html=True)
        
        # URL input section
        st.markdown("### 🌐 Enter Website URL")
        url_input = st.text_input(
            "Website URL",
            value=st.session_state.get('example_url', ''),
            placeholder="https://example.com/list-of-entities",
            help="Enter a website URL that contains tables with entity names and addresses"
        )
        
        # Additional options
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 📋 What to Extract")
            st.info("""
            **Entity Name**: Hospital names, company names, organization names, etc.
            
            **Address**: Location, street address, city, state, etc.
            """)
        
        with col2:
            st.markdown("### ⚙️ Scraping Options")
            st.info("""
            **Regular Mode**: For static HTML tables (faster)
            
            **Selenium Mode**: For dynamic JavaScript-rendered content
            """)
        
        # Scrape button
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            scrape_button = st.button(
                "🚀 Extract Entities",
                type="primary",
                use_container_width=True,
                disabled=st.session_state.is_scraping
            )
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Scraping logic
        if scrape_button and url_input:
            st.session_state.is_scraping = True
            
            with st.spinner("🔄 Extracting entities from website... This may take a few minutes."):
                try:
                    # Scrape from specific URL
                    st.info(f"🔗 Extracting data from: {url_input}")
                    
                    # Show extraction progress
                    progress_bar = st.progress(0)
                    status_text = st.empty()
                    
                    status_text.text("🔍 Analyzing website structure...")
                    progress_bar.progress(25)
                    
                    scraped_data = st.session_state.scraper.scrape_website(
                        url_input, 
                        "entity",
                        use_selenium=use_selenium
                    )
                    
                    progress_bar.progress(75)
                    status_text.text("🧹 Processing and cleaning data...")
                    
                    if scraped_data:
                        # Process data to extract only entity names and addresses
                        processed_data = []
                        for item in scraped_data:
                            entity_name = item.get('Entity_Name', '')
                            address = item.get('Address', '')
                            
                            # Only add if we have both entity name and address
                            if entity_name and address and len(entity_name) > 2 and len(address) > 5:
                                processed_data.append({
                                    'Entity_Name': entity_name,
                                    'Address': address
                                })
                        
                        progress_bar.progress(100)
                        status_text.text("✅ Extraction completed!")
                        
                        if processed_data:
                            df = pd.DataFrame(processed_data)
                            st.session_state.scraped_data = df
                            
                            st.success(f"✅ Successfully extracted {len(df)} entities with addresses!")
                            
                            # Show extraction summary
                            st.markdown('<div class="extraction-info">', unsafe_allow_html=True)
                            st.markdown(f"""
                            **📊 Extraction Summary:**
                            - **Total Rows Found**: {len(scraped_data)}
                            - **Valid Entities**: {len(processed_data)}
                            - **Success Rate**: {(len(processed_data)/len(scraped_data)*100):.1f}%
                            """)
                            st.markdown('</div>', unsafe_allow_html=True)
                            
                            # Show sample of extracted data
                            st.markdown("### 📋 Sample of Extracted Data")
                            st.dataframe(df.head(10), use_container_width=True)
                            
                            # Show data quality info
                            if len(df) > 0:
                                st.markdown("### 🔍 Data Quality Check")
                                col1, col2 = st.columns(2)
                                
                                with col1:
                                    avg_name_length = df['Entity_Name'].str.len().mean()
                                    st.metric("Average Entity Name Length", f"{avg_name_length:.1f} characters")
                                
                                with col2:
                                    avg_address_length = df['Address'].str.len().mean()
                                    st.metric("Average Address Length", f"{avg_address_length:.1f} characters")
                        else:
                            st.warning("⚠️ No entities with addresses found. The website might not have the expected table structure.")
                    else:
                        st.error("❌ No data found on the website. Please check the URL or try using Selenium option.")
                    
                    st.rerun()
                    
                except Exception as e:
                    st.error(f"❌ Error during extraction: {str(e)}")
                    st.info("💡 Try using the Selenium option for dynamic websites or check the URL format.")
                finally:
                    st.session_state.is_scraping = False
    
    with tab2:
        if not st.session_state.scraped_data.empty:
            st.markdown('<div class="results-container">', unsafe_allow_html=True)
            
            # Results summary
            df = st.session_state.scraped_data
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown(f'<div class="metric-card"><h3>📊 Total Entities</h3><h2>{len(df)}</h2></div>', unsafe_allow_html=True)
            
            with col2:
                with_address = df['Address'].notna().sum() if 'Address' in df.columns else 0
                st.markdown(f'<div class="metric-card"><h3>📍 With Address</h3><h2>{with_address}</h2></div>', unsafe_allow_html=True)
            
            with col3:
                st.markdown(f'<div class="metric-card"><h3>📅 Extracted</h3><h2>{datetime.now().strftime("%H:%M")}</h2></div>', unsafe_allow_html=True)
            
            # Data table
            st.markdown("### 📋 Extracted Entities and Addresses")
            
            # Filter options
            col1, col2 = st.columns([2, 1])
            with col1:
                if 'Address' in df.columns:
                    address_filter = st.text_input("🔍 Filter by address", placeholder="Enter address keywords...")
                    if address_filter:
                        df_filtered = df[df['Address'].str.contains(address_filter, case=False, na=False)]
                    else:
                        df_filtered = df
                else:
                    df_filtered = df
            
            with col2:
                if 'Entity_Name' in df.columns:
                    entity_filter = st.text_input("🔍 Filter by entity name", placeholder="Enter entity keywords...")
                    if entity_filter:
                        df_filtered = df_filtered[df_filtered['Entity_Name'].str.contains(entity_filter, case=False, na=False)]
            
            # Display filtered data
            st.dataframe(df_filtered, use_container_width=True)
            
            # Download options
            st.markdown("### 💾 Download Data")
            
            col1, col2 = st.columns(2)
            with col1:
                if not df_filtered.empty:
                    filename = f"entities_and_addresses_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
                    download_link = download_excel(df_filtered, filename)
                    st.markdown(download_link, unsafe_allow_html=True)
            
            with col2:
                if not df_filtered.empty:
                    csv = df_filtered.to_csv(index=False)
                    st.download_button(
                        label="📥 Download CSV",
                        data=csv,
                        file_name=f"entities_and_addresses_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                        mime="text/csv"
                    )
            
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.info("💡 No entities have been extracted yet. Use the Website Scraping tab to get started!")
    
    with tab3:
        if not st.session_state.scraped_data.empty:
            st.markdown('<div class="results-container">', unsafe_allow_html=True)
            st.markdown("### 📊 Data Analytics & Visualizations")
            
            df = st.session_state.scraped_data
            
            # Create visualizations
            create_visualizations(df)
            
            # Data quality metrics
            st.markdown("### 📈 Data Quality Metrics")
            
            col1, col2 = st.columns(2)
            
            with col1:
                if 'Entity_Name' in df.columns:
                    # Entity name quality
                    name_lengths = df['Entity_Name'].str.len()
                    avg_name_length = name_lengths.mean()
                    st.metric("Average Entity Name Length", f"{avg_name_length:.1f} characters")
                    
                    # Missing data analysis
                    missing_names = df['Entity_Name'].isna().sum()
                    st.metric("Missing Entity Names", missing_names)
            
            with col2:
                if 'Address' in df.columns:
                    # Address quality
                    address_lengths = df['Address'].str.len()
                    avg_address_length = address_lengths.mean()
                    st.metric("Average Address Length", f"{avg_address_length:.1f} characters")
                    
                    # Missing addresses
                    missing_addresses = df['Address'].isna().sum()
                    st.metric("Missing Addresses", missing_addresses)
            
            # Data sample
            st.markdown("### 🔍 Data Sample")
            st.dataframe(df.head(10), use_container_width=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.info("💡 No data available for analytics. Extract some entities first!")

if __name__ == "__main__":
    main()
