from email import message
from binance.client import Client
import config
from telegram.ext import *
from requests import *
import file_transactions
updater = Updater(token="5357518095:AAGtmKepEdAOkyop1NXKLVbjqOucpPlUZng")
dispatcher = updater.dispatcher
#bot = telebot.TeleBot(config.APi_KEY)
client = Client(config.API_KEY, config.API_SECRET)


def get_deposit_history(user_txid,  user_name):
    btc_deposits = client.get_deposit_history(coin='USDT')
    deleted_user_list = file_transactions.read_json("deleted_user_list")
    user_list = file_transactions.read_json("users")
    message_txt =""
    for i in deleted_user_list:
        if(i==user_txid):
            message_txt = "bu txid kullanılmış ya da eksik veya hatalı girdiniz tekrar deneyin"
        return message_txt
    for x in user_list:
        print(user_list[x])
        if(user_list[x]["user_name"]!=user_name):
            return "Bu txid ile kayıtlı başka bir kullanıcı var"
        
    for x in range(len(btc_deposits)):
        if(user_txid == btc_deposits[x]["txId"][18:] and float(btc_deposits[x]["amount"]) >= 10.4 and btc_deposits[x]["coin"] == "USDT" ):
            user_list = file_transactions.read_json("users")
            user_list[user_txid] = {"user_name": user_name, "days_left": 30}
            file_transactions.convert_to_json(user_list, "users")
            message_txt= "link"
        else:
            message_txt = "Lütfen yeniden deneyiniz"

    return message_txt



print(get_deposit_history("1653925802001", "basak"))
