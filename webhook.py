from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

TELEGRAM_TOKEN = os.getenv("7933621950:AAEMx0oUWK27zx9NDrYyvRGHhimemAh5pic")
CHAT_ID =  os.getenv("6873763875")


@app.route("/", methods=["GET"])
def home():
    return "Webhook funcionando"

@app.route("/alert", methods=["POST"])
def alert():
    data = request.json

    message = f"Alerta recibida:\n{data}"

    r = requests.post(
        f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
        json={
            "chat_id": CHAT_ID,
            "text": message
        }
    )

    return jsonify({
        "status": "ok",
        "telegram_status": r.status_code
    })
