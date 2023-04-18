import requests
from discordbot import DiscordBot
import telebot
import subprocess
import json

MAIN_CHANNEL = (1068776705042415626, 1068776705042415629)

secret = json.load(open("secret.json"))
userbot = DiscordBot(secret["login"], secret["password"], debug=False)
tbot = telebot.TeleBot(secret["tg_key"])


def downloadImage(url):
    img_data = requests.get(url).content
    with open('out.'+url[-3:], 'wb') as handler:
        handler.write(img_data)


def midJourney(prompt):
    proc = subprocess.Popen(
        ['python3', 'getAnswerBot.py'], stdout=subprocess.PIPE)
    userbot.sendMessage(*MAIN_CHANNEL, "/imagine "+prompt)
    for line in proc.stdout:
        print(line)
        if "https://" in str(line):
            return str(line)[2:-3]


@tbot.message_handler(commands=['start'])
def start(message):
    tbot.send_message(message.from_user.id,
                      "Your user_id: "+str(message.from_user.id))


@tbot.message_handler(commands=['imagine'])
def imagine(message):
    tbot.send_message(message.chat.id, "generating..")
    print(message.text)
    url = midJourney(message.text.replace("/imagine ", ""))
    print(url)
    downloadImage(url)
    tbot.send_chat_action(message.chat.id, 'upload_photo')
    img = open('out.png', 'rb')
    tbot.send_photo(message.chat.id, img,
                    reply_to_message_id=message.message_id)
    img.close()


tbot.polling(none_stop=True, interval=0)
