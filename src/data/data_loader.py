import pandas as pd

class DataLoader:
    def __init__(self, fraud_data_path: str, ip_country_path: str):
        self.fraud_data_path = fraud_data_path
        self.ip_country_path = ip_country_path
        self.fraud_df = None
        self.ip_country_df = None

    def load_data(self):
        self.fraud_df = pd.read_csv(self.fraud_data_path)
        self.ip_country_df = pd.read_csv(self.ip_country_path)
        return self.fraud_df, self.ip_country_df

    def check_missing_values(self):
        print("Missing values in Fraud Data:")
        print(self.fraud_df.isnull().sum())
        print("\nMissing values in IP Address to Country Data:")
        print(self.ip_country_df.isnull().sum())

    def handle_missing_values(self):
        # Example logic (can be customized later):
        self.fraud_df.dropna(inplace=True)
        self.ip_country_df.dropna(inplace=True)
        print("Missing values handled (rows with missing data dropped).")
        return self.fraud_df, self.ip_country_df
