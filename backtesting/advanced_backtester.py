# backtesting/advanced_backtester.py
import numpy as np
from utils.performance_metrics import PerformanceMetrics

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
        portfolio_history = [initial_capital]
        trades = []
        position = 0
        entry_price = 0.0
        entry_date = None
        
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
                else:
                    position = 0
            
            portfolio_history.append(portfolio_value)
        
        self.results = self._calculate_metrics(portfolio_history, trades, predictions, y)
        return self.results
    
    def _calculate_metrics(self, portfolio_history, trades, predictions, actual):
        """Calculate comprehensive backtest performance metrics."""
        portfolio_arr = np.array(portfolio_history)
        
        # Calculate returns
        returns = np.diff(portfolio_arr) / portfolio_arr[:-1]
        
        # Prediction accuracy metrics
        rmse = np.sqrt(np.mean((predictions.flatten() - actual.flatten()) ** 2))
        mae = np.mean(np.abs(predictions.flatten() - actual.flatten()))
        
        # Portfolio metrics
        total_return = (portfolio_arr[-1] - portfolio_arr[0]) / portfolio_arr[0]
        sharpe_ratio = (np.mean(returns) / np.std(returns) * np.sqrt(252)) if np.std(returns) > 0 else 0
        max_drawdown = PerformanceMetrics._calculate_max_drawdown(portfolio_history)
        
        # Trade statistics
        winning_trades = [t for t in trades if t['pnl'] > 0]
        losing_trades = [t for t in trades if t['pnl'] <= 0]
        win_rate = len(winning_trades) / len(trades) if trades else 0
        
        return {
            'total_return': total_return,
            'sharpe_ratio': sharpe_ratio,
            'max_drawdown': max_drawdown,
            'rmse': rmse,
            'mae': mae,
            'total_trades': len(trades),
            'winning_trades': len(winning_trades),
            'losing_trades': len(losing_trades),
            'win_rate': win_rate,
            'final_portfolio_value': portfolio_arr[-1],
            'portfolio_history': portfolio_history
        }