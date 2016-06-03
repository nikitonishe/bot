import telebot
import shelve
import SQLiter
import config
import random

def get_question(chat_id):

    db_worker = SQLiter.SQLiter(config.data_base_name)
    row = db_worker.get_info_by_id(config.table_name, random.randint(1, db_worker.get_quantity_of_rows(config.table_name)))[0]
    db_worker.close();

    with shelve.open("shelve/"+config.shelve_name) as storage:
        storage[str(chat_id)] = row[2]

    answers = list(row[3].split("/"))
    answers.append(row[2])
    random.shuffle(answers)
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    for i in answers:
        markup.add(i)

    question = row[1]

    return question, markup

def get_right_answer(chat_id):
    with shelve.open("shelve/"+config.shelve_name) as storage:
        try:
            answer = storage[str(chat_id)]
            return answer
        except KeyError:
            return None

def stop_game(chat_id):
    with shelve.open("shelve/"+config.shelve_name) as storage:
        del storage[str(chat_id)]

