# main.py
from config.config import Config
from data.data_collector import DataCollector
from data.technical_indicators import TechnicalIndicators
from models.model_factory import ModelFactory
from backtesting.advanced_backtester import AdvancedBacktester
from web.app import WebInterface, app

def main():
    # Initialize configuration
    config = Config()
    
    # Set up data collection
    data_collector = DataCollector(config)
    df = data_collector.fetch_historical_data('BTC/USDT')
    
    if df is not None:
        # Add technical indicators and preprocess
        df = TechnicalIndicators.add_all_indicators(df)
        
        # Create and train model
        model = ModelFactory.create_model('lstm', config)
        X, y = model.prepare_sequences(df[config.FEATURE_COLUMNS].values)
        
        # Split data and train
        split_idx = int(len(X) * config.TRAIN_SPLIT)
        model.train(X[:split_idx], y[:split_idx])
        
        # Run backtesting
        backtester = AdvancedBacktester(model, df, config)
        results = backtester.run_backtest()
        
        # Start web interface
        web_interface = WebInterface(backtester, df)
        app.run(debug=True)

if __name__ == "__main__":
    main()