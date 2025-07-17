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

# Customer Segmentation Predictor

A machine learning application that predicts customer segments based on age, annual income, and spending score using K-Means clustering.

## 🎯 Features

- **Interactive Web Interface**: Built with Gradio for easy use
- **Real-time Predictions**: Instant customer segment classification
- **Five Customer Categories**: Comprehensive segmentation system
- **User-friendly Design**: Intuitive sliders and clear descriptions

## 🛍️ Customer Segments

The model classifies customers into five distinct categories:

1. **Standard** - Average income and spending patterns
2. **Careful** - Low income, low spending (budget-conscious customers)
3. **Target** - High income, high spending (premium customers)
4. **Careless** - High income, low spending (potential for growth)
5. **Sensible** - Low income, high spending (value-seekers)

## 🚀 Usage

1. **Age**: Select customer age (18-70 years)
2. **Annual Income**: Set income in thousands of dollars (15-137k)
3. **Spending Score**: Choose spending behavior score (1-100)
4. **Get Prediction**: View the predicted customer segment

## 📊 Model Details

- **Algorithm**: K-Means Clustering
- **Features**: Age, Annual Income, Spending Score
- **Preprocessing**: StandardScaler for feature normalization
- **Clusters**: 5 distinct customer segments

## 🔧 Technical Stack

- **Frontend**: Gradio
- **Machine Learning**: scikit-learn
- **Data Processing**: NumPy, Pandas
- **Model Persistence**: joblib

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference