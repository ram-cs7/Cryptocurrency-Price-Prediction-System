# models/xgboost_model.py
import xgboost as xgb
import numpy as np
from .base_model import BaseModel

class XGBoostModel(BaseModel):
    def __init__(self, config):
        self.config = config
        self.model = xgb.XGBRegressor(
            n_estimators=100,
            learning_rate=0.1,
            max_depth=5,
            min_child_weight=1,
            subsample=0.8,
            colsample_bytree=0.8,
            random_state=42,
            n_jobs=-1
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
        if validation_data is not None:
            eval_set = [(validation_data[0], validation_data[1])]
            return self.model.fit(X_train, y_train, eval_set=eval_set,
                                early_stopping_rounds=10, verbose=False)
        return self.model.fit(X_train, y_train)
    
    def predict(self, X):
        return self.model.predict(X)