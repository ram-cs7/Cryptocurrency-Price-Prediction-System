# models/svm_model.py
from sklearn.svm import SVR
import numpy as np
from .base_model import BaseModel

class SVMModel(BaseModel):
    def __init__(self, config):
        self.config = config
        self.model = SVR(
            kernel='rbf',
            C=1.0,
            epsilon=0.1,
            gamma='scale'
        )
    
    def prepare_sequences(self, data):
        X, y = [], []
        for i in range(len(data) - self.config.SEQUENCE_LENGTH):
            sequence = data[i:(i + self.config.SEQUENCE_LENGTH)]
            X.append(sequence.flatten())
            y.append(data[i + self.config.SEQUENCE_LENGTH,
                    self.config.FEATURE_COLUMNS.index('close')])
        return np.array(X), np.array(y)
    
    def train(self, X_train, y_train, validation_data=None):
        return self.model.fit(X_train, y_train)
    
    def predict(self, X):
        return self.model.predict(X)