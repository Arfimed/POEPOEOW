HELP = """"
help - Напечатать справку по программе
add - добавить задачу в список
show - показать все задачи
del - удалить задачу из списка
random - сгенерировать случайную задачу
exit - завершить работу
"""""

RANDOM_TASK = ['Помыть полы','помытся','помыть посду', 'cделать уроки', 'сделать машину времени', 'не уснуть на физике'
'одется(по желанию)', 'побегать(от бомжей)','спрыгнуть с круши и выжить(выживать не обязательно)']

tasks = {}

print(HELP)
while True:
    command = input("\nВВедите каманду:")
    if command == "help":
        print(HELP)
    elif command == 'add':
        task = input("\nВВедите задачу:")
        date = input("Когда нужно выполнить задачу?")
        if date in tasks:
            tasks[date].append(task)
        else:
            tasks[date] = []
            tasks[date].append(task)
        print('Задача - {task} успешно добавлено на дату - {date}')
    elif command == 'show':
        date = input("Введите дату для отображения задач")
        if date in tasks[date]:
            for task in tasks[date]:
                print('-', task)
        else:
            print('На эту дату нет событий')
    elif command == 'del':
        task = input('\nВВедите задачу lдля удаления')
        if task in tasks[date]:
            tasks[date].remove(task)
            print('Задача удалена')
            break
        else:
            print('Задача не найдена')
    elif command == 'exit':
        print('Спасибо за использование!')
        break
    elif command == 'random':
        if 'Сегодня'.append(RANDOM_TASK)
        else:
            tasks['Сегодня'] = []
            tasks['Сегодня'].append(RANDOM_TASK)
    else:
        print('Неизвестная команда', HELP)

print('До свидания!')


