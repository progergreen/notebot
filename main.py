#The simplest bot for saving text notes to a computer via the telegram social network.

import telebot
bot = telebot.TeleBot("6047389802:AAGiZsSaFsxx-4xk5olDTHt470xE9KsKEH4")
@bot.message_handler()
def save_text(message):
    if message.text == '/start':
        bot.send_message(message.chat.id, 'Bot is ready!')
    elif message.text == '/delete':
        with open('C:/bot/text.txt', 'w') as file:
            file.write('')
    else:
        with open('C:/bottext/text.txt', 'a+') as file:
            file.write(message.text+'\n')
            bot.send_message(message.chat.id, 'Note saved!')
bot.polling(none_stop=True)
