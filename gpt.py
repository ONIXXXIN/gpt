import telebot
import ns
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import random
import pyautogui

from openai import OpenAI
client = OpenAI(api_key="sk-proj-4hYf1piDCKcaL2G5AsXAT3BlbkFJO4JS7cRz7BUD1qx7oYkJ")
bot = telebot.TeleBot(ns.TOKEN)


@bot.message_handler(commands = ["start"])
def kinder(message):
    knopki = ReplyKeyboardMarkup(resize_keyboard=True)
    btr1 = KeyboardButton("купи больше попыток")
    btr2 = KeyboardButton("нарисуй картинку")
    knopki.add(btr1)
    bot.send_message(message.from_user.id, '999', reply_markup = knopki)
@bot.message_handler(content_types=["text"])
def ky(message):
    print(message.text)
    print(message.from_user.first_name)
    print(message.from_user.username)
    print(message.from_user.id)
    # response = client.chat.completions.create(
    # model="gpt-4o",
    # messages=[
    #     {"role": "system", "content": ns.PROMPT },
    #     {"role": "user", "content": message.text}])
    # ufx = response.choices[0].message.content
    # bot.send_message(message.from_user.id, ufx)
    if message.text[0:7].lower() == "нарисуй":

        response = client.images.generate(
            model="dall-e-3",
            prompt=message.text[7:],
            size="1024x1024",
            quality="standard",
            n=1,)

        image_url = response.data[0].url

        bot.send_photo(message.from_user.id,image_url)


bot.polling()


"""
создать список где-то вверху и поместить туда тебя (именно айдишник, узнать здесь: @getmyid_bot)
а затем сделать проверку, что если юзер есть в списке, то можно отправить картинку, а если нет, то написать: «сперва купите подписку у нас»

"""


