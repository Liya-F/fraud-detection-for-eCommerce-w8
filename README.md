# Fraud Detection for E-Commerce Transactions

This project aims to detect fraudulent e-commerce transactions using machine learning. It includes data preprocessing, feature engineering, handling class imbalance, training classification models, evaluating them with appropriate metrics, and explaining predictions using SHAP.

## Objective

Build robust pipelines to preprocess data, address fraud-specific challenges such as class imbalance, train machine learning models, and interpret predictions to identify fraudulent behavior effectively.

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

### Model Explainability (SHAP)

SHAP was used to interpret Random Forest predictions.

- SHAP Summary Plots to identify globally important features.
- SHAP Force Plots for local explanations of individual predictions.
- Used TreeExplainer with performance tuning for SHAP computation.
- Subsampled data for efficiency and clarity in visualizations.
