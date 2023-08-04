import telebot
import axios

BASE_URL = "https://love-calculator.p.rapidapi.com"

BOT_TOKEN = "5868706821:AAFG_JUGNaB9RsEDvOet22EQsLotaKDrM-U"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.on(telebot.message.Command("LOVE_CALCULATE"))
def love_calculate(message):
    your_name = message.text
    partner_name = "ashi"

    response = axios.get(
        f"{BASE_URL}/getPercentage?yourName={your_name}&partnerName={partner_name}"
    )

    if response.status_code == 200:
        data = response.json()
        percentage = data["percentage"]
        result = data["result"]

        bot.send_message(message.chat.id, f"Your love percentage is {percentage}%. {result}")
    else:
        bot.send_message(message.chat.id, "Something went wrong. Please try again later.")

bot.polling()
