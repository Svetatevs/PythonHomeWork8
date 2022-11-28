from view2 import get_action, add_user, get_user
from csv_append2 import append_user
from csv_update2 import update_user
from csv_del2 import delete_user

def start_engine():

    act = 1
    while act != 0:
        act = get_action()
        if act == 1:
           get_user(1)
        elif act == 2:
           get_user(2)
        elif act == 3:
           add_user()
        elif act == 4:
           delete_user()
        elif act == 5:
           update_user()

    print("До свидания!")



