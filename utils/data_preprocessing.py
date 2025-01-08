# utils/data_preprocessing.py
from sklearn.preprocessing import MinMaxScaler
import numpy as np

class DataPreprocessor:
    @staticmethod
    def preprocess_data(df, feature_columns):
        scaler = MinMaxScaler()
        df_scaled = df.copy()
        df_scaled[feature_columns] = scaler.fit_transform(df[feature_columns])
        return df_scaled, scaler