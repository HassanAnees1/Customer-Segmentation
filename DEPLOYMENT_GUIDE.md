# Deployment Guide

This guide will help you deploy your Customer Segmentation Predictor on both GitHub and Hugging Face.

## 📁 File Structure

Make sure you have all these files in your project directory:

```
customer-segmentation-predictor/
├── app.py                          # Main Gradio application
├── requirements.txt                # Python dependencies
├── scaler.pkl                     # Trained StandardScaler (you need to add this)
├── kmeans_model.pkl               # Trained K-Means model (you need to add this)
├── README.md                      # GitHub README
├── HuggingFace_Space_README.md    # Hugging Face Space README
├── LICENSE                        # MIT License
├── .gitignore                     # Git ignore file
└── DEPLOYMENT_GUIDE.md            # This file
```

## 🐙 GitHub Deployment

### Step 1: Create a New Repository

1. Go to [GitHub](https://github.com) and click "New repository"
2. Name it: `customer-segmentation-predictor`
3. Make it public
4. Don't initialize with README (we have our own)

### Step 2: Upload Your Files

**Option A: Using Git Command Line**
```bash
git init
git add .
git commit -m "Initial commit: Customer segmentation predictor"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/customer-segmentation-predictor.git
git push -u origin main
```

**Option B: Using GitHub Web Interface**
1. Click "uploading an existing file"
2. Drag and drop all files (including your .pkl model files)
3. Commit changes

### Step 3: Update README

- Replace `YOUR_USERNAME` with your actual GitHub username
- Add your contact information
- Update the Hugging Face Space link once created

## 🤗 Hugging Face Deployment

### Step 1: Create a New Space

1. Go to [Hugging Face](https://huggingface.co)
2. Click "New" → "Space"
3. Name it: `customer-segmentation`
4. Select SDK: `Gradio`
5. Make it public
6. Click "Create Space"

### Step 2: Upload Files

1. **Upload the special README**: 
   - Rename `HuggingFace_Space_README.md` to `README.md`
   - Upload it to your Hugging Face Space

2. **Upload all other files**:
   - `app.py`
   - `requirements.txt`
   - `scaler.pkl` (your trained scaler)
   - `kmeans_model.pkl` (your trained model)

### Step 3: Configuration

The `README.md` for Hugging Face contains metadata at the top:
```yaml
---
title: Customer Segmentation Predictor
emoji: 🛍️
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: 4.44.0
app_file: app.py
pinned: false
license: mit
---
```

This configures your Space automatically.

## 🔧 Important Notes

### Model Files
- Make sure your `scaler.pkl` and `kmeans_model.pkl` files are in the root directory
- These files should be generated from your training notebook
- File sizes should be reasonable (< 100MB for free tier)

### Dependencies
- The `requirements.txt` includes all necessary packages
- Gradio version is pinned for stability
- scikit-learn version should match your training environment

### Testing Locally
Before deploying, test locally:
```bash
pip install -r requirements.txt
python app.py
```

## 🚀 Post-Deployment

### GitHub
- Enable GitHub Pages if you want a project website
- Add topics/tags for better discoverability
- Consider adding a CONTRIBUTING.md file

### Hugging Face
- Your Space will be available at: `https://huggingface.co/spaces/YOUR_USERNAME/customer-segmentation`
- It will auto-rebuild when you push changes
- Monitor the build logs for any issues

## 🐛 Troubleshooting

### Common Issues:

1. **Model files not found**
   - Ensure `scaler.pkl` and `kmeans_model.pkl` are in the root directory
   - Check file names match exactly

2. **Import errors**
   - Verify all packages are in `requirements.txt`
   - Check version compatibility

3. **Gradio interface not loading**
   - Check the `app.py` file for syntax errors
   - Ensure the interface is properly defined

4. **Large file sizes**
   - Use Git LFS for files > 100MB
   - Consider model compression techniques

## 📞 Support

- **GitHub Issues**: Use the Issues tab on your repository
- **Hugging Face Community**: Check the Hugging Face forums
- **Documentation**: Refer to Gradio and Hugging Face docs

## ✅ Checklist

Before deploying:
- [ ] All files are in the correct directory
- [ ] Model files (.pkl) are included
- [ ] README.md is updated with your information
- [ ] Requirements.txt has all dependencies
- [ ] App.py runs locally without errors
- [ ] GitHub repository is created
- [ ] Hugging Face Space is created
- [ ] All files are uploaded to both platforms

---

🎉 **Congratulations!** Your Customer Segmentation Predictor is now deployed and ready to use!