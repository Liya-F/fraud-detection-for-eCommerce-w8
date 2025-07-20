import pandas as pd

class DataCleaner:
    def __init__(self, fraud_df: pd.DataFrame):
        self.fraud_df = fraud_df

    def remove_duplicates(self):
        before = self.fraud_df.shape[0]
        self.fraud_df = self.fraud_df.drop_duplicates()
        after = self.fraud_df.shape[0]
        print(f"Removed {before - after} duplicate rows.")
        return self.fraud_df

    def correct_data_types(self):
        try:
            self.fraud_df['signup_time'] = pd.to_datetime(self.fraud_df['signup_time'])
            self.fraud_df['purchase_time'] = pd.to_datetime(self.fraud_df['purchase_time'])
            self.fraud_df['age'] = pd.to_numeric(self.fraud_df['age'], errors='coerce')
            self.fraud_df['purchase_value'] = pd.to_numeric(self.fraud_df['purchase_value'], errors='coerce')
            self.fraud_df['ip_address'] = pd.to_numeric(self.fraud_df['ip_address'], errors='coerce')
            print("Converted data types successfully.")
        except Exception as e:
            print("Error converting data types:", e)
        return self.fraud_df
