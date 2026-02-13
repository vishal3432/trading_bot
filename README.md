# Binance Futures Testnet Trading Bot

## Setup
```
pip install -r requirements.txt
```

Create .env file
```
API_KEY=your_key
API_SECRET=your_secret
```

## Run

Market Order
```
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

Limit Order
```
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 60000
```

## Features
- Market + Limit orders
- Logging
- Validation
- Structured architecture
- Error handling

Log file → bot.log