import csv
def get_action():
    mode = int(input('1 - Посмотр по id\n2 - Посмотр по фамилии\n3 - Добавление нового абонента\n4 - Удаление абонента\n5 - Перезапись абонента\n0 - Выйти\nВведите действие, которое хотите совершить: '))
    return mode

def get_user(type):
    if type == 1:
        reading = input('Введите ID: ')
    elif type == 2:
        reading = input('Введите Фамилию: ')
    with open('database.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if type == 1 and row['id'] == reading:
                print(row)
            elif type == 2 and row['last_name'] == reading:
                print(row)

def add_user():
    fieldnames = ['last_name', 'first_name', 'second_name', 'number']
    user = {}
    for el in fieldnames:
        user[el] = input(f'Введите {el}: ')
    return user 
 
