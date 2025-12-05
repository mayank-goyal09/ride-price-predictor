# 📁 Project Structure Guide

This document explains the organization of the **Ride Price Predictor** project.

---

## 📂 Directory Layout

### **`data/`** - Dataset Storage
```
data/
├── raw/              # Original, unmodified dataset
│   └── rides.csv
├── processed/        # Cleaned and preprocessed data
│   └── rides_cleaned.csv
└── README.md        # Data description and sources
```

**Purpose**: Separates raw data from processed data to maintain data lineage.

---

### **`notebooks/`** - Jupyter Notebooks
```
notebooks/
├── 01_EDA.ipynb                    # Exploratory Data Analysis
├── 02_Model_Training.ipynb         # Model development
└── 03_Model_Evaluation.ipynb       # Performance analysis
```

**Purpose**: Interactive analysis and experimentation. Each notebook focuses on one stage of the ML pipeline.

---

### **`src/`** - Source Code
```
src/
├── data_preprocessing.py    # Data cleaning functions
├── feature_engineering.py   # Feature creation
├── model_training.py        # Model training pipeline
└── prediction.py            # Prediction functions
```

**Purpose**: Modular, reusable Python code for production use.

---

### **`models/`** - Trained Models
```
models/
└── ride_price_model.pkl    # Serialized trained model
```

**Purpose**: Stores trained model files for deployment.

---

### **Root Files**

- **`app.py`** - Main Streamlit application
- **`requirements.txt`** - Python dependencies
- **`.gitignore`** - Files to exclude from Git
- **`README.md`** - Project documentation

---

## 🔄 Typical Workflow

1. **Data Collection** → Place raw data in `data/raw/`
2. **Exploration** → Use `notebooks/01_EDA.ipynb`
3. **Preprocessing** → Run `src/data_preprocessing.py`
4. **Feature Engineering** → Run `src/feature_engineering.py`
5. **Model Training** → Use `notebooks/02_Model_Training.ipynb` or `src/model_training.py`
6. **Evaluation** → Use `notebooks/03_Model_Evaluation.ipynb`
7. **Deployment** → Run `app.py` for Streamlit app

---

## 💡 Best Practices

✅ **Keep raw data untouched** - Always work with copies  
✅ **Version your models** - Save models with timestamps  
✅ **Document your code** - Add docstrings and comments  
✅ **Use relative paths** - Ensures portability  
✅ **Commit regularly** - Small, meaningful commits  

---

**Happy Coding! 🚀**
