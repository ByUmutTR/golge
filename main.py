import os
from flask import Flask, request
import telebot

TOKEN = "BURAYA_BOT_TOKENINI_YAZ"
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)


@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
  json_string = request.get_data().decode("utf-8")
  update = telebot.types.Update.de_json(json_string)
  bot.process_new_updates([update])
  return "!", 200


@app.route("/")
def index():
  return "Gölge Timi Bot Aktif!", 200


if __name__ == "__main__":
  # Render'ın verdiği dinamik portu yakalar
  port = int(os.environ.get("PORT", 5000))

  # Webhook'u Telegram'a tanımla (Render URL'ini buraya yazacaksın)
  # bot.remove_webhook()
  # bot.set_webhook(url=f"https://senin-proje-adin.onrender.com/{TOKEN}")

  app.run(host="0.0.0.0", port=port)
