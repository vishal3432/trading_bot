# Binance Futures Testnet Trading Bot

## Setup
```
pip install -r requirements.txt
```

Create .env file
```
API_KEY
API_SECRET
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

## This is how you can make a trading bot 
