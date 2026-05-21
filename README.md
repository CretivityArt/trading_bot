# Binance Futures Testnet Trading Bot

A simple Python-based trading bot for Binance USDT-M Futures Testnet that supports MARKET, LIMIT, and STOP_MARKET orders using the `python-binance` library.

---

# Features

- Place MARKET orders
- Place LIMIT orders
- Place STOP_MARKET (Stop Loss) orders
- Supports BUY and SELL sides
- Command-line interface (CLI)
- Input validation
- Logging of API requests, responses, and errors
- Error handling for invalid inputs and API failures
- Structured and reusable codebase

---

# Project Structure

```text
trading_bot/
│
├── cli.py
├── requirements.txt
├── README.md
│
└── bot/
    ├── __init__.py
    ├── client.py
    ├── validators.py
    └── logger.py
```

---

# Requirements

- Python 3.9+
- Binance Futures Testnet account
- Binance Testnet API Key & Secret

---

# Installation

## 1. Clone the Repository

```bash
git clone <your-github-repo-url>
cd trading_bot
```

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Binance Futures Testnet Setup

1. Open Binance Futures Testnet:
   https://testnet.binancefuture.com

2. Create/Login to a Testnet account

3. Generate API credentials:
   - API Key
   - Secret Key

4. Add your keys inside `cli.py`

```python
API_KEY = "YOUR_API_KEY"
API_SECRET = "YOUR_API_SECRET"
```

---

# Usage

## MARKET Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.001
```

---

## LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --qty 0.001 --price 50000
```

---

## STOP_MARKET Order (Stop Loss)

```bash
python cli.py --symbol BTCUSDT --side SELL --type STOP_MARKET --qty 0.001 --price 98000
```

---

# Parameters

| Parameter | Description | Example |
|---|---|---|
| symbol | Trading pair | BTCUSDT |
| side | BUY or SELL | BUY |
| type | MARKET / LIMIT / STOP_MARKET | LIMIT |
| qty | Order quantity | 0.001 |
| price | Required for LIMIT and STOP_MARKET | 50000 |

---

# Logging

All API requests, responses, and errors are logged in:

```text
bot.log
```

Example logged information:
- Order request details
- Binance API response
- Validation errors
- Network/API exceptions

---

# Validation & Error Handling

The application validates:
- Supported order types
- Valid BUY/SELL side
- Positive quantity
- Positive price
- USDT-M trading pairs only

The bot also handles:
- API failures
- Invalid credentials
- Network issues
- Incorrect CLI arguments

---

# Assumptions

- Only Binance Futures Testnet is used
- Only USDT-M futures pairs are supported
- No leverage configuration included
- Only basic order placement functionality implemented

---

# Technologies Used

- Python 3
- python-binance
- argparse
- logging

---

# Future Improvements

Possible enhancements:
- Take Profit orders
- OCO orders
- WebSocket live price feed
- Strategy-based automation
- GUI dashboard
- Position monitoring

---

# Author

Ongshu Roy Chowdhury
