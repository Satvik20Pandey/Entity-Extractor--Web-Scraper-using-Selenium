# 🚀 Deploy Entity Extractor to Render

## **Free Hosting on Render**

### **Step 1: Prepare Your Repository**

1. **Ensure these files are in your repository**:
   - ✅ `app.py` (main Streamlit app)
   - ✅ `scraper.py` (scraping engine)
   - ✅ `requirements.txt` (Python dependencies)
   - ✅ `render.yaml` (Render configuration)
   - ✅ `.streamlit/config.toml` (Streamlit config)

2. **Push to GitHub** (if not already done):
   ```bash
   git add .
   git commit -m "Ready for Render deployment"
   git push origin main
   ```

### **Step 2: Deploy to Render**

1. **Go to [render.com](https://render.com)**
2. **Sign up/Login with GitHub**
3. **Click "New +" → "Web Service"**
4. **Connect your repository**: `Satvik20Pandey/Entity-Extractor--Web-Scraper-using-Selenium`
5. **Configure the service**:
   - **Name**: `entity-extractor` (or your preferred name)
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt && pip install streamlit`
   - **Start Command**: `streamlit run app.py --server.port $PORT --server.address 0.0.0.0 --server.headless true`
   - **Plan**: `Free`

6. **Click "Create Web Service"**

### **Step 3: Wait for Deployment**

- **Build time**: 5-10 minutes
- **Status**: Check the deployment logs
- **Success**: You'll get a public URL like `https://your-app-name.onrender.com`

### **Step 4: Test Your App**

- **Visit your public URL**
- **Test with example URLs**
- **Share with others!**

## **🔧 Render-Specific Configuration**

### **Environment Variables**

The `render.yaml` automatically sets these:
- `PYTHON_VERSION`: 3.9.16
- `STREAMLIT_SERVER_PORT`: $PORT (Render's port)
- `STREAMLIT_SERVER_ADDRESS`: 0.0.0.0 (bind to all interfaces)
- `STREAMLIT_SERVER_HEADLESS`: true (no browser UI)
- `STREAMLIT_BROWSER_GATHER_USAGE_STATS`: false

### **Port Configuration**

Render automatically provides a `$PORT` environment variable. The app is configured to use this port.

### **Free Plan Limitations**

- **Sleep after inactivity**: 15 minutes
- **Build time**: 5-10 minutes
- **Bandwidth**: 100 GB/month
- **Perfect for**: Development, testing, small projects

## **🚨 Important Notes for Render**

### **Selenium Limitations**

- **No Chrome/Chromium**: Render free plan doesn't support browser automation
- **Alternative**: Use regular requests mode for static websites
- **Dynamic content**: May not work without Selenium

### **File System**

- **Read-only**: Cannot write files permanently
- **Downloads**: Excel/CSV downloads work via browser
- **Temporary storage**: Available during request processing

### **Performance**

- **Cold starts**: First request after inactivity takes longer
- **Memory**: Limited to 512 MB on free plan
- **CPU**: Shared resources

## **🔧 Troubleshooting Render Issues**

### **Common Issues**

1. **Build Failures**:
   - Check `requirements.txt` versions
   - Ensure all imports are correct
   - Check for syntax errors

2. **Runtime Errors**:
   - Check Render logs
   - Test locally first
   - Verify dependencies

3. **Port Issues**:
   - Ensure `$PORT` is used in start command
   - Check `render.yaml` configuration

4. **Selenium Errors**:
   - Use regular mode instead of Selenium
   - Check website accessibility
   - Try different URLs

### **Performance Tips**

- **Use regular mode**: Faster than Selenium
- **Optimize imports**: Remove unused dependencies
- **Monitor logs**: Check for errors in Render dashboard

## **📱 Features After Render Deployment**

- ✅ **Public URL** accessible from anywhere
- ✅ **No local setup** required for users
- ✅ **Automatic updates** when you push to GitHub
- ✅ **Free hosting** (with limitations)
- ✅ **Professional appearance** for sharing
- ✅ **HTTPS enabled** automatically

## **🎯 Ready to Deploy on Render?**

Your Entity Extractor is now configured for Render deployment!

**Next Steps**:
1. Push your code to GitHub
2. Deploy to Render
3. Get your public URL: `https://your-app-name.onrender.com`
4. Test and share! 🎉

---

**Need help?** Check the Render documentation or deployment logs!
