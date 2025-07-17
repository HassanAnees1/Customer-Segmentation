---
title: Customer Segmentation
emoji: 🛍️
colorFrom: pink
colorTo: indigo
sdk: gradio
sdk_version: "4.26.0"
app_file: app.py
pinned: false
---

# 🛍️ Customer Segmentation Predictor

A machine learning web application that segments mall customers based on their age, annual income, and spending score using the K-Means clustering algorithm.

---

## 🎯 Features

- ✅ **Interactive Interface** – Built with Gradio
- 📊 **Real-Time Visualization** – Adjust number of clusters and instantly view groupings
- 📁 **Uses Clean Dataset** – Mall customer data with 5 useful features
- 📉 **Unsupervised Learning** – No labels required
- 💡 **Cluster Insights** – Understand customer behaviors visually

---

## 🛍️ Customer Segments (Example Labels)

The app segments customers into distinct clusters. When using 5 clusters, these can be interpreted as:

1. **Standard** – Average income and spending
2. **Careful** – Low income, low spending
3. **Target** – High income, high spending (ideal for marketing)
4. **Careless** – High income, low spending (untapped opportunity)
5. **Sensible** – Low income, high spending (value-oriented)

> 💬 *These labels are suggestive only. Actual segmentation is based on KMeans output and may vary.*

---

## 🚀 Quick Start

### 🔗 Try the Live App

👉 [Launch on Hugging Face Spaces](https://huggingface.co/spaces/HassanAnees1/Customer-Segmentation)

### 🖥️ Run Locally

1. Clone the repository:

```bash
git clone https://github.com/HassanAnees1/Customer-Segmentation.git
cd Customer-Segmentation
````

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Launch the app:

```bash
python app.py
```

4. Open your browser and go to:

```
http://localhost:7860
```

---

## 📊 Model Information

| Component              | Description                              |
| ---------------------- | ---------------------------------------- |
| **Model**              | KMeans (scikit-learn)                    |
| **Type**               | Unsupervised                             |
| **Features**           | Age, Annual Income (k\$), Spending Score |
| **Preprocessing**      | StandardScaler (normalization)           |
| **Number of Clusters** | Adjustable (default = 5)                 |

---

## 🧰 Tech Stack

* 🧠 **Machine Learning**: `scikit-learn`
* 🖼️ **Frontend**: `Gradio`
* 📊 **Visualization**: `matplotlib`, `seaborn`
* 📂 **Data Handling**: `pandas`, `numpy`
* 💻 **Platform**: Hugging Face Spaces

---

## 📁 Project Structure

```
Customer-Segmentation/
├── app.py                 # Gradio app file
├── Mall_Customers.csv     # Dataset file
├── kmeans_model.pkl       # (Optional) Pre-trained KMeans model
├── README.md              # This documentation
├── LICENSE                # MIT License file
├── requirements.txt       # Python dependencies
├── HF_README.md           # Optional Hugging Face config
├── DEPLOYMENT_GUIDE.md    # Deployment instructions
└── Custumer.ipynb         # Jupyter notebook (exploration & EDA)
```

---

## 🧪 How to Use the App

1. **Select number of clusters (2 to 10)** using the slider.
2. The app runs KMeans clustering on the dataset.
3. Customers are segmented and visualized by:

   * **Annual Income** (X-axis)
   * **Spending Score** (Y-axis)
   * **Color-coded clusters**

---

## 📈 Example Cluster Assignments

| Age | Income (k\$) | Spending Score | Cluster   |
| --- | ------------ | -------------- | --------- |
| 25  | 40           | 80             | Cluster 4 |
| 45  | 100          | 30             | Cluster 2 |
| 35  | 60           | 60             | Cluster 0 |
| 55  | 25           | 85             | Cluster 3 |
| 30  | 80           | 75             | Cluster 1 |

---

## 🔧 Advanced Features (coming soon)

* Upload your own dataset 📤
* Export clustered results as CSV 📁
* Customize color palette 🎨

---

## 🤝 Contributing

Contributions are welcome! Follow these steps:

```bash
# 1. Fork the repo
# 2. Create a branch
git checkout -b feature/amazing-feature

# 3. Commit your changes
git commit -m "Add amazing feature"

# 4. Push and open PR
git push origin feature/amazing-feature
```

---

## 📄 License

This project is licensed under the **MIT License**.
See the [LICENSE](LICENSE) file for full details.

---

## 🙏 Acknowledgments

* Dataset: [Mall Customer Dataset](https://www.kaggle.com/vjchoudhary7/customer-segmentation-tutorial-in-python)
* ML: `scikit-learn`
* UI: `Gradio`
* Hosting: `Hugging Face Spaces`

---

## 📞 Contact

* 📧 Email: [hassananees188@gmail.com](mailto:hassananees188@gmail.com)
* 🔗 LinkedIn: [Hassan Elzeny](https://linkedin.com/in/hassan-elzeny)
* 🐙 GitHub: [@HassanAnees1](https://github.com/HassanAnees1)

---

⭐ **If you like this project, give it a ⭐ star on GitHub!**