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

## 🚀 Quick Start

### Online Demo
Try the live demo: [Hugging Face Space](https://huggingface.co/spaces/YOUR_USERNAME/customer-segmentation)

### Local Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/customer-segmentation-predictor.git
   cd customer-segmentation-predictor
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Open your browser** and navigate to `http://localhost:7860`

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

## 📁 Project Structure

```
customer-segmentation-predictor/
├── app.py                 # Main Gradio application
├── requirements.txt       # Python dependencies
├── scaler.pkl            # Trained StandardScaler
├── kmeans_model.pkl      # Trained K-Means model
├── README.md             # Project documentation
└── .gitignore           # Git ignore file
```

## 🎮 Usage

1. **Age**: Select customer age (18-70 years)
2. **Annual Income**: Set income in thousands of dollars (15-137k)
3. **Spending Score**: Choose spending behavior score (1-100)
4. **Get Prediction**: View the predicted customer segment

## 📈 Example Predictions

| Age | Income | Spending | Predicted Segment |
|-----|--------|----------|------------------|
| 25  | 40k    | 80       | Sensible         |
| 45  | 100k   | 30       | Careless         |
| 35  | 60k    | 60       | Standard         |
| 55  | 25k    | 85       | Sensible         |
| 30  | 80k    | 75       | Target           |

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Dataset: Customer segmentation data
- Framework: Gradio for the web interface
- ML Library: scikit-learn for clustering algorithms

## 📞 Contact

- **GitHub**: [@YOUR_USERNAME](https://github.com/YOUR_USERNAME)
- **LinkedIn**: [Your Name](https://linkedin.com/in/yourprofile)
- **Email**: your.email@example.com

---

⭐ If you found this project helpful, please give it a star on GitHub!