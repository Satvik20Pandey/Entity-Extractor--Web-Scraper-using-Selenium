# 🚀 Deploy Entity Extractor to Streamlit Cloud

## **Free Hosting on Streamlit Cloud**

### **Step 1: Prepare Your Repository**

1. **Push to GitHub** (if not already done):
   ```bash
   git add .
   git commit -m "Ready for Streamlit deployment"
   git push origin main
   ```

2. **Ensure these files are in your repository**:
   - ✅ `app.py` (main Streamlit app)
   - ✅ `scraper.py` (scraping engine)
   - ✅ `requirements.txt` (Python dependencies)
   - ✅ `.streamlit/config.toml` (Streamlit config)
   - ✅ `packages.txt` (system dependencies)

### **Step 2: Deploy to Streamlit Cloud**

1. **Go to [share.streamlit.io](https://share.streamlit.io)**
2. **Sign in with GitHub**
3. **Click "New app"**
4. **Fill in the details**:
   - **Repository**: `your-username/Extractor`
   - **Branch**: `main`
   - **Main file path**: `app.py`
   - **App URL**: Leave blank (auto-generated)
5. **Click "Deploy!"**

### **Step 3: Wait for Deployment**

- **Build time**: 2-5 minutes
- **Status**: Check the deployment logs
- **Success**: You'll get a public URL like `https://your-app-name.streamlit.app`

### **Step 4: Test Your App**

- **Visit your public URL**
- **Test with example URLs**
- **Share with others!**

## **Alternative: Deploy to Render**

### **Step 1: Create render.yaml**

```yaml
services:
  - type: web
    name: entity-extractor
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: streamlit run app.py --server.port $PORT --server.address 0.0.0.0
    envVars:
      - key: PYTHON_VERSION
        value: 3.9.16
```

### **Step 2: Deploy to Render**

1. **Go to [render.com](https://render.com)**
2. **Sign up/Login with GitHub**
3. **Click "New +" → "Web Service"**
4. **Connect your repository**
5. **Configure and deploy**

## **Alternative: Deploy to Heroku**

### **Step 1: Create Procfile**

```
web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```

### **Step 2: Deploy to Heroku**

1. **Install Heroku CLI**
2. **Create Heroku app**
3. **Push to Heroku**

## **🌐 Your App Will Be Available At:**

- **Streamlit Cloud**: `https://your-app-name.streamlit.app`
- **Render**: `https://your-app-name.onrender.com`
- **Heroku**: `https://your-app-name.herokuapp.com`

## **🔧 Troubleshooting**

### **Common Issues:**

1. **Build Failures**:
   - Check `requirements.txt` versions
   - Ensure all imports are correct
   - Check for syntax errors

2. **Runtime Errors**:
   - Check Streamlit logs
   - Test locally first
   - Verify dependencies

3. **ChromeDriver Issues**:
   - Use `packages.txt` for system dependencies
   - Consider using Selenium alternatives

## **📱 Features After Deployment:**

- ✅ **Public URL** accessible from anywhere
- ✅ **No local setup** required for users
- ✅ **Automatic updates** when you push to GitHub
- ✅ **Free hosting** (with limitations)
- ✅ **Professional appearance** for sharing

## **🎯 Ready to Deploy?**

Your Entity Extractor is now ready for deployment! 

**Recommended**: Start with **Streamlit Cloud** - it's free, easy, and perfect for Streamlit apps.

**Next Steps**:
1. Push your code to GitHub
2. Deploy to Streamlit Cloud
3. Share your public URL
4. Enjoy your hosted app! 🎉

---

**Need help?** Check the Streamlit Cloud documentation or ask for assistance!
