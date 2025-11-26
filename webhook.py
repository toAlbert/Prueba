import os
from flask import Flask, request, jsonify
import requests

app = Flask(name)

TELEGRAM_TOKEN = os.getenv("8043571009:AAEpvETQ8IKjrH1ouGXPr0l3s6J4uBgHzRc")
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
    "telegram_status": r.status_code,
    "telegram_response": r.text
})
