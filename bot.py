import os
import requests
from flask import Flask, request

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
WEBHOOK_URL = os.environ.get("WEBHOOK_URL")

OWNER_ID = 7009251207
CHANNEL_ID = "@pcbschub"


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
    raw_text = message.get("text", "")
    text = raw_text.lower().strip()

    # 🔐 OWNER-ONLY POST COMMAND
    if text.startswith("/post"):
        if chat_id != OWNER_ID:
            send_message(
                chat_id,
                "🔒 This command is available only to the PCBCsHub admin."
            )
            return "OK"

        content = raw_text[5:].strip()

        if not content:
            send_message(
                chat_id,
                "📢 Send your post like this:\n\n"
                "/post\n"
                "📚 Today's Study Target\n\n"
                "🧪 Chemistry: Thermodynamics revision\n"
                "⚡ Physics: Motion in a Straight Line\n"
                "🧬 Biology: Cell Cycle revision"
            )
            return "OK"

        send_message(CHANNEL_ID, content)

        send_message(
            chat_id,
            "✅ Posted successfully to PCBCsHub! 📢💙"
        )
        return "OK"

    # START
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

    # HELP
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

    # NOTES
    elif text == "/notes":
        send_message(
            chat_id,
            """📝 PCBCsHub Handwritten Notes

https://t.me/handwrittennotespcbcshub"""
        )

    # NCERT
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

    # MCQ
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

    # PYQ
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

    # REVISION
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

    # NEET
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

    # CUET
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

    # CBSE
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

    # STUDY PLAN
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

Learn • Practice • Revise • Improve."""
        )

    # MOTIVATION
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

    # LINKS
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
