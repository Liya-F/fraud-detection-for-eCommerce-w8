import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class DataExplorer:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def describe_data(self):
        print("\n Descriptive Statistics (Numeric Features):")
        print(self.df.describe())
        
        print("\n Value Counts (Categorical Features):")
        categorical_cols = self.df.select_dtypes(include='object').columns
        for col in categorical_cols:
            print(f"\nColumn: {col}")
            print(self.df[col].value_counts())

    def plot_distributions(self):
        numeric_cols = self.df.select_dtypes(include=['int64', 'float64']).columns
        for col in numeric_cols:
            plt.figure(figsize=(6, 4))
            sns.histplot(self.df[col], kde=True, bins=30)
            plt.title(f'Distribution of {col}')
            plt.xlabel(col)
            plt.ylabel("Frequency")
            plt.tight_layout()
            plt.show()
            
    def plot_categorical_vs_target(self, target_col='class'):
        categorical_cols = self.df.select_dtypes(include='object').columns
        for col in categorical_cols:
            plt.figure(figsize=(6, 4))
            sns.countplot(data=self.df, x=col, hue=target_col)
            plt.title(f'{col} vs {target_col}')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()

    def plot_numeric_vs_target(self, target_col='class'):
        numeric_cols = self.df.select_dtypes(include=['int64', 'float64']).columns
        numeric_cols = [col for col in numeric_cols if col != target_col]

        for col in numeric_cols:
            plt.figure(figsize=(6, 4))
            sns.boxplot(x=target_col, y=col, data=self.df)
            plt.title(f'{col} vs {target_col}')
            plt.tight_layout()
            plt.show()

    def correlation_heatmap(self):
        plt.figure(figsize=(10, 6))
        corr = self.df.corr(numeric_only=True)
        sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
        plt.title("Correlation Heatmap")
        plt.tight_layout()
        plt.show()

