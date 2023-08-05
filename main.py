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

bot = telebot.TeleBot('5868706821:AAFG_JUGNaB9RsEDvOet22EQsLotaKDrM-U')

@bot.on('message')
def handle_message(message):
  if message.chat.type == 'group' and message.chat.title == 'Work Group':
    if message.text == '/start':
      bot.send_message(message.chat.id, 'Welcome to the Love Calculator!')
    elif message.text == 'your name':
      bot.send_message(message.chat.id, 'Enter your name:')
    elif message.text == 'partner\'s name':
      your_name = message.chat.first_name
      partner_name = message.text
      love_percentage = calculate_love_percentage(your_name, partner_name)
      bot.send_message(message.chat.id, f'Your love percentage is {love_percentage}%')
    elif message.text == '/love':
      your_name = message.text.split(' ')[1]
      partner_name = message.text.split(' ')[2]
      love_percentage = calculate_love_percentage(your_name, partner_name)
      bot.send_message(message.chat.id, f'Your love percentage is {love_percentage}%')
      bot.send_message(message.chat.id, f'❤️❤️❤️')
  else:
    bot.send_message(message.chat.id, 'This bot is only available to work groups.')

bot.polling()
