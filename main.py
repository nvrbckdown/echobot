import telebot

TOKEN = "BotFatherdan olingan bot tokeni!"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start_command_handler(message):
    bot.send_message(message.chat.id, "Salom, men ask-sado botiman!")


@bot.message_handler(content_types=["text"])
def echo_message_handler(message):
    chat_id = message.chat.id
    text = message.text
    bot.send_message(chat_id, text)


bot.polling()

