import json
import botlib
import telebot

codeLength = [10, 13]

with open('settings.json', encoding='utf-8') as file:
    settings = json.load(file)   
    botToken = settings['api.key.bot']


bot = telebot.TeleBot(token=botToken, parse_mode='html')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    reply = botlib.getReply('welcome')
    bot.send_message(message.chat.id, reply)
    
    
@bot.message_handler()
def parse_message(message):
    reply = botlib.getReply('wrong')
    
    if len(message.text) in codeLength:
        reply = botlib.getReply('makeRequest', message.text)
        
    bot.send_message(message.chat.id, reply)
    
    
bot.infinity_polling()