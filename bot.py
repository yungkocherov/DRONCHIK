import config
import telebot
import fcalculate
import fInToOut

from telebot import types

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def buttons(message):
    f = open('music/qweewq.ogg', 'rb')
    msg = bot.send_voice(message.chat.id, f, None)
    markup = types.ReplyKeyboardMarkup()
    markup.row('Примеры формул функций')
    markup.row('smth')
    markup.row('smh')
    bot.send_message(message.chat.id, 'Выбирай:', reply_markup=markup)


@bot.message_handler(regexp="Примеры формул функций")
def knopki(message):
    f = open('music/ulya.ogg', 'rb')
    msg = bot.send_voice(message.chat.id, f, None)


@bot.message_handler(regexp="smh")
def knopki(message):
    md = bot.send_message(message.chat.id, 'Это тебе <3', None)
    f = open('music/kartinki24_flowers_0017.jpg', 'rb')

    msg = bot.send_photo(message.chat.id, f, None)


# @bot.message_handler(commands=['start', 'help'])
# def handle_start_help(message):
#  pass


# @bot.message_handler(content_types=["text"])
# def povtoryator(message):
# bot.send_message(message.chat.id, message.text)
if __name__ == '__main__':
    bot.polling(none_stop=True)
