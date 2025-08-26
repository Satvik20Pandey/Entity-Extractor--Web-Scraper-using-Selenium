# 🚀 Quick Start Guide - Entity Extractor

## ⚡ Get Started in 3 Steps

### 1. **Install Dependencies**
```bash
# Option A: Automated setup (Recommended)
python setup.py

# Option B: Manual installation
pip install -r requirements.txt
```

### 2. **Run the Application**
```bash
# Start the Streamlit web app
streamlit run app.py
```

### 3. **Open Your Browser**
Navigate to: `http://localhost:8501`

---

## 🎯 What You Can Do

### **Extract Entity Data from Websites**
- **Paste Website URL**: Enter any website that contains tables with entity data
- **Choose Mode**: Regular (static HTML) or Selenium (dynamic content)
- **Get Results**: Extract entity names and addresses automatically

### **Example Websites to Try**
- 🏥 **NABH Hospitals**: `https://nabh.co/hospitals-accredited-list/`
- 🏥 **Apollo Hospitals**: `https://www.apollohospitals.com/`
- 🏦 **RBI Banks**: `https://rbi.org.in/`
- 🛡️ **IRDAI Insurance**: `https://www.irdai.gov.in/`

### **Download Results**
- Excel (.xlsx) format
- CSV format
- Automatic filename generation

---

## 🔧 Quick Commands

### **Windows Users**
```bash
# Double-click these files:
run_app.bat          # Command Prompt
run_app.ps1          # PowerShell
```

### **Linux/Mac Users**
```bash
# Make executable and run:
chmod +x run_app.sh
./run_app.sh
```

### **Test the Scraper**
```bash
# Test simplified functionality
python test_simple_scraper.py

# Generate demo data
python demo.py
```

---

## 📱 Features at a Glance

- 🌐 **Direct URL Scraping**: Extract from any website with tables
- 📋 **Smart Column Detection**: Automatically finds entity name and address columns
- 📍 **Address Extraction**: Intelligent address parsing
- 📊 **Data Visualization**: Interactive charts for entity and address lengths
- 💾 **Multiple Formats**: Excel, CSV export
- 🎨 **Modern UI**: Beautiful Streamlit interface
- ⚡ **Dual Engine**: Requests + Selenium
- 🔧 **Advanced Filtering**: Filter by entity name or address
- 🔒 **SSL Handling**: Automatic SSL certificate issue resolution

---

## 🚨 Troubleshooting

### **Common Issues**
1. **Python not found**: Install Python 3.8+
2. **Dependencies error**: Run `pip install -r requirements.txt`
3. **Chrome not found**: Install Google Chrome for Selenium
4. **Port in use**: Change port in Streamlit settings
5. **No data found**: Ensure website has proper HTML tables

### **Need Help?**
- Check `README.md` for detailed documentation
- Run `python setup.py` for automated setup
- Use demo data: `python demo.py`
- Test scraper: `python test_simple_scraper.py`

---

## 🎉 You're Ready!

Start extracting entities like:
- 🏥 Hospital names and addresses
- 🏦 Bank names and locations
- 🛡️ Insurance company details
- 🏢 Company names and addresses
- 🏫 School names and locations

**Happy Data Extraction! 🚀**
