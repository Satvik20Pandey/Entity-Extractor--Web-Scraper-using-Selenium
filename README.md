# 🔍 Entity Extractor - Table Data Extraction Tool

A powerful Python-based web scraping tool with a beautiful Streamlit interface for extracting entity names and addresses from website tables. Simply paste a website URL and get accurate entity data in a clean, organized format.

## ✨ Features

- **🌐 Direct URL Scraping**: Extract data from any website with tables
- **📋 Smart Column Detection**: Automatically identifies entity name and address columns
- **🔍 Intelligent Entity Separation**: Automatically separates entity names from addresses in mixed content
- **📍 Address Extraction**: Intelligent address parsing and extraction
- **📊 Data Visualization**: Interactive charts and analytics
- **💾 Multiple Export Formats**: Download data as Excel or CSV
- **🎨 Modern UI**: Beautiful Streamlit interface with responsive design
- **⚡ Dual Scraping Engine**: Both requests and Selenium for dynamic websites
- **🔧 Advanced Filtering**: Filter results by entity name or address
- **🔒 SSL Handling**: Automatic SSL certificate issue resolution
- **🎯 Focused Output**: Only extracts entity names and addresses (2 columns)
- **📈 Data Quality Metrics**: Real-time quality assessment and validation

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Chrome browser (for Selenium functionality)
- Internet connection

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Extractor
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:8501`

## 📖 Usage Guide

### Simple 3-Step Process

1. **Enter Website URL**: Paste the website URL that contains tables with entity data
2. **Choose Scraping Mode**: Select Regular (for static HTML) or Selenium (for dynamic content)
3. **Click Extract**: Get your data in seconds!

### What Gets Extracted

- **Entity Name**: Hospital names, company names, organization names, etc.
- **Address**: Location, street address, city, state, etc.

### Example URLs to Try

- **🏥 NABH Hospitals**: `https://nabh.co/hospitals-accredited-list/`
- **🏥 Apollo Hospitals**: `https://www.apollohospitals.com/`
- **🏦 RBI Banks**: `https://rbi.org.in/`
- **🛡️ IRDAI Insurance**: `https://www.irdai.gov.in/`

## 🏗️ Architecture

### Core Components

1. **`scraper.py`**: Main scraping engine with intelligent column detection and entity separation
2. **`app.py`**: Streamlit web interface with progress tracking and data quality metrics
3. **`requirements.txt`**: Python dependencies

### Scraping Methods

- **Table Extraction**: Parse HTML tables with smart column identification
- **List Extraction**: Extract data from unordered/ordered lists
- **Structured Data**: Parse JSON-LD and microdata
- **Address Intelligence**: Smart address pattern recognition
- **Entity Separation**: Automatic separation of entity names from addresses

### Data Processing

- **Column Detection**: Automatically identifies entity name and address columns
- **Entity Separation**: Intelligently separates mixed entity name and address content
- **Text Cleaning**: Remove noise and normalize text
- **Address Extraction**: Identify and extract address information
- **Data Validation**: Ensure data quality and completeness

## ⚙️ Configuration

### Selenium Options

- **Headless Mode**: Run browser in background
- **User Agent Rotation**: Avoid detection
- **Dynamic Content Loading**: Handle JavaScript-rendered content
- **SSL Error Handling**: Ignore certificate errors for problematic sites

### Scraping Settings

- **Regular Mode**: For static HTML tables (faster)
- **Selenium Mode**: For dynamic JavaScript-rendered content

## 📊 Data Output

### Standard Fields

- **Entity_Name**: Name of the hospital, company, organization, etc.
- **Address**: Extracted address information

### Export Formats

- **Excel (.xlsx)**: Full-featured spreadsheet with formatting
- **CSV**: Simple comma-separated values
- **Custom Naming**: Automatic filename generation with timestamps

## 🔧 Advanced Features

### Data Quality Metrics

- **Completeness Analysis**: Track missing data
- **Length Distribution**: Analyze text patterns
- **Validation**: Ensure both entity name and address are present
- **Success Rate**: Monitor extraction effectiveness

### Interactive Visualizations

- **Entity Name Length**: Distribution of entity name lengths
- **Address Length**: Distribution of address lengths
- **Real-time Updates**: Dynamic chart refreshing

### Filtering & Search

- **Entity Name Filtering**: Search within extracted entity names
- **Address Filtering**: Search within extracted addresses
- **Real-time Search**: Instant result filtering

### Error Handling & Fallbacks

- **SSL Certificate Issues**: Automatic retry without verification
- **Column Detection**: Intelligent fallback to first/second columns
- **Data Validation**: Skip incomplete entries automatically
- **Entity Separation**: Handle mixed content intelligently

## 🚨 Important Notes

### Legal & Ethical Considerations

- **Respect robots.txt**: Always check website terms
- **Rate Limiting**: Built-in delays to avoid overwhelming servers
- **Data Usage**: Use extracted data responsibly and legally

### Technical Limitations

- **Dynamic Content**: Some websites require Selenium
- **CAPTCHA Protection**: May not work on protected sites
- **Data Accuracy**: Quality depends on source website table structure
- **SSL Issues**: Some sites may have certificate problems (handled automatically)

## 🐛 Troubleshooting

### Common Issues

1. **No Data Found**
   - Try enabling Selenium option for dynamic websites
   - Check website accessibility
   - Verify URL format
   - Ensure the website has tables with entity data

2. **ChromeDriver Errors (Windows)**
   - **Error**: `[WinError 193] %1 is not a valid Win32 application`
   - **Solution**: Run the ChromeDriver fix script:
     ```bash
     python fix_chromedriver.py
     ```
   - **Alternative**: Manually download ChromeDriver from https://chromedriver.chromium.org/
   - **Check**: Ensure Chrome browser is up to date

3. **Selenium Errors**
   - Ensure Chrome browser is installed
   - Update ChromeDriver if needed
   - Check system permissions
   - Clear ChromeDriver cache if needed

4. **SSL Certificate Errors**
   - Tool automatically handles most SSL issues
   - For persistent problems, try using Selenium option

5. **Poor Data Quality**
   - Check if the website has proper table structure
   - Verify column headers are descriptive
   - Try different websites for better results

6. **Mixed Entity Names and Addresses**
   - **Problem**: Same text appears in both columns
   - **Solution**: The tool now automatically separates entity names from addresses
   - **Example**: "Dr. Manpreets Global Eye Hospital SCF 36, SST Nagar, Rajpura road, Patiala Punjab- 147001"
   - **Result**: 
     - Entity: "Dr. Manpreets Global Eye Hospital SCF 36"
     - Address: "SST Nagar, Rajpura road, Patiala Punjab- 147001"

### Performance Tips

- **Use Selenium sparingly**: Only for dynamic websites
- **Check table structure**: Ensure the website has proper HTML tables
- **Monitor results**: Check extracted data quality

## 🧪 Testing

### Test Scripts

- **`test_simple_scraper.py`**: Test focused entity name and address extraction
- **`test_entity_separation.py`**: Test entity name and address separation logic
- **`demo_improved_scraper.py`**: Demonstrate improved functionality
- **`fix_chromedriver.py`**: Fix ChromeDriver issues on Windows

### Running Tests

```bash
# Test basic scraper
python test_simple_scraper.py

# Test entity separation
python test_entity_separation.py

# Run demo
python demo_improved_scraper.py

# Fix ChromeDriver issues (Windows)
python fix_chromedriver.py
```

## 🤝 Contributing

We welcome contributions! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **BeautifulSoup4**: HTML parsing
- **Selenium**: Dynamic content handling
- **Streamlit**: Web interface framework
- **Pandas**: Data manipulation
- **Plotly**: Interactive visualizations
- **urllib3**: SSL handling improvements

## 📞 Support

For support and questions:

- **Issues**: Create a GitHub issue
- **Documentation**: Check this README
- **Community**: Join our discussions

---

**Happy Data Extraction! 🎉**

*Built with ❤️ for accurate entity data extraction*
