# Adult Income Prediction 💰

## Author: Mohamed Mohamed Shatia

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.1%2B-orange)
![License](https://img.shields.io/badge/License-MIT-green)

A machine learning pipeline to predict whether an individual's income exceeds $50K/year using census data.

---

## 📌 Table of Contents
1. [Overview](#-overview)
2. [Features](#-features)
3. [Installation](#-installation)
4. [Usage](#-usage)
5. [Project Structure](#-project-structure)
6. [Contact](#-contact)

---

## 🔍 Overview

This project presents a complete end-to-end machine learning pipeline that leverages the UCI Adult Income dataset. The goal is to develop a predictive model that can accurately classify whether an individual earns more than $50K per year based on a range of demographic and employment features such as age, education, marital status, and hours worked per week.

The pipeline covers all essential stages of a data science workflow:

- **Exploratory Data Analysis** to understand feature distributions and correlations.
- **Preprocessing**: handling missing values, stripping whitespace, and encoding categorical data.
- **Feature Engineering**: creating new features like `net_capital`.
- **Handling Class Imbalance** with resampling techniques like `SMOTETomek`.
- **Model Training**: evaluating various classifiers such as Logistic Regression, Random Forest, and XGBoost.
- **Hyperparameter Tuning** to optimize the best-performing model.
- **Evaluation** using metrics like precision, recall, and F1-score.

The final outcome is an interpretable and scalable XGBoost model that can assist in predicting income levels.

---

## 🚀 Features

✅ Full end-to-end ML pipeline.
✅ Multiple models evaluated: Logistic Regression, Random Forest, XGBoost, etc.
✅ Handles missing values & imbalanced data using `SMOTETomek`.
✅ In-depth feature analysis and engineering.
✅ Visualizations: correlation plots, feature importance, and distribution plots.
✅ Modular notebooks for easy updates and experimentation.

---

## 🛠 Installation

1.  **Clone the Repository**:
    ```bash
    git clone <https://github.com/mohamedshatia29/Predict-Adult-Income-Based-on-Census-Data.git>
    cd <https://github.com/mohamedshatia29/Predict-Adult-Income-Based-on-Census-Data.git>
    ```

2.  **Install Dependencies**:
    A `requirements.txt` file is recommended. You can create one with:
    ```bash
    pip freeze > requirements.txt
    ```
    Then install the necessary packages:
    ```bash
    pip install -r requirements.txt
    ```

---
## 📌 Usage

### 🔹 `00_exploration.ipynb` & `01_analytics.ipynb`:
   Perform Exploratory Data Analysis (EDA) — visualize distributions, clean the data, and perform feature engineering.

### 🔹 `02_Pre-Processing.ipynb`:
   Execute the core ML pipeline: data preprocessing, handling imbalances (e.g., `SMOTETomek`), model training, and evaluation with Logistic Regression, Random Forest, XGBoost, etc.

### 🔹 `03_Test_Model.ipynb`:
   Load the final `xgboost_model.pkl` and test it with sample data to get predictions.

---

## 📁 Project Structure

```
Epsilon project/
├── Dataset/
│   ├── raw/adult.csv
│   └── processed/
├── Notebooks/
│   ├── 00_exploration.ipynb
│   ├── 01_analytics.ipynb
│   ├── 02_Pre-Processing.ipynb
│   ├── 03_Test_Model.ipynb
│   ├── xgboost_model.pkl
│   └── app.py
├── requirements.txt
└── README.md
```

---

## 🤝 Contributing
Contributions are welcome! To contribute:
1. *Fork the repository.*
2. *Create a new branch:*
   ```bash
   git checkout -b feature/YourFeature
   ```
3. *Commit your changes:*
   ```bash
   git commit -m "Add new feature"
   ```
4. *Push to the branch:*
   ```bash
   git push origin feature/YourFeature
   ```
5. *Open a Pull Request.*

---

## 📧 Contact
For questions or feedback, feel free to reach out:

📩 *Email:* mohamedshatia405@gmail.com
🔗 *GitHub:* [Mohamed Shatia](https://github.com/mohamedshatia29)

---

📌 *If you find this project helpful, don't forget to ⭐ the repository!* 🚀

