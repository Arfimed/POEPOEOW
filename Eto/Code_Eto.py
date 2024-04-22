HELP = """"
help - Напечатать справку по программе
add - добавить задачу в список
show - показать все задачи
del - удалить задачу из списка
exit - завершить работу
"""""

tasks = []

print(HELP)
while True:
    command = input("\nВВедите каманду:")
    if command == "help":
        print(HELP)
    elif command == 'add':
        task = input("\nВВедите задачу:")
        tasks.append(task)
        print('Задача добавлена')
    elif command == 'show':
        print(tasks)
    elif command == 'del':
        task = input('\nВВедите задачу lдля удаления')
        if task in tasks:
            tasks.remove(task)
            print('Задача удалена')
        else:
            print('Задача не найдена')
    elif command == 'exit':
        print('Спасибо за использование!')
        break
    else:
        print('Неизвестная команда', HELP)

print('До свидания!')


