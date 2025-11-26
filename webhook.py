import os
from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = os.getenv("7933621950:AAEMx0oUWK27zx9NDrYyvRGHhimemAh5pic")
CHAT_ID =  os.getenv("6873763875")



@app.post("/alert")
def alert():
    data = request.json

    # Mensaje simple (puede ser dinámico según lo que envíe TradingView)
    message = f"🚨 Alerta recibida:\n\n{data}"

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    # Enviar a Telegram
    r = requests.post(url, json=payload)

    return jsonify({"status": "ok", "telegram_status": r.status_code})
