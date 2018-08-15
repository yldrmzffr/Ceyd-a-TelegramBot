"""
MIT License

Copyright (c) 2018 Muzaffer YILDIRIM

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# coding=utf-8
import telebot
import requests
import json

bot = telebot.TeleBot("<<TELEGRAM-BOT-TOKEN-CODE>>")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Merhaba {} nasıl yadımcı olabilirim?".format(message.from_user.first_name))


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    arg = {'username': '<<CEYD-A-USERNAME>>', 'token': '<<CEYD-A-TOKEN-CODE>>','code': message.text.lower() ,'type':'text'}
    cevap = json.loads(requests.post("http://beta.ceyd-a.com/jsonengine.jsp", data=arg).content.decode('utf-8')[1:-3]).get("answer")
    bot.send_message(message.chat.id,cevap)


bot.polling()
