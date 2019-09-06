## IMPORTANT
dev = True

import tweepy
from os import environ as env
from dotenv import load_dotenv

load_dotenv()

consumer_key = env["consumer_key"]
consumer_secret = env["consumer_secret"]
access_token = env["access_token"]
access_token_secret = env["access_token_secret"]

#Logando com elas no twitter
if(not dev):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth) #Cria objeto da api

from datetime import datetime, timezone, timedelta
import requests
from status import textoAlmoco, textoJantar, textoLanche

dias = [
    'seg',
    'ter',
    'qua',
    'qui',
    'sex',
    'sab',
    'dom'
]

url = "https://raw.githubusercontent.com/coelhobf/ufv_ru_bot/master/semanal.json"

tw_almoco = True
tw_jantar = True
tw_day = -1

diff = timedelta(hours = -3) # fuzo do brasil
fuzo = timezone(diff)

print("Iniciado, aguardando horario de publicar")

while(True):

    # pega a data atual com fuzo horário do brasil
    dia = datetime.now(fuzo)

    # verifica se o dia da ultima publicação é igual ao dia atual
    # se for diferente, reseta as flags de publicação
    if(tw_day != dia.day):
        tw_day = dia.day
        tw_almoco = False
        tw_jantar = False

    if(dev or not tw_almoco and dia.hour == 10 and dia.minute == 0):

        resp = requests.get(url=url)
        data = resp.json()

        almoco = data[str(dia.weekday())]["almoco"]

        almoco_base = f"ALMOÇO {dias[dia.weekday()]}, {dia.day}\n"
        almoco = almoco_base + textoAlmoco(almoco)

        status = almoco
        if(dev):
            if(not tw_almoco):
                print(status)
        else:
            api.update_status(status = status)
            print("Almoço publicado")

        
        tw_almoco = True
    
    if(dev or not tw_jantar and dia.hour == 16 and dia.minute == 00):

        resp = requests.get(url=url)
        data = resp.json()

        jantar = data[str(dia.weekday())]["jantar"]
        lanche = data[str(dia.weekday())]["lanche"]
 
        jantar_base = f"JANTAR {dias[dia.weekday()]}, {dia.day}\n"
        jantar = jantar_base + textoJantar(jantar)

        lanche_base = f"LANCHE {dias[dia.weekday()]}, {dia.day}\n"
        lanche = lanche_base + textoLanche(lanche)

        status = jantar
        if(dev):
            if(not tw_jantar):
                print(status)
        else:
            api.update_status(status = status)
            print("Jantar publicado")
        

        status = lanche
        if(dev):
            if(not tw_jantar):
                print(status)
        else:
            api.update_status(status = status)
            print("Lanche publicado")
        

        tw_jantar = True
        