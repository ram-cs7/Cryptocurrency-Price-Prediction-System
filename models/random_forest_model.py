# models/random_forest_model.py
from sklearn.ensemble import RandomForestRegressor
import numpy as np
from .base_model import BaseModel

class RandomForestModel(BaseModel):
    def __init__(self, config):
        self.config = config
        self.model = RandomForestRegressor(
            n_estimators=100,
            max_depth=10,
            min_samples_split=5,
            min_samples_leaf=2,
            random_state=42,
            n_jobs=-1
        )
    
    def prepare_sequences(self, data):
        X, y = [], []
        for i in range(len(data) - self.config.SEQUENCE_LENGTH):
            sequence = data[i:(i + self.config.SEQUENCE_LENGTH)]
            X.append(sequence.flatten())  # Flatten the sequence for RF
            y.append(data[i + self.config.SEQUENCE_LENGTH,
                    self.config.FEATURE_COLUMNS.index('close')])
        return np.array(X), np.array(y)
    
    def train(self, X_train, y_train, validation_data=None):
        return self.model.fit(X_train, y_train)
    
    def predict(self, X):
        return self.model.predict(X)