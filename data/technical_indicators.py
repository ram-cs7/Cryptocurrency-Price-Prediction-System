# data/technical_indicators.py
import pandas as pd
import numpy as np
import talib

class TechnicalIndicators:
    @staticmethod
    def add_all_indicators(df):
        # Trend Indicators
        df['ema_9'] = talib.EMA(df['close'], timeperiod=9)
        df['ema_21'] = talib.EMA(df['close'], timeperiod=21)
        df['sma_50'] = talib.SMA(df['close'], timeperiod=50)
        
        # Momentum Indicators
        df['rsi'] = talib.RSI(df['close'], timeperiod=14)
        df['macd'], df['macd_signal'], _ = talib.MACD(df['close'])
        
        # Volatility Indicators
        df['atr'] = talib.ATR(df['high'], df['low'], df['close'], timeperiod=14)
        
        return df