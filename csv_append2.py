import csv

def append_user(user):
 
    with open('database.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        max_id = 1
        for row in reader:
            if max_id < int(row['id']):
                max_id = int(row['id'])

    user['id'] = str(max_id + 1)
    with open('database.csv', 'a', encoding='utf-8', newline='') as csvfile:
        fnames = ['id', 'last_name', 'first_name', 'second_name', 'number']
        csv_writer = csv.DictWriter(csvfile, fieldnames=fnames)
        csv_writer.writerow(user)   


