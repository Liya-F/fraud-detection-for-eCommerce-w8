# 🛡️ Fraud Detection for E-Commerce Transactions

This project focuses on detecting fraudulent e-commerce transactions using data-driven techniques. It involves loading, cleaning, and enriching transactional data, followed by engineering features that help distinguish legitimate behavior from potential fraud. The prepared dataset will be used in later stages for machine learning model development and evaluation.

## Objective

The objective is to build a reliable and well-structured preprocessing pipeline that prepares e-commerce transaction data for fraud detection. This includes handling missing values, extracting behavioral and time-based features, addressing class imbalance, and encoding and scaling the data for modeling.

## Datasets

- **Fraud_Data.csv**: Contains user and transaction information such as signup time, purchase time, browser, source, device ID, age, and IP address, along with the fraud label.
- **IpAddress_to_Country.csv**: Maps IP address ranges to their corresponding countries, which is used for geolocation enrichment.

## 🔧 Main Steps

- **Data Loading**: Custom classes are used to load and structure data efficiently.
- **Cleaning**: Duplicate entries are removed, and column data types are corrected for consistency.
- **Exploratory Analysis**: Distributions of numeric and categorical variables are explored, and relationships with fraud labels are visualized.
- **IP Geolocation**: IP addresses are converted to integers and mapped to countries to enhance location-based insights.
- **Feature Engineering**:
  - Extracted time-related fields like `hour_of_day`, `day_of_week`, and `time_since_signup`.
  - Calculated behavioral metrics such as user transaction count and average transaction velocity.
- **Class Imbalance Handling**: SMOTE (Synthetic Minority Over-sampling Technique) is applied to improve the balance between fraudulent and legitimate transactions.
- **Encoding & Scaling**: Categorical variables are one-hot encoded, and numeric features are standardized using `StandardScaler`.

## Technologies Used

- **Python** (pandas, numpy)
- **Visualization**: seaborn, matplotlib
- **Machine Learning Prep**: scikit-learn, imbalanced-learn (SMOTE)

## Next Phase

The cleaned and enriched dataset is now ready for training classification models. Future steps include model building, evaluation using precision-recall metrics, and applying explainability methods to understand model decisions.

---

