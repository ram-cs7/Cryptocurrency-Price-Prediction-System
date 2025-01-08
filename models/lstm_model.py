# models/lstm_model.py
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from .base_model import BaseModel

class LSTMModel(BaseModel):
    def __init__(self, config):
        self.config = config
        self.model = self._build_model()
    
    def _build_model(self):
        model = Sequential([
            LSTM(self.config.LSTM_UNITS, return_sequences=True, 
                 input_shape=(self.config.SEQUENCE_LENGTH, len(self.config.FEATURE_COLUMNS))),
            Dropout(self.config.DROPOUT_RATE),
            LSTM(self.config.LSTM_UNITS, return_sequences=False),
            Dropout(self.config.DROPOUT_RATE),
            Dense(1)
        ])
        model.compile(optimizer='adam', loss='mse')
        return model

    def prepare_sequences(self, data):
        X, y = [], []
        for i in range(len(data) - self.config.SEQUENCE_LENGTH):
            X.append(data[i:(i + self.config.SEQUENCE_LENGTH)])
            y.append(data[i + self.config.SEQUENCE_LENGTH, 
                    self.config.FEATURE_COLUMNS.index('close')])
        return np.array(X), np.array(y)