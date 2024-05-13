import telebot
import random

token = '7165230836:AAHkvYWlYPfGwI2LpDu09gxkCcgDu6Do6yo'
bot = telebot.TeleBot(token)
tasks = {}
def add_todo(date, task):
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = []
        tasks[date].append(task)

HELP = """
/help - напечатать справку по программме
/add - добавить задачу в список
/del - удалить задачу из списка
/show - показатб все задачи
/random - сгенерировать случайную задачу сегодня
"""

RANDOM_TASK = ['Помыть полы','помытся','помыть посду', 'cделать уроки', 'сделать машину времени', 'не уснуть на физике'
'одется(по желанию)', 'побегать(от бомжей)','спрыгнуть с круши и выжить(выживать не обязательно)']

@bot.message_handler(commands=['add'])
def add(message):
    command = message.spliit(maxsplit = 2)
    date = command[1].lower()
    task = command[2]
    add_todo(date, task)
    text = f'Задача "{task}" добавлена на дату {date}'
    bot.send_message(message.chat.id, text)

    print(task, date)
    print(message.text)
    bot.send_message(message.chat.id, 'Команда принята')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,HELP)

@bot.message_handler(commands=['del'])
def delete_task(message):
    command = message.text.split(maxsplit = 1)
    task = command[1]
    for date in tasks:
        if task in tasks[date]:
            tasks[date].remove(task)
            bot.reply_to(message, 'Задача удалена')
            break
        else:
            bot.reply_to(message, 'Задачи нет в списке')
    else:
        text = f'Задача "{task}" не найдена'
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['random'])
def random_add(message):
    date = 'сегодня'
    task = random.choice(RANDOM_TASK)
    add_todo(date, task)
    text = f'Задача "{task}" добавлена на дату {date}'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['show'])
def show(message):
    command = message.text.split(maxsplit=1)
    date = command[1].lower()
    text = ''
    if date in tasks:
        text = date.upper() + '\n'
        for task in tasks[date]:
            text = text + '[]' + task + "\n"
    else:
        text = 'на эту дату дел нет'
    bot.send_message(message.chat.id, text)

bot.polling(non_stop=True)
