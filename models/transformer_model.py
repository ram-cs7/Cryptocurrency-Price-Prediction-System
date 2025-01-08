# models/transformer_model.py
import tensorflow as tf
import numpy as np
from .base_model import BaseModel

class TransformerModel(BaseModel):
    def __init__(self, config):
        self.config = config
        self.model = self._build_transformer()
    
    def _build_transformer(self):
        input_shape = (self.config.SEQUENCE_LENGTH, len(self.config.FEATURE_COLUMNS))
        
        inputs = tf.keras.Input(shape=input_shape)
        x = inputs
        
        # Transformer Encoder
        x = tf.keras.layers.MultiHeadAttention(
            num_heads=8, key_dim=64
        )(x, x)
        x = tf.keras.layers.LayerNormalization(epsilon=1e-6)(x)
        x = tf.keras.layers.Dense(128, activation='relu')(x)
        x = tf.keras.layers.Dense(64, activation='relu')(x)
        x = tf.keras.layers.GlobalAveragePooling1D()(x)
        x = tf.keras.layers.Dense(32, activation='relu')(x)
        outputs = tf.keras.layers.Dense(1)(x)
        
        model = tf.keras.Model(inputs=inputs, outputs=outputs)
        model.compile(optimizer='adam', loss='mse')
        return model
    
    def prepare_sequences(self, data):
        X, y = [], []
        for i in range(len(data) - self.config.SEQUENCE_LENGTH):
            X.append(data[i:(i + self.config.SEQUENCE_LENGTH)])
            y.append(data[i + self.config.SEQUENCE_LENGTH,
                    self.config.FEATURE_COLUMNS.index('close')])
        return np.array(X), np.array(y)
    
    def train(self, X_train, y_train, validation_data=None):
        return self.model.fit(
            X_train, y_train,
            validation_data=validation_data,
            epochs=self.config.EPOCHS,
            batch_size=self.config.BATCH_SIZE
        )
    
    def predict(self, X):
        return self.model.predict(X)