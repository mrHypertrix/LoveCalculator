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
    bot.send_message(message.chat.id, 'Welcome to the Love Calculator!\n\nTo calculate love percentage, use the /love command.\nExample: /love nameA nameB\n\n[ᴢᴏɴᴇʏ](https://t.me/itszoney) ❤️', parse_mode='Markdown')

@bot.message_handler(commands=["love"])
def love_message(message):
    names = message.text.split(' ')[1:]
    if len(names) >= 2:
        your_name = names[0]
        partner_name = names[1]

        if your_name.lower() in ['zoney', 'zony'] or partner_name.lower() in ['zoney', 'zony']:
            bot.send_message(message.chat.id, 'Pyar ek dhokha hai, zoney nahi padhta usme 😜', reply_to_message_id=message.message_id)
        else:
            if (your_name.lower() == 'shivani' and partner_name.lower() == 'gautam') or (your_name.lower() == 'gautam' and partner_name.lower() == 'shivani') or (your_name.lower() == 'panda' and partner_name.lower() == 'shivani'):
                love_percentage = 100
            else:
                love_percentage = calculate_love_percentage(your_name, partner_name)

            reply_text = f"{your_name} and {partner_name} love percentage is {love_percentage}% ❤️❤️❤️"
            bot.send_message(message.chat.id, reply_text, reply_to_message_id=message.message_id)
    else:
        bot.send_message(message.chat.id, 'Please provide two names for the love calculation.', reply_to_message_id=message.message_id)

bot.polling()
