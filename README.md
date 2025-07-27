# Fraud Detection for E-Commerce Transactions

This project aims to detect fraudulent e-commerce transactions using machine learning. It involves structured data preprocessing, feature engineering, handling class imbalance, and evaluating classification models using appropriate metrics for imbalanced data.

## Objective

Build robust pipelines to preprocess data, handle fraud-specific challenges (like imbalance), and train & evaluate models to identify fraudulent behavior effectively.

## Datasets Used

- `Fraud_Data.csv` + `IpAddress_to_Country.csv` – For behavioral and location-based fraud detection.
- `creditcard.csv` – For detecting fraud in credit card transactions.

## Key Steps

### Preprocessing & Feature Engineering

- Handled missing values, duplicates, and inconsistent types.
- Enriched data with:
  - IP-to-country mapping
  - Time-based features (`time_since_signup`, `hour_of_day`, etc.)
  - Behavioral metrics (user transaction count, etc.)
- Addressed **class imbalance** using SMOTE.
- One-hot encoded categorical features and standardized numeric ones.

### Model Training & Evaluation

Models trained on both datasets:
- **Logistic Regression**
- **Random Forest Classifier**

Evaluation included:
- **F1-Score**
- **Confusion Matrix**
- **Precision-Recall AUC**
- **ROC Curve**

## Status
- Preprocessing pipelines  
- Trained & evaluated 4 models (2 per dataset)  
- Visual evaluation and metric-based comparison using consistent evaluation workflow

