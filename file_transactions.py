import json
import os
import datetime


def convert_to_json(list, json_file_name):

    with open(json_file_name + '.json', 'w') as json_file:
        json.dump(list, json_file, indent=4)


def read_json(json_file_name):
    with open(json_file_name + '.json', 'r') as json_file:
        data = json.load(json_file)

    return data


def remove_2days_file(now, coin_name):
    remover_time = now - datetime.timedelta(days=2)
    remover_dt_string = remover_time.strftime("%d%m%Y%H%M")
    file_name = '1m{}data{}.json'.format(coin_name, remover_dt_string)

    if os.path.exists(file_name) and os.path.isfile(file_name):
        os.remove(file_name)

    else:
        print("Silmek istediğiniz {} dosyası mevcut değil!".format(file_name))


def remove_4hours_file(now):
    remover_time = now - datetime.timedelta(hours=4, minutes=30)
    remover_dt_string = remover_time.strftime("%d%m%Y%H%M")
    file_name = '1malltickersdata{}.json'.format(remover_dt_string)

    if os.path.exists(file_name) and os.path.isfile(file_name):
        os.remove(file_name)

    else:
        print("Silmek istediğiniz {} dosyası mevcut değil!".format(file_name))


# def remove_folder(folder_name):
#     if os.path.exists(folder_name):
#         os.chdir(folder_name)
#         files = os.listdir()
#         for file in files:
#             os.remove(file)
#         os.chdir(os.pardir)
#         os.rmdir(folder_name)
