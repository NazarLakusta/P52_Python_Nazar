# 8544687765:AAHxCF7BBUVvgibF5UGNhrTTHFB0l0wwkJ8

import telebot

# встав сюди свій токен
TOKEN = "8544687765:AAHxCF7BBUVvgibF5UGNhrTTHFB0l0wwkJ8"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def reply_to_message(message):
    if message.text.lower() == "чернівці":
        bot.reply_to(message, "ІтСтеп")
    else:
        bot.reply_to(message, "Напиши 'Чернівці' 😉")

bot.polling()
