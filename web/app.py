# web/app.py
from flask import Flask, render_template, jsonify, request
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import json
import numpy as np

app = Flask(__name__)
dash_app = Dash(__name__, server=app, url_base_pathname='/dash/')


class WebInterface:
    def __init__(self, backtester, data):
        self.backtester = backtester
        self.data = data
        self.setup_routes()
        self.setup_dash_layout()
    
    def setup_routes(self):
        @app.route('/')
        def index():
            return render_template('index.html')
        
        @app.route('/api/v1/predictions')
        def get_predictions():
            """Get latest price predictions for specified cryptocurrency."""
            symbol = request.args.get('symbol', 'BTC/USDT')
            timeframe = request.args.get('timeframe', '1h')
            
            try:
                current_price = float(self.data['close'].iloc[-1])
                # Use the model to predict next price
                X, _ = self.backtester.model.prepare_sequences(
                    self.data[self.backtester.config.FEATURE_COLUMNS].values
                )
                predictions = self.backtester.model.predict(X)
                predicted_price = float(predictions[-1])
                direction = 'up' if predicted_price > current_price else 'down'
                confidence = self._calculate_prediction_confidence(predictions)
                
                return jsonify({
                    'timestamp': str(self.data.index[-1]),
                    'symbol': symbol,
                    'current_price': current_price,
                    'predicted_price': predicted_price,
                    'prediction_probability': confidence,
                    'direction': direction
                })
            except Exception as e:
                return jsonify({'error': str(e)}), 500
        
        @app.route('/api/v1/performance')
        def get_performance():
            """Get historical performance metrics."""
            try:
                results = self.backtester.results
                return jsonify({
                    'accuracy': results.get('win_rate', 0),
                    'profit_loss': results.get('total_return', 0) * 100,
                    'sharpe_ratio': results.get('sharpe_ratio', 0),
                    'max_drawdown': results.get('max_drawdown', 0),
                    'total_trades': results.get('total_trades', 0)
                })
            except Exception as e:
                return jsonify({'error': str(e)}), 500
    
    def _calculate_prediction_confidence(self, predictions):
        """Calculate prediction confidence based on recent prediction stability."""
        if len(predictions) < 5:
            return 0.5
        recent = predictions[-5:]
        std = float(np.std(recent))
        mean = float(np.mean(np.abs(recent)))
        # Lower relative volatility = higher confidence
        if mean == 0:
            return 0.5
        confidence = max(0.0, min(1.0, 1.0 - (std / mean)))
        return round(confidence, 4)
    
    def setup_dash_layout(self):
        dash_app.layout = html.Div([
            html.H1('Crypto Price Prediction Dashboard',
                     style={'textAlign': 'center', 'color': '#e0e0e0',
                            'fontFamily': 'Inter, sans-serif'}),
            dcc.Graph(id='price-chart'),
            dcc.Graph(id='portfolio-performance'),
            html.Div(id='metrics-display',
                     style={'padding': '20px', 'textAlign': 'center'}),
            dcc.Interval(id='interval-component', interval=60*1000)
        ], style={'backgroundColor': '#1a1a2e', 'minHeight': '100vh',
                  'padding': '20px'})