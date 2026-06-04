# Cryptocurrency Price Prediction System

## Overview
A comprehensive cryptocurrency price prediction system that uses multiple machine learning models and technical analysis to predict price movements. The system includes data collection, preprocessing, model training, backtesting, and a web interface for visualization.

## Features
- Multiple ML model implementations:
  - LSTM (Long Short-Term Memory)
  - Transformer (Multi-Head Attention)
  - Random Forest
  - Gradient Boosting Machine (GBM)
  - XGBoost
  - LightGBM
  - SVM (Support Vector Machine)
- Technical analysis indicators (EMA, SMA, RSI, MACD, ATR)
- Advanced backtesting framework with performance metrics
- Web-based dashboard with Plotly charts
- REST API for predictions and performance metrics
- Real-time price updates

## Prerequisites
- Python 3.8+
- Binance API credentials
- TA-Lib C library installation ([install guide](https://github.com/TA-Lib/ta-lib-python#dependencies))

### Installing TA-Lib

**Windows:**
Download the prebuilt binary from [here](https://github.com/cgohlke/talib-build/releases) and install via pip.

**macOS:**
```bash
brew install ta-lib
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install -y build-essential wget
wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz
tar -xzf ta-lib-0.4.0-src.tar.gz
cd ta-lib/ && ./configure --prefix=/usr && make && sudo make install
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ram-cs7/Cryptocurrency-Price-Prediction-System.git
cd Cryptocurrency-Price-Prediction-System
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create `.env` file with your Binance API credentials:
```
BINANCE_API_KEY=your_api_key
BINANCE_SECRET=your_api_secret
```

## Usage

1. Run the application:
```bash
python main.py
```

2. Access the web interface:
   - Main dashboard: http://localhost:5000
   - Dash analytics: http://localhost:5000/dash/

3. API Endpoints:
   - `GET /api/v1/predictions?symbol=BTC/USDT` — latest price prediction
   - `GET /api/v1/performance` — backtest performance metrics

## Model Details

### LSTM (Long Short-Term Memory)
- Deep learning recurrent neural network
- Features:
  - 2 LSTM layers with 50 units each
  - Dropout rate of 0.2 for regularization
  - Adam optimizer with MSE loss

### Transformer
- Attention-based deep learning model
- Features:
  - Multi-Head Attention with 8 heads
  - Layer normalization
  - Global average pooling

### Random Forest
- Ensemble learning method
- Features:
  - 100 estimators
  - Max depth of 10
  - Parallel processing enabled

### Gradient Boosting Machine (GBM)
- Boosting algorithm
- Features:
  - 100 estimators
  - Learning rate of 0.1
  - Max depth of 5

### XGBoost
- Advanced implementation of gradient boosting
- Features:
  - Early stopping support
  - Subsample ratio of 0.8
  - Column sampling of 0.8

### LightGBM
- Light Gradient Boosting Machine
- Features:
  - Leaf-wise growth strategy
  - 31 leaves per tree
  - Parallel processing enabled

### SVM (Support Vector Machine)
- Support Vector Regression with RBF kernel
- Features:
  - RBF kernel with gamma='scale'
  - C=1.0 regularization
  - Epsilon-insensitive loss (epsilon=0.1)

## Project Structure
```
Cryptocurrency-Price-Prediction-System/
├── config/
│   ├── __init__.py
│   └── config.py              # Configuration & hyperparameters
├── data/
│   ├── __init__.py
│   ├── data_collector.py      # Binance data fetching via CCXT
│   └── technical_indicators.py # TA-Lib indicator calculations
├── models/
│   ├── __init__.py
│   ├── base_model.py          # Abstract base class
│   ├── lstm_model.py          # LSTM implementation
│   ├── transformer_model.py   # Transformer implementation
│   ├── random_forest_model.py # Random Forest implementation
│   ├── gbm_model.py           # GBM implementation
│   ├── xgboost_model.py       # XGBoost implementation
│   ├── lightgbm_model.py      # LightGBM implementation
│   ├── svm_model.py           # SVM implementation
│   └── model_factory.py       # Factory for model creation
├── backtesting/
│   ├── __init__.py
│   └── advanced_backtester.py # Backtesting engine
├── web/
│   ├── __init__.py
│   ├── app.py                 # Flask + Dash web server
│   ├── templates/
│   │   └── index.html         # Dashboard HTML
│   └── static/
│       ├── css/style.css      # Dashboard styles
│       └── js/dashboard.js    # Frontend logic
├── utils/
│   ├── __init__.py
│   ├── data_preprocessing.py  # MinMaxScaler preprocessing
│   └── performance_metrics.py # RMSE, Sharpe, drawdown metrics
├── main.py                    # Application entry point
├── requirements.txt           # Python dependencies
├── API_Documentation.md       # REST & WebSocket API docs
└── README.md
```

## Configuration
- Adjust model parameters in `config/config.py`
- Modify technical indicators in `data/technical_indicators.py`
- Configure backtesting parameters in `backtesting/advanced_backtester.py`

## Testing
Run tests:
```bash
python -m pytest tests/
```

## Contributing
1. Fork the repository
2. Create your feature branch: `git checkout -b feature/new-feature`
3. Commit your changes: `git commit -am 'Add new feature'`
4. Push to the branch: `git push origin feature/new-feature`
5. Submit a pull request

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- Binance API for cryptocurrency data
- CCXT library for exchange integration
- TA-Lib for technical analysis indicators
- TensorFlow, scikit-learn, XGBoost, LightGBM contributors

## Disclaimer
This software is for educational purposes only. Do not use it for trading without proper validation and risk management.