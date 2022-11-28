import csv

def delete_user():

    fieldnames = ['id', 'last_name', 'first_name', 'second_name', 'number']

    userId = input(f'Введите ID удаляемого пользователя: ')

    nfile = []
    with open('database.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['id'] != userId:
                nfile.append(row)

    with open('database.csv', 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in nfile:
            writer.writerow(row)
        