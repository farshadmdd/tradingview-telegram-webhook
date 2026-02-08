# TradingView Webhook → Telegram Signal Bot

A simple Flask-based webhook server that receives alerts from TradingView and forwards them to Telegram channels or groups.

## 🚀 Features
- Receive TradingView alerts via webhook (POST request)
- Parse JSON payload from TradingView
- Format the signal message
- Send the message to one or multiple Telegram channels
- Lightweight and easy to deploy on any VPS

## 📦 Requirements
- Python 3.x
- Flask
- requests

Install dependencies:
```bash
pip install flask requests

Configuration:
Edit the following variables inside the script:
telegram_channels = ["YOUR_CHANNEL_ID"]
token = "YOUR_TELEGRAM_BOT_TOKEN"


TradingView Setup
In your TradingView alert message, send JSON in this format:
{
  "symbol": "BTCUSDT",
  "ordertype": "LONG",
  "Entry": "42000",
  "Leverage": "10",
  "leveragetype": "Cross",
  "Target1": "42500",
  "Target2": "43000",
  "Stop_Loss": "41000"
}


Set your webhook URL to:
https://your-server.com/webhook


Run the server
python app.py 


Telegram Output Example
BTCUSDT
LONG
ENTRY: 42000
Leverage: Cross 10
Target 1 - 42500
Target 2 - 43000
Stop Loss: 41000

Notes
You can add up to 8 targets.
Works with any TradingView alert.
You can deploy it on VPS, Render, Railway, or Heroku.