# Cryptocurrency Price Prediction System

## Overview
A comprehensive cryptocurrency price prediction system that uses multiple machine learning models and technical analysis to predict price movements. The system includes data collection, preprocessing, model training, backtesting, and a web interface for visualization.

## Features
- Multiple ML model implementations:
  - LSTM (Long Short-Term Memory)
  - Random Forest
  - Gradient Boosting Machine (GBM)
  - XGBoost
  - LightGBM
- Technical analysis indicators
- Advanced backtesting framework
- Web-based dashboard
- Real-time price updates
- Performance metrics and visualization

## Prerequisites
- Python 3.8+
- Binance API credentials
- TA-Lib installation

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/crypto-predictor.git
cd crypto-predictor
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

4. Create .env file:
```bash
touch .env
```

5. Add your Binance API credentials to .env:
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
- Main interface: http://localhost:5000
- Dashboard: http://localhost:5000/dash

## Model Details

### Random Forest Model
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

### XGBoost Model
- Advanced implementation of gradient boosting
- Features:
  - Early stopping
  - Subsample ratio of 0.8
  - Column sampling of 0.8

### LightGBM Model
- Light Gradient Boosting Machine
- Features:
  - Leaf-wise growth
  - 31 leaves per tree
  - Parallel processing enabled

## Project Structure
```
crypto_predictor/
├── config/          # Configuration settings
├── data/            # Data collection and preprocessing
├── models/          # ML model implementations
├── backtesting/     # Backtesting framework
├── web/             # Web interface
└── utils/           # Utility functions
```

## Configuration
- Adjust model parameters in config.py
- Modify technical indicators in technical_indicators.py
- Configure backtesting parameters in advanced_backtester.py

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
- Various ML libraries contributors

## Disclaimer
This software is for educational purposes only. Do not use it for trading without proper validation and risk management.