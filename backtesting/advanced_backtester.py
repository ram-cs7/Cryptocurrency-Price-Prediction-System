# backtesting/advanced_backtester.py
class AdvancedBacktester:
    def __init__(self, model, data, config):
        self.model = model
        self.data = data
        self.config = config
        self.results = {}
    
    def run_backtest(self, initial_capital=10000, transaction_fee=0.001):
        df = self.data.copy()
        X, y = self.model.prepare_sequences(df.values)
        predictions = self.model.predict(X)
        
        # Trading simulation
        portfolio_value = initial_capital
        portfolio_history = []
        trades = []
        position = 0
        
        for i in range(len(predictions) - 1):
            signal = np.sign(predictions[i + 1] - predictions[i])
            
            if signal != position:
                if position != 0:
                    pnl = position * (df['close'].iloc[i] - entry_price)
                    portfolio_value += pnl
                    portfolio_value *= (1 - transaction_fee)
                    trades.append({
                        'entry_date': entry_date,
                        'exit_date': df.index[i],
                        'position': position,
                        'pnl': pnl
                    })
                
                if signal != 0:
                    position = signal
                    entry_price = df['close'].iloc[i]
                    entry_date = df.index[i]
            
            portfolio_history.append(portfolio_value)
        
        return self._calculate_metrics(portfolio_history, trades, predictions, y)