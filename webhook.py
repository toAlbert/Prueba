import os
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

TELEGRAM_TOKEN = os.getenv("8043571009:AAEpvETQ8IKjrH1ouGXPr0l3s6J4uBgHzRc")
CHAT_ID =  os.getenv("-6873763875")


@app.route("/alert", methods=["POST"])
def alert():
    data = request.json
    message_text = f"Alerta recibida: {data}"

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message_text}
    r = requests.post(url, json=payload)

    # Este return debe estar dentro de la función
    return jsonify({"status": "ok", "telegram_status": r.status_code, "telegram_response": r.text})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
