import config
import threading
import time
import parse
import telebot

def habr_checker_thread():
    latest_task = -1
    while True:
        dt = parse.parse_main_page()
        if dt[0][2] > latest_task:
            for task in dt:
                if task[2] > latest_task:
                    broadcast_task(task)
            latest_task = dt[0][2]
        else:
            pass
        time.sleep(5)
        
def broadcast_task(task):
    users = get_reged_users()
    for user in users:
        if user != '':
            bot.send_message(int(user), f"{task[0]}\n{task[1]}")

def check_user_reged(user_tg_id):
    with open("users.txt", "r") as file:
        data = file.read().split()
    if str(user_tg_id) in data:
        return True
    else:
        return False


def reg_user(user_tg_id):
    with open("users.txt", "a+") as file:
        file.write(str(user_tg_id))

def get_reged_users():
    with open("users.txt", "r") as file:
        data = file.read().split()
    return data

bot = telebot.TeleBot(config.tg_bot_token)

@bot.message_handler(commands=["start"])
def start(m):
    if not check_user_reged(m.chat.id):
        reg_user(m.chat.id)
    bot.send_message(m.chat.id, "Вы зарегистрированы!")

if __name__ == "__main__":
    threading.Thread(target=habr_checker_thread).start()
    bot.polling(none_stop=True, interval=0)
