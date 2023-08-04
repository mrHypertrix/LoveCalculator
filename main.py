import telebot
import requests

BASE_URL = "https://love-calculator.p.rapidapi.com"

BOT_TOKEN = "5868706821:AAFG_JUGNaB9RsEDvOet22EQsLotaKDrM-U"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['love'])
def love_calculate(message):
    your_name = message.text.split()[1]  # Extract the name from the command
    partner_name = "ashi"

    response = requests.get(
        f"{BASE_URL}/getPercentage?yourName={your_name}&partnerName={partner_name}",
        headers={
            "x-rapidapi-host": "love-calculator.p.rapidapi.com",
            "x-rapidapi-key": "b5f715ba64msha7ad36c828d9b16p14c38fjsnf07017e60f2a"
        }
    )

    if response.status_code == 200:
        data = response.json()
        percentage = data["percentage"]
        result = data["result"]

        bot.send_message(message.chat.id, f"Your love percentage is {percentage}%. {result}")
    else:
        bot.send_message(message.chat.id, "Something went wrong. Please try again later.")

bot.polling()
