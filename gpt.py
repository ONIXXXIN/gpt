import telebot
import ns
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import random
import pyautogui

from openai import OpenAI

client = OpenAI(api_key="sk-proj-4hYf1piDCKcaL2G5AsXAT3BlbkFJO4JS7cRz7BUD1qx7oYkJ")
bot = telebot.TeleBot(ns.TOKEN)
uriy = []
donnate = [629401483, 6871116267, 5281764431, 136962775]


@bot.message_handler(commands=["start"])
def kinder(message):
    knopki = ReplyKeyboardMarkup(resize_keyboard=True)
    btr1 = KeyboardButton("купить подписку")
    knopki.add(btr1)
    bot.send_message(message.from_user.id,
                     "To have the bot draw a picture, write “draw” and then a description of the picture.Sample:draw a cat \n"
                     "To talk to GPT - just send a message. \n\n"
                     "Чтобы бот нарисовал картинку - напиши «нарисуй» , а затем описание картинки.Шаблон:нарисуй котика \n"
                     "Чтобы поговорить с GPT - просто отправьте сообщение.", reply_markup=knopki)


@bot.message_handler(content_types=["text"])
def ky(message):
    print(message.text)
    print(message.from_user.first_name)
    print(message.from_user.username)
    print(message.from_user.id)
    if message.text[0:7].lower() in ["нарисуй", "draw"]:
        if message.from_user.id in donnate:
            response = client.images.generate(
                model="dall-e-3",
                prompt=message.text[7:],
                size="1024x1024",
                quality="standard",
                n=1, )

            image_url = response.data[0].url

            bot.send_photo(message.from_user.id, image_url)
        else:
            bot.send_message(message.from_user.id, "купи подпискуууу")


    elif message.text == "купить подписку":
        knopki = InlineKeyboardMarkup()
        btr = InlineKeyboardButton("купить подписку",
                                   url="https://www.youtube.com/watch?v=jz2qWxKYBqw&ab_channel=MadFutPlays")
        knopki.add(btr)
        bot.send_message(message.from_user.id, "тогда тебе сюда", reply_markup=knopki)


    else:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": ns.PROMPT},
                {"role": "user", "content": message.text}])
        ufx = response.choices[0].message.content
        bot.send_message(message.from_user.id, ufx)


bot.polling()

"""
создать список где-то вверху и поместить туда тебя (именно айдишник, узнать здесь: @getmyid_bot)
а затем сделать проверку, что если юзер есть в списке, то можно отправить картинку, а если нет, то написать: «сперва купите подписку у нас»

"""
