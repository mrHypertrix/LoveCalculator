# Your main script

import telebot
import config

def calculate_love_percentage(your_name, partner_name):
    """Calculates the love percentage between two names.

    Args:
        your_name: The name of the first person.
        partner_name: The name of the second person.

    Returns:
        The love percentage between the two names.
    """
    your_name_score = sum(ord(letter) - ord('A') + 1 for letter in your_name.upper())
    partner_name_score = sum(ord(letter) - ord('A') + 1 for letter in partner_name.upper())
    love_percentage = (your_name_score * partner_name_score) % 100
    return love_percentage

bot = telebot.TeleBot(config.bot_token)

@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, 'Welcome to the Love Calculator!')

@bot.message_handler(commands=["love"])
def love_message(message):
    names = message.text.split(' ')[1:]
    if len(names) >= 2:
        your_name = names[0]
        partner_name = names[1]
        love_percentage = calculate_love_percentage(your_name, partner_name)
        bot.send_message(message.chat.id, f'Your love percentage is {love_percentage}%')
        bot.send_message(message.chat.id, '❤️❤️❤️')
    else:
        bot.send_message(message.chat.id, 'Please provide two names for the love calculation.')

bot.polling()
