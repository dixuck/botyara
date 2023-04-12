import telebot
from decouple import config
from telebot import types
from parse import news, wishnum


TOKEN = config('TOKEN')  # name: botyara_n2; https://t.me/pityhonnbot

bot = telebot.TeleBot(TOKEN)

is_digit = lambda x: x.isdigit() if x[:1]!='-' else x[1:].isdigit()


@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("start")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "Привет, я был создан для одной из самых бесполезных целей - находить первые 20(или сколько угодно, но makers захотели 20) новостей Кыргызстана из сайта кактус или фикус не помню уже. Нажми start и получишь новости =(", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text.lower() == 'start':

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn2 = types.KeyboardButton('Quit')
        markup.add(btn2)
        ans = 'Напиши номер новости ниже и я дам тебе ссылку с изображением 👇\n'
        for new in news:
            ans += f'{str(new[0])}: {new[1][0]}\n'
        bot.send_message(message.from_user.id, ans, reply_markup=markup)

    elif is_digit(message.text):
        if int(message.text) in (range(1, wishnum+1)):
            for num, result in dict(news).items():
                if num == int(message.text):
                    bot.send_message(message.from_user.id, f'Ссылка:\n{result[1]}\nСсылка на убогое изображение:\n{result[2]} ') # result = title, link, img
        else: bot.send_message(message.from_user.id, 'Новости с таким номером нет')


    elif message.text.lower() == 'quit':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("start")
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'До свидания', reply_markup=markup)
    else:
        bot.send_message(message.from_user.id, 'Я тебя не понимаю')

bot.polling(none_stop=True, interval=0)