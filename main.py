import telebot
import os
import requests
import random

token = os.getenv('TOKEN')
bot = telebot.TeleBot(token)


class CatGetter:
    def __init__(self):
        self.urls_list = requests.get('https://catoverflow.com/api/query?offset=0&limit=10000000',
                                      verify=False).text.rstrip().split()

    def get_picture(self):
        url = random.choice(self.urls_list) + '.jpg'
        return requests.get(url, verify=False).content


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(commands=['cat'])
def send_picture_of_cat(message):
    with open('./pic.jpg', 'wb') as new_pic:
        new_pic.write(CatGetter().get_picture())
    with open('./pic.jpg', 'rb') as pic:
        bot.send_photo(message.chat.id, pic)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.infinity_polling()
