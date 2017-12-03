import config
from config import *
import telebot
from fInToOut import *
from fcalculate import func
from telebot import types

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def buttons(message):
    f = open('music/qweewq.ogg', 'rb')
    msg = bot.send_voice(message.chat.id, f, None)
    markup = types.ReplyKeyboardMarkup()
    markup.row('Примеры')
    markup.row('Построй график')
    markup.row('smh')
    bot.send_message(message.chat.id, 'Выбирай:', reply_markup=markup)


@bot.message_handler(regexp="Примеры")
def roflanHmm(message):
    msg = bot.send_message(message.chat.id, str(helpme), None)

@bot.message_handler(regexp="Построй график")
def roflanPomoyka(message):
    msg = bot.send_message(message.chat.id, 'Напишите функцию:', None)
    @bot.message_handler(content_types=["text"])
    def art(message):
        func(message.text)
        plot = open('plot.png', 'rb')
        msg = bot.send_photo(message.chat.id, plot, None)
        message.text = 0
'''
@bot.message_handler(content_types=["text"])
def art(message):
    func(message.text)
    plot = open('plot.png', 'rb')
    msg = bot.send_photo(message.chat.id, plot, None)
    message.text = 0
''' 
if __name__ == '__main__':
    bot.polling(none_stop=True)
