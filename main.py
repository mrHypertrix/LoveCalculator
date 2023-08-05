import telebot

def calculate_love_percentage(your_name, partner_name):
  """Calculates the love percentage between two names.

  Args:
    your_name: The name of the first person.
    partner_name: The name of the second person.

  Returns:
    The love percentage between the two names.
  """

  your_name_score = sum(ord(letter) - ord('A') + 1 for letter in your_name)
  partner_name_score = sum(ord(letter) - ord('A') + 1 for letter in partner_name)
  love_percentage = (your_name_score * partner_name_score) % 100
  return love_percentage

bot = telebot.TeleBot('YOUR_BOT_TOKEN')

@bot.message_handler(commands=["start"])
def start(message):
  bot.send_message(message.chat.id, 'Welcome to the Love Calculator!')

@bot.message_handler(commands=["love"])
def love(message):
  your_name = message.text.split(' ')[1]
  partner_name = message.text.split(' ')[2]
  love_percentage = calculate_love_percentage(your_name, partner_name)
  bot.send_message(message.chat.id, f'Your love percentage is {love_percentage}%')
  bot.send_message(message.chat.id, f'❤️❤️❤️')

bot.polling()
