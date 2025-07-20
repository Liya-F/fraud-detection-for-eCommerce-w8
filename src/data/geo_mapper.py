import pandas as pd
import numpy as np

class GeoMapper:
    def __init__(self, fraud_df: pd.DataFrame, ip_df: pd.DataFrame):
        self.fraud_df = fraud_df.copy()
        self.ip_df = ip_df.copy()

    def convert_ip_column(self):
        self.fraud_df['ip_address'] = self.fraud_df['ip_address'].astype(np.int64)
        return self.fraud_df

    def map_ip_to_country(self):
        # Sort for efficient matching
        self.ip_df = self.ip_df.sort_values(by='lower_bound_ip_address')

        def find_country(ip):
            match = self.ip_df[
                (self.ip_df['lower_bound_ip_address'] <= ip) &
                (self.ip_df['upper_bound_ip_address'] >= ip)
            ]
            return match['country'].values[0] if not match.empty else 'Unknown'

        self.fraud_df['country'] = self.fraud_df['ip_address'].apply(find_country)
        return self.fraud_df
