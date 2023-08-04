import requests
import telebot

BASE_URL = "https://love-calculator.p.rapidapi.com"
RAPIDAPI_KEY = "b5f715ba64msha7ad36c828d9b16p14c38fjsnf07017e60f2a"  # Replace this with your RapidAPI key
BOT_TOKEN = "5868706821:AAFG_JUGNaB9RsEDvOet22EQsLotaKDrM-U"        # Replace this with your Telegram Bot token

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['LOVE_CALCULATE'])
def love_calculate(message):
    your_name, _, partner_name = message.text.partition(' ')
    if not partner_name:
        bot.send_message(message.chat.id, "Please provide two names separated by a space after the command.")
        return

    headers = {
        "X-RapidAPI-Host": "love-calculator.p.rapidapi.com",
        "X-RapidAPI-Key": b5f715ba64msha7ad36c828d9b16p14c38fjsnf07017e60f2a
    }

    response = requests.get(f"{BASE_URL}/getPercentage?yourName={your_name}&partnerName={partner_name}", headers=headers)

    if response.status_code == 200:
        data = response.json()
        percentage = data["percentage"]
        result = data["result"]
        bot.send_message(message.chat.id, f"Your love percentage with {partner_name} is {percentage}%. {result}")
    else:
        bot.send_message(message.chat.id, "Something went wrong. Please try again later.")

bot.polling()
