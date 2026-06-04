# utils/performance_metrics.py
import numpy as np

class PerformanceMetrics:
    @staticmethod
    def calculate_metrics(predictions, actual, portfolio_history):
        return {
            'rmse': np.sqrt(np.mean((predictions - actual) ** 2)),
            'sharpe_ratio': np.sqrt(252) * np.mean(portfolio_history) / np.std(portfolio_history),
            'max_drawdown': PerformanceMetrics._calculate_max_drawdown(portfolio_history)
        }
    
    @staticmethod
    def _calculate_max_drawdown(portfolio_values):
        peak = portfolio_values[0]
        max_dd = 0
        for value in portfolio_values:
            if value > peak:
                peak = value
            dd = (peak - value) / peak
            max_dd = max(max_dd, dd)
        return max_dd
