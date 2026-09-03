import os
import requests
from flask import Flask, request

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
WEBHOOK_URL = os.environ.get("WEBHOOK_URL")


def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={
        "chat_id": chat_id,
        "text": text,
        "disable_web_page_preview": False
    })


@app.route("/", methods=["GET"])
def home():
    return "PCBCsHub Bot is running! 💙"


@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()

    if not data or "message" not in data:
        return "OK"

    message = data["message"]
    chat_id = message["chat"]["id"]
    text = message.get("text", "").lower().strip()

    if text == "/start":
        send_message(
            chat_id,
            """🎓 Welcome to PCBCsHub! 💙

Your study companion for NEET, CUET & CBSE 📚

📝 Handwritten Notes
📖 NCERT Resources
❓ MCQs & PYQs
⚡ Quick Revision

Use /help to see all commands.

🔥 Learn • Practice • Revise • Improve"""
        )

    elif text == "/help":
        send_message(
            chat_id,
            """📚 PCBCsHub Commands

/notes - Handwritten notes
/ncert - NCERT resources
/mcq - Practice MCQs
/pyq - Previous year questions
/revision - Quick revision
/neet - NEET resources
/cuet - CUET resources
/cbse - CBSE resources
/studyplan - Study plans
/motivation - Study motivation
/links - All PCBCsHub platforms"""
        )

    elif text == "/notes":
        send_message(
            chat_id,
            "📝 PCBCsHub Handwritten Notes:\nhttps://t.me/handwrittennotespcbcshub"
        )

    elif text == "/links":
        send_message(
            chat_id,
            """🌐 PCBCsHub Platforms

📱 WhatsApp:
https://whatsapp.com/channel/0029VbCkiwxC1FuKCjz9vH1F

💬 Telegram:
https://t.me/pcbschub

📝 Handwritten Notes:
https://t.me/handwrittennotespcbcshub

▶️ YouTube:
https://youtube.com/@pcbcshub"""
        )

    elif text == "/motivation":
        send_message(
            chat_id,
            "🔥 Keep going! Small progress every day becomes a big result. 💙\n\n— PCBCsHub"
        )

    else:
        send_message(
            chat_id,
            "🤔 I don't recognize that command.\n\nUse /help to see what I can do."
        )

    return "OK"


if __name__ == "__main__":
    if WEBHOOK_URL:
        requests.get(
            f"https://api.telegram.org/bot{BOT_TOKEN}/setWebhook",
            params={"url": WEBHOOK_URL + "/webhook"}
        )

    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
