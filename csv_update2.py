import csv

def update_user():    

    fieldnames = ['id', 'last_name', 'first_name', 'second_name', 'number']
    user = {}
    for el in fieldnames:
        user[el] = input(f'Введите {el}: ')
        
    nfile = []
    with open('database.csv', 'r', encoding='utf-8') as csvfile:
    
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['id'] == user['id']:
                row['last_name'] = user['last_name']
                row['first_name'] = user['first_name']
                row['second_name'] = user['second_name']
                row['number'] = user['number']
            nfile.append(row)

    with open('database.csv', 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in nfile:
            writer.writerow(row)
    return nfile       