# 🚕 The Ride Price Predictor

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B.svg)](https://streamlit.io)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3+-F7931E.svg)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **ML-powered ride fare estimator using Linear Regression** | Predicts ride prices based on distance, duration, time of day & ride type

---

## 📋 Project Overview

**The Ride Price Predictor** is a machine learning project that estimates ride fares using **Linear Regression**. This project demonstrates the complete ML workflow — from data cleaning and feature engineering to model training, evaluation, and deployment via an interactive Streamlit app.

### 🎯 Key Features

- ✅ **End-to-End ML Pipeline**: Data preprocessing → Model training → Evaluation → Prediction
- ✅ **Multi-Factor Prediction**: Considers distance, duration, time of day, and ride type
- ✅ **Interactive Web App**: User-friendly Streamlit interface for real-time predictions
- ✅ **Model Performance Metrics**: R² score, MAE, RMSE evaluation
- ✅ **Feature Engineering**: Smart handling of categorical and numerical features

---

## 🛠️ Technologies & Skills

### **Core Technologies**
- **Python 3.8+** - Primary programming language
- **Pandas & NumPy** - Data manipulation and numerical computing
- **Scikit-learn** - Machine learning modeling (Linear Regression)
- **Streamlit** - Interactive web application framework
- **Matplotlib/Seaborn** - Data visualization

### **Skills Demonstrated**
- Data preprocessing and cleaning
- Feature selection and engineering
- Linear Regression modeling
- Model evaluation (R², MAE, RMSE)
- Hyperparameter tuning
- Web app deployment

---

## 📂 Project Structure

```
ride-price-predictor/
│
├── data/
│   ├── raw/                 # Raw dataset files
│   ├── processed/           # Cleaned and preprocessed data
│   └── README.md            # Data description
│
├── notebooks/
│   ├── 01_EDA.ipynb        # Exploratory Data Analysis
│   ├── 02_Model_Training.ipynb  # Model development
│   └── 03_Model_Evaluation.ipynb  # Performance analysis
│
├── src/
│   ├── data_preprocessing.py   # Data cleaning functions
│   ├── feature_engineering.py  # Feature creation
│   ├── model_training.py       # Model training pipeline
│   └── prediction.py           # Prediction functions
│
├── models/
│   └── ride_price_model.pkl    # Trained model file
│
├── app.py                   # Streamlit web application
├── requirements.txt         # Project dependencies
├── .gitignore              # Git ignore file
└── README.md               # Project documentation (this file)
```

---

## 🚀 Getting Started

### **Prerequisites**

Make sure you have Python 3.8+ installed on your system.

### **Installation**

1. **Clone the repository**
   ```bash
   git clone https://github.com/mayank-goyal09/ride-price-predictor.git
   cd ride-price-predictor
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### **Usage**

#### **1. Training the Model**
```bash
python src/model_training.py
```

#### **2. Running the Streamlit App**
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

#### **3. Making Predictions**
Use the interactive interface to input:
- Distance (km)
- Duration (minutes)
- Time of day (Morning/Afternoon/Evening/Night)
- Ride type (Economy/Premium/Luxury)

Get instant fare predictions! 💰

---

## 📊 Model Performance

| Metric | Value |
|--------|-------|
| **R² Score** | 0.XX |
| **Mean Absolute Error (MAE)** | ₹XX.XX |
| **Root Mean Squared Error (RMSE)** | ₹XX.XX |

*Update these values after training your model*

---

## 📈 Features Used

### **Numerical Features**
- Distance (km)
- Duration (minutes)

### **Categorical Features**
- Time of Day (Morning, Afternoon, Evening, Night)
- Ride Type (Economy, Premium, Luxury)

### **Engineered Features**
- Speed (Distance/Duration)
- Peak hour indicator
- Weekend/Weekday flag

---

## 🔮 Future Enhancements

- [ ] Add more features (weather, traffic conditions, surge pricing)
- [ ] Implement advanced models (Random Forest, XGBoost)
- [ ] Create API endpoints for integration
- [ ] Add model versioning with MLflow
- [ ] Deploy to cloud platform (AWS/GCP/Heroku)
- [ ] Build mobile-responsive UI

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Mayank Goyal**  
🔗 [LinkedIn](https://www.linkedin.com/in/mayank-goyal-4b8756363/)  
🔗 [GitHub](https://github.com/mayank-goyal09)  
📧 itsmaygal09@gmail.com

---

## 🙏 Acknowledgments

- Dataset source: [Add your data source]
- Inspiration: Real-world ride-sharing pricing models
- Built as part of ML portfolio project series

---

<div align="center">
  <strong>⭐ If you found this project helpful, please give it a star! ⭐</strong>
</div>