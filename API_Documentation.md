# API Documentation

## REST API Endpoints

### Price Predictions
```
GET /api/v1/predictions
```
Get latest price predictions for specified cryptocurrency.

Parameters:
- symbol (required): Trading pair (e.g., 'BTC/USDT')
- timeframe (optional): Prediction timeframe (default: '1h')

Response:
```json
{
    "timestamp": "2024-01-08T12:00:00Z",
    "symbol": "BTC/USDT",
    "current_price": 45000.00,
    "predicted_price": 45500.00,
    "prediction_probability": 0.75,
    "direction": "up"
}
```

### Historical Performance
```
GET /api/v1/performance
```
Get historical performance metrics.

Parameters:
- start_date (optional): Start date for analysis
- end_date (optional): End date for analysis

Response:
```json
{
    "accuracy": 0.68,
    "profit_loss": 15.5,
    "sharpe_ratio": 1.2,
    "max_drawdown": 0.12,
    "total_trades": 150
}
```

## WebSocket API

### Real-time Updates
```
WSS /ws/price-updates
```
Subscribe to real-time price and prediction updates.

Message Format:
```json
{
    "type": "prediction_update",
    "data": {
        "timestamp": "2024-01-08T12:00:00Z",
        "current_price": 45000.00,
        "predicted_price": 45500.00,
        "confidence": 0.75
    }
}
```

## Environment Variables

Required environment variables:
```
BINANCE_API_KEY=your_api_key
BINANCE_SECRET=your_api_secret
MODEL_PATH=path/to/model
DEBUG=True/False
LOG_LEVEL=INFO
```