# Ob-havo haqida ma'lumot beruvchi botimizga xush kelibsiz !!!!
# Muallif: Hamdamov Nozimjon.
# 1-qadam : O'zimizga kerakli bo'lgan kutubxonalarni chaqirib olamiz. 
from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler,CallbackQueryHandler, ConversationHandler, MessageHandler, Filters
import requests
from bs4 import BeautifulSoup as BS 
import logging as lg



def logging():
	lg.basicConfig(
    	format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=lg.INFO)
	logger = lg.getLogger(__name__)

# Start tugmasi uchun funksiyasini kiritib olamiz.
def start(update,context):
	user = update.message.from_user
	update.message.reply_html("Assalomu Aleykum <b>{}</b>🤝!. \n \n Ob-havo🌦 haqida ma'lumot beruvchi 🤖botimizga xush kelibsiz😊.\nILtimos kerakli hududni kiriting (Eslatma tarzida hududlarni krill alifbosida kirgizing.👇)\n Misol uchun: <b>Бухара</b>".format(user.first_name))

# API bilan ishlash qismi uchun funksiyani tuzib olamiz.
def first(update,context):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'}
    r = requests.get('https://sinoptik.ua/погода-{}'.format(update.message.text), headers=headers)
    wth = update.message.text
    html = BS(r.content,'html.parser')
    minimum = html.findAll("div",{"class": "min"})
    maximum = html.findAll("div", {"class" : "max"})
    date = html.findAll("p", {"class": "date"})
    month = html.findAll("p", {"class": "month"})
	#############################################
    t_min = minimum[0].text
    t_max = maximum[0].text
    t_date = date[0].text
    t_month = month[0].text
    update.message.reply_text("{} belgilandi. Bugun {}-{}, {}da ob-havo 🌦👇: ".format(wth,t_date,t_month,wth) + '\n' + "Eng past daraja⬇️ :" + t_min + ','+ '\n' + "Eng yuqori daraja⬆️ :"+ t_max)

# Yordam tugmasi uchun funksiyani qo'shib olamiz.
def help_command(update,context):
    update.message.reply_html("Yordam uchun 👨‍💻<b>@nozimjon_hamdamov</b>ga murojaat qiling .")

# Admin tugmasi uchun funskiyani qo'shib olamiz.
def admin(update,context):
    update.message.reply_text("Admin👨🏻‍💻 bilan bog'lanish - @nozimjon_hamdamov ")

# Token, tugmalarga funksiylarni ula1535776751:AAENKr4UR3yuQlU2sWX70zwmZbB9L9YGHxIsh uchun funksiya tuzib olamiz.
updater = Updater('1535776751:AAENKr4UR3yuQlU2sWX70zwmZbB9L9YGHxI', use_context = True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('admin', admin))
dispatcher.add_handler(CallbackQueryHandler(first))
dispatcher.add_handler(MessageHandler(Filters.text,first))

# botni ishga tushiruvchi buyruq.
updater.start_polling()
# Run the bot until the user presses Ctrl-C or the process receives SIGINT,SIGTERM or SIGABRT
updater.idle()