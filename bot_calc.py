import telebot
from telebot import types
from config import TOKEN
import rational as rat
import complex_nums as cnums
import logger as lg

bot = telebot.TeleBot(TOKEN, skip_pending=True)

storage = {}

def init_storage(user_id):
    storage[user_id] = dict(first_number=None, second_number=None, operation=None)

def store_number(user_id, key, value):
    storage[user_id][key] = dict(value=value)

def get_number(user_id, key):
    return storage[user_id][key].get('value')

@bot.message_handler(func=lambda m: True)
def start(message):
    init_storage(message.from_user.id)
    bot.reply_to(message, "Выберите с какими числами будем работать. Введите Комплексные или Рациональные.")
    bot.register_next_step_handler(message, begin)

def begin(message):
    if message.text == "Рациональные":
        bot.reply_to(message,"Введите первое число(например 3/7)")
        bot.register_next_step_handler(message, first_rat_num)
    elif message.text == "Комплексные":
        bot.reply_to(message, "Введите первое число(например 3+7j)")
        bot.register_next_step_handler(message, first_comp_num)
    else:
        bot.reply_to(message, "Введите Комплексные или Рациональные")
        bot.register_next_step_handler(message, begin)

def first_rat_num(message):
        first_number = message.text

        store_number(message.from_user.id, "first_number", first_number)
        bot.reply_to(message, "Введите второе число(например 3/7)")
        bot.register_next_step_handler(message, second_rat_num)

def second_rat_num(message):
        second_number = message.text

        store_number(message.from_user.id, "second_number", second_number)
        bot.reply_to(message, "Выберите и введите желаемую операцию (+  -  *  /)")
        bot.register_next_step_handler(message, operation_rat)

def first_comp_num(message):
        first_number = message.text

        store_number(message.from_user.id, "first_number", first_number)
        bot.reply_to(message, "Введите второе число(например 5+8j)")
        bot.register_next_step_handler(message, second_comp_num)

def second_comp_num(message):
        second_number = message.text

        store_number(message.from_user.id, "second_number", second_number)
        bot.reply_to(message, "Выберите и введите желаемую операцию (+  -  *  /)")
        bot.register_next_step_handler(message, operation_comp)


def operation_rat(message):
        operation = message.text

        store_number(message.from_user.id, "operation", operation)

        num1 = get_number(message.from_user.id, "first_number")
        num2 = get_number(message.from_user.id, "second_number")
        oper = get_number(message.from_user.id, "operation")

        result = rat.fract(num1,num2,oper)
        bot.reply_to(message, f'Ответ:  {result}')

        lg.log_result(num1,oper,num2,result)

def operation_comp(message):
        operation = message.text

        store_number(message.from_user.id, "operation", operation)

        num1 = get_number(message.from_user.id, "first_number")
        num2 = get_number(message.from_user.id, "second_number")
        oper = get_number(message.from_user.id, "operation")

        result = cnums.complex_num(num1,num2,oper)
        bot.reply_to(message, f'Ответ:  {result}')

        lg.log_result(num1,oper,num2,result)

bot.polling(none_stop=True, interval=0)
