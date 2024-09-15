import telebot
from telebot import types
import os
from dotenv import load_dotenv, find_dotenv


# bot = telebot.TeleBot('7282018206:AAFNZuiT33TvxJi2lZ4uR80NETEp2nn6R2M')

load_dotenv(find_dotenv())
bot = telebot.TeleBot(os.getenv('TOKEN'))


@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('👨‍🦱Man')
    btn2 = types.KeyboardButton('👩Woman')
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, "Welcome! What's your gender? 👨‍🦱/👩", reply_markup=markup)

@bot.message_handler(content_types = ['text'])
def get_text_messages(message):

        if message.text == '👨‍🦱Man':
            markup = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton('💪Hands', url='https://www.youtube.com/watch?v=HZljSiK8UUY&pp=ygUi0YPQv9GA0LDQttC90LXQvdC40Y8g0L3QsCDRgNGD0LrQuA%3D%3D')
            btn2 = types.InlineKeyboardButton('🦵Legs', url='https://www.youtube.com/watch?v=9UAW39h9AwY&pp=ygUb0YLRgNC10L3QuNGA0L7QstC60LAg0L3QvtCz')
            btn3 = types.InlineKeyboardButton('Chest', url='https://www.youtube.com/watch?v=pTsViGMYoq4&pp=ygUl0YPQv9GA0LDQttC90LXQvdC40Y8g0L3QsCDQs9GA0YPQtNGMIA%3D%3D')
            btn4 = types.InlineKeyboardButton('Back side', url='https://www.youtube.com/watch?v=eVgR9JUS6z8&pp=ygUb0L3QsNC60LDRh9Cw0YLRjCDRgdC_0LjQvdGD')
            markup.add(btn1, btn2, btn3, btn4)
            bot.send_message(message.from_user.id, ('Which one part of ur body u want to pump up?🦍'), reply_markup = markup)

        elif message.text == '👩Woman':
            markup = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton('💪Arms', url= 'https://www.youtube.com/watch?v=LZadh0M13Bk&pp=ygUo0L3QsNC60LDRh9Cw0YLRjCDRgNGD0LrQuCDQttC10L3RidC40L3QtQ%3D%3D')
            btn2 = types.InlineKeyboardButton('🦵Legs', url= 'https://www.youtube.com/watch?v=n2t9t_Z_2ro&pp=ygUo0L3QsNC60LDRh9Cw0YLRjCDQvdC-0LPQuCDQttC10L3RidC40L3QtQ%3D%3D')
            btn3 = types.InlineKeyboardButton('Back side', url= 'https://www.youtube.com/watch?v=psvilt9vaoQ&pp=ygUq0L3QsNC60LDRh9Cw0YLRjCDRgdC_0LjQvdGDINC20LXQvdGJ0LjQvdC1')
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.from_user.id, ('Which one part of ur body u want to pump up?✨'), reply_markup = markup)
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback_query(call):
#     if call.data == 'back_from_man' or call.data == 'back_from_woman':
#         start(call.message)


bot.polling(none_stop=True, interval=0)