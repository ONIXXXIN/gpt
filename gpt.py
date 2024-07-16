import telebot
import ns
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from openai import OpenAI, PermissionDeniedError

client = OpenAI(api_key="sk-proj-4hYf1piDCKcaL2G5AsXAT3BlbkFJO4JS7cRz7BUD1qx7oYkJ")
bot = telebot.TeleBot(ns.TOKEN)
uriy = []
donnate = [629401483, 6871116267, 5281764431, 136962775]

prompts = {}


@bot.message_handler(commands=["start"])
def kinder(message):
    prompts [message.from_user.id] = "шо ты лысый"
    print(prompts)
    knopki = ReplyKeyboardMarkup(resize_keyboard=True)
    btr1 = KeyboardButton("купить подписку")
    knopki.add(btr1)
    bot.send_message(message.from_user.id,
                     "To have the bot draw a picture, write “draw” and then a description of the picture.Sample:draw a cat \n"
                     "To talk to GPT - just send a message. \n"
                     "To change the prompt (the manner of communication, etc.), write \"/prompt (and here is your prompt)\", if you want the bot to answer you in your language, write the prompt in your language. \n\n"
                     "Чтобы бот нарисовал картинку - напиши «нарисуй» , а затем описание картинки.Шаблон:нарисуй котика \n"
                     "Чтобы поговорить с GPT - просто отправьте сообщение .\n"
                     "Чтобы поменять промт(манеру общения и т д) напиши, \"/prompt(а тут твой промт)\", если хочешь чтобы бот отвечал тебе на твоем языке пиши промт на твоем языке", reply_markup=knopki)

@bot.message_handler(commands=["prompt"])
def pilesos(message):
    ananas = message.text[8:]
    prompts[message.from_user.id] = ananas
    print(prompts)

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
                                   url = "https://www.google.com/search?sca_esv=04aa412ff406bf20&sxsrf=ADLYWILpUGznJkslni83XOud41G792GQjw:1720465697579&q=%D1%83%D0%BD%D0%BD%D0%B2+%D0%B1%D0%B5%D0%B7+%D0%B4%D0%B0%D1%82%D1%8B&stick=H4sIAAAAAAAAAONgFuLVT9c3NEzLyk0pMcgpVIJwM0yLCo2zy020BH1LizOTHYtKMotLQvKD8_PSF7FKXGy-sBcINylc2Hhh64XtChe2XNhwseliNwAmP-KzTgAAAA&sa=X&ved=2ahUKEwjRxoCWkpiHAxVkQlUIHRxaBekQri56BAhKEAU&biw=1270&bih=582&dpr=1.25")
        knopki.add(btr)
        bot.send_message(message.from_user.id, "тогда тебе сюда", reply_markup=knopki)


    else:
        try:
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": ns.PROMPT},
                    {"role": "user", "content": message.text}])
            ufx = response.choices[0].message.content
        except PermissionDeniedError:
            print("dix petits nègres")
        else:
           bot.send_message(message.from_user.id, ufx)




bot.polling()

"""
- В бота добавить картинки/видео/гифки, по желанию
- Добавить команду по которой можно видеть всех, кто есть в списке ДОНАТ
    - Команда должна выводить только админу (тебе), другим запретить доступ
- Сделать так, чтобы можно было менять промт по какой-то команде
- Узнать что такое try/except/finally/else и рассказать :))
- Поиграть в роблокс 8 минут
"""
