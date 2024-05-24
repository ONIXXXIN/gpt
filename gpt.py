import telebot
import ns
import random
import pyautogui
bot = telebot.TeleBot(ns.TOKEN)



@bot.message_handler(commands = ["start"])
def kinder(message):
    bot.send_message(message.from_user.id, '999')

@bot.message_handler(content_types=["text"])
def ky(message):
    print(message.text)
    print(message.from_user.first_name)
    print(message.from_user.username)
    print(message.from_user.id)


bot.polling()


"""
Код из main.py достать и закинуть в ту функцию, где обрабатываются именно сообщения (не команды)

В том коде у тебя есть промт и инпут данные (входные данные)
"role": "user", "content": "броу как быстро пропылесосить " - в этой строчке нужно менять надпись "броу как быстро..."
Сюда подставлять то, что написал юзер и на этом этапе вспомнить, а где мы ловим текст сообщения от юзера.

Простыми словами: скопировать, втсавить и в правильном месте подставить значения.

"""