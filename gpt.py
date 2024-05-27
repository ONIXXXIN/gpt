import telebot
import ns
import random
import pyautogui
from openai import OpenAI
client = OpenAI(api_key="sk-proj-maJ8LTTnbnAuIoNdfvXoT3BlbkFJisebZVtCCYJ09Reu2lmo")
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
    response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "общайся только зумерским сленгом, не кринжуй и не юзай плохих слов. ты - Влад, живёшь в Каннах, шаришь за многие вещички. + изучаешь французский. в предложениях иногда пиши: кек, лол, ору, хз, мб, ахахах"},
        {"role": "user", "content": message.text}])
    ufx = response.choices[0].message.content
    bot.send_message(message.from_user.id, ufx )


bot.polling()


"""
Код из main.py достать и закинуть в ту функцию, где обрабатываются именно сообщения (не команды)

В том коде у тебя есть промт и инпут данные (входные данные)
"role": "user", "content": "броу как быстро пропылесосить " - в этой строчке нужно менять надпись "броу как быстро..."
Сюда подставлять то, что написал юзер и на этом этапе вспомнить, а где мы ловим текст сообщения от юзера.

Простыми словами: скопировать, втсавить и в правильном месте подставить значения.

"""