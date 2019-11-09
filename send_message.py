import vk_api, random,time,socket
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

vk = vk_api.VkApi(token='e3cab8bc244b9464646db0b4b684c277d1ef69850c589881c70cd0a11445b42cdc125dfc80bc8f1ec471a')
vk._auth_token()
snd = vk.get_api()
server ='localhost', 5050
longpoll = VkBotLongPoll(vk,187536433)
sor = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sor.bind(('', 0))
def say_ser(mes):
    sor.sendto(mes.encode('utf-8'),server)
while True:
    msg = input('> ')
    try:
        say_ser(msg)
        snd.messages.send(chat_id = 2, message = msg,random_id =random.randint(0, 2147483647))
    except:
        continue
