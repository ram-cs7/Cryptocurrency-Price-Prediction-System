# config/config.py
from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    # API Configuration
    BINANCE_API_KEY = os.getenv('BINANCE_API_KEY')
    BINANCE_SECRET = os.getenv('BINANCE_SECRET')
    
    # Data Parameters
    DATA_DIR = Path('data')
    MODEL_DIR = Path('models')
    SEQUENCE_LENGTH = 60
    FEATURE_COLUMNS = ['open', 'high', 'low', 'close', 'volume']
    TARGET_COLUMN = 'close'
    TRAIN_SPLIT = 0.8
    
    # Model Parameters
    LSTM_UNITS = 50
    DROPOUT_RATE = 0.2
    BATCH_SIZE = 32
    EPOCHS = 50
    
    def __init__(self):
        self.DATA_DIR.mkdir(exist_ok=True)
        self.MODEL_DIR.mkdir(exist_ok=True)