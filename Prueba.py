from flask import Flask, request
import requests

TOKEN = "7933621950:AAEMx0oUWK27zx9NDrYyvRGHhimemAh5pic"
CHAT_ID = "6873763875"
TELEGRAM_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

app = Flask(__name__)

@app.route('/alert', methods=['POST'])
def alert():
    data = request.get_json(force=True)

    symbol = data.get("symbol", "NA")
    price  = data.get("price", "NA")
    time   = data.get("time", "NA")

    message = f"📈 Alerta desde TradingView\n\nSímbolo: {symbol}\nPrecio: {price}\nHora: {time}"

    requests.post(TELEGRAM_URL, data={
        "chat_id": CHAT_ID,
        "text": message
    })
    
    return "OK", 200

app.run(host="0.0.0.0", port=80)
