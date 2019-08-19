import tweepy
from os import environ as env
from dotenv import load_dotenv

load_dotenv()

consumer_key = env["consumer_key"]
consumer_secret = env["consumer_secret"]
access_token = env["access_token"]
access_token_secret = env["access_token_secret"]

#Logando com elas no twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth) #Cria objeto da api

from datetime import datetime, timezone, timedelta
import requests
from status import textoAlmoco, textoJantar, textoLanche

url = "https://raw.githubusercontent.com/coelhobf/ufv_ru_bot/master/semanal.json"

tw_almoco = True
tw_jantar = True
tw_day = -1

diff = timedelta(hours = -3) # fuzo do brasil
fuzo = timezone(diff)

print("Iniciado, aguardando horario de publicar")

while(True):

    dia = datetime.now(fuzo)

    if(tw_day != dia.day):
        tw_day = dia.day
        tw_almoco = False
        tw_jantar = False

    if(not tw_almoco and dia.hour == 11 and dia.minute == 0):

        resp = requests.get(url=url)
        data = resp.json()

        almoco = data[str(dia.weekday())]["almoco"]

        almoco = textoAlmoco(almoco)

        # status = "[test]\n" + almoco
        status = almoco
        api.update_status(status = status)
        print("Almoço publicado")

        tw_almoco = True

    if(not tw_jantar and dia.hour == 17 and dia.minute == 00):

        resp = requests.get(url=url)
        data = resp.json()

        jantar = data[str(dia.weekday())]["jantar"]
        lanche = data[str(dia.weekday())]["lanche"]

        jantar = textoJantar(jantar)
        lanche = textoLanche(lanche)

        # status = "[test]\n" + jantar
        status = jantar
        api.update_status(status = status)
        print("Jantar publicado")

        status = lanche
        # status = "[test]\n" + lanche
        api.update_status(status = status)
        print("Lanche publicado")
        
        tw_jantar = True