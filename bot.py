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
/cbse - CBSE preparation
/studyplan - Study plans
/motivation - Study motivation
/links - All PCBCsHub platforms"""
        )

    elif text == "/notes":
        send_message(
            chat_id,
            """📝 PCBCsHub Handwritten Notes

https://t.me/handwrittennotespcbcshub"""
        )

    elif text == "/ncert":
        send_message(
            chat_id,
            """📖 NCERT Resources

📚 NCERT is the foundation for NEET & CBSE preparation.

Use PCBCsHub for:
• NCERT-based revision
• Important concepts
• Chapter-wise resources
• Quick revision material

📝 Handwritten Notes:
https://t.me/handwrittennotespcbcshub

💬 Join PCBCsHub Telegram:
https://t.me/pcbschub"""
        )

    elif text == "/mcq":
        send_message(
            chat_id,
            """❓ MCQ Practice

Practice questions to test your preparation.

🎯 NEET
📚 CBSE
🧪 PCB subjects

More MCQ resources will be added soon.

💬 PCBCsHub Telegram:
https://t.me/pcbschub"""
        )

    elif text == "/pyq":
        send_message(
            chat_id,
            """📝 Previous Year Questions

Practice PYQs to understand:
• Important concepts
• Question patterns
• Frequently tested topics
• Exam-level difficulty

More PYQ resources will be added soon.

💬 PCBCsHub Telegram:
https://t.me/pcbschub"""
        )

    elif text == "/revision":
        send_message(
            chat_id,
            """⚡ Quick Revision

Revise smarter with PCBCsHub!

🧠 Short revision resources
📖 NCERT-based revision
📝 Handwritten notes
❓ Practice questions

📝 Notes:
https://t.me/handwrittennotespcbcshub

💬 Telegram:
https://t.me/pcbschub"""
        )

    elif text == "/neet":
        send_message(
            chat_id,
            """🩺 NEET Preparation

📚 NCERT Revision
❓ MCQs
📝 PYQs
⚡ Quick Revision
📖 Handwritten Notes

Your NEET preparation starts with consistent practice.

💬 PCBCsHub Telegram:
https://t.me/pcbschub

📝 Handwritten Notes:
https://t.me/handwrittennotespcbcshub"""
        )

    elif text == "/cuet":
        send_message(
            chat_id,
            """🎯 CUET Preparation

📚 NCERT-based preparation
❓ MCQs & PYQs
⚡ Quick Revision
📝 Study resources

Follow PCBCsHub for CUET resources and updates.

💬 Telegram:
https://t.me/pcbschub

▶️ YouTube:
https://youtube.com/@pcbcshub"""
        )

    elif text == "/cbse":
        send_message(
            chat_id,
            """📚 CBSE Preparation

Prepare smarter with:

📖 NCERT-based resources
📝 Notes
❓ MCQs
⚡ Quick Revision
🎯 Exam-focused practice

💬 PCBCsHub Telegram:
https://t.me/pcbschub

▶️ YouTube:
https://youtube.com/@pcbcshub"""
        )

    elif text == "/studyplan":
        send_message(
            chat_id,
            """🗓️ Study Plan

A simple study cycle:

1️⃣ Learn the concept
2️⃣ Make/revise notes
3️⃣ Read NCERT
4️⃣ Practice MCQs
5️⃣ Solve PYQs
6️⃣ Analyse mistakes
7️⃣ Revise again 🔁

🔥 Consistency > perfection

Use PCBCsHub resources to Learn • Practice • Revise • Improve."""
        )

    elif text == "/motivation":
        send_message(
            chat_id,
            """🔥 Study Motivation

You don't need to finish everything today.

Just complete today's target.
Then repeat tomorrow. 💙

📚 Learn
✍️ Practice
🔁 Revise
📈 Improve

— PCBCsHub"""
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

    else:
        send_message(
            chat_id,
            """🤔 I don't recognize that command.

Use /help to see what I can do."""
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
