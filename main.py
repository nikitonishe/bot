import telebot
import config
import Shelve

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=["start","help"])
def start(message):
    bot.send_message(message.chat.id,"Основные команды: \n /start - Начальное меню \n /play - Начать игру")

@bot.message_handler(commands=["play"])
def game(message):
    question, markup = Shelve.get_question(message.chat.id)
    bot.send_message(message.chat.id, question, reply_markup = markup)

@bot.message_handler(content_types=["text"])
def check_answer(message):
    answer = Shelve.get_right_answer(message.chat.id)
    if not answer:
        bot.send_message(message.chat.id,"Чтобы начать игру введите команду '/play'")
    else:
        keyboard_hider = telebot.types.ReplyKeyboardHide()
        if message.text == answer:
            bot.send_message(message.chat.id, "Верно" , reply_markup = keyboard_hider)
        else:
            bot.send_message(message.chat.id, "Неверно. Правильный ответ - %s" % answer , reply_markup = keyboard_hider)
        Shelve.stop_game(message.chat.id)

bot.polling(none_stop = True, interval = 0)


