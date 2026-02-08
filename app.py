from flask import Flask, request
import requests
import json

application = Flask(__name__)

@application.route("/")
def home():
    return "Your bot is alive"

# ------------------------------ Put your Telegram channel IDs here ------------------------------
telegram_channels = []

# ------------------------------ Put your Telegram API TOKEN here ---------------------------------
token = ""

@application.route("/webhook", methods=['POST', 'GET'])
def webhook():
    try:
        if request.method == "POST":
            data = json.loads(request.data.decode())
            print("TV Data:", data)

            symbol = data.get("symbol", "")
            ordertype = data.get("ordertype", "")
            Entry = data.get("Entry", "")
            Leverage = data.get("Leverage", "")
            leveragetype = data.get("leveragetype", "")   
            Stop_Loss = data.get("Stop_Loss", "")

            # Targets
            targets = []
            for i in range(1, 9):
                targets.append(data.get(f"Target{i}", ""))

            # The message sent from TradingView should be in this format
            msg = f"{symbol}\n{ordertype}\nENTRY: {Entry}\nLeverage: {leveragetype} {Leverage}\n"
            for i, t in enumerate(targets, start=1):
                msg += f"Target {i} - {t}\n"
            msg += f"Stop Loss: {Stop_Loss}"

            broadcast_msg(telegram_channels, msg)
            print("Signal message:", msg)

            return msg + "\nSignal sent"

        else:
            return "GET request received. Use POST to send signals."

    except Exception as e:
        print("Error:", e)
        return f"Error: {e}"

def broadcast_msg(channels, msg):
    for group_id in channels:
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        payload = {"chat_id": group_id, "text": msg, "parse_mode": "HTML"}
        resp = requests.post(url, data=payload)
        print(resp.text)

if __name__ == "__main__":
    application.run(debug=False)
