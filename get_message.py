#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from plyer import notification

import vk_api, random,time,datetime, socket,threading
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind (('localhost',5050))

def tip(title,msg):
    notification.notify(
    title=title,
    message=msg,
    app_name='Pushhh',
    timeout = 1
    )
def read_sok():
        while 1 :
                data , addres = sock.recvfrom(1024)
                tim = datetime.datetime.today().strftime("%H:%M")
                print('['+tim+'] ' + 'Diya Tayulor (id549205760) > ' + data.decode('utf-8'))
potok = threading.Thread(target=read_sok)
potok.daemon = True
potok.start()

vk = vk_api.VkApi(token='e3cab8bc244b9464646db0b4b684c277d1ef69850c589881c70cd0a11445b42cdc125dfc80bc8f1ec471a')
vk._auth_token()
snd = vk.get_api()
longpoll = VkBotLongPoll(vk,187536433)

while True:
        for event in longpoll.listen():
                if event.type == VkBotEventType.MESSAGE_NEW:
                        ids = int(event.object.from_id)
                        tim = datetime.datetime.today().strftime("%H:%M")
                        tip('New message', 'Message from ' + snd.users.get(user_ids=ids)[0]['first_name'] + ' ' + snd.users.get(user_ids=ids)[0]['last_name'] + ' > ' + event.object.text) 
                        print('[' + tim + '] ' +snd.users.get(user_ids=ids)[0]['first_name'] + ' ' + snd.users.get(user_ids=ids)[0]['last_name'] + ' (id' + str(event.object.from_id) + ') > ' + str(event.object.text))
