import file_transactions
import time


def countdown(t):
    while t:
        mins, secs = divmod(t, 100)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        t -= 1

def deleting_users():
    user_list = file_transactions.read_json("users")
    delete_user_list = file_transactions.read_json("deleted_user_list")
    deleting_user_list = []
    for x in user_list:
        user_list[x]['days_left'] -= 1
        if(user_list[x]['days_left'] == 0):
            deleting_user_list.append(x)
    for i in deleting_user_list:
        del user_list[i]
        delete_user_list.append(i)
    file_transactions.convert_to_json(user_list, "users")
    file_transactions.convert_to_json(
        delete_user_list, "deleted_user_list")

while True:
    countdown(5)
    deleting_users()


