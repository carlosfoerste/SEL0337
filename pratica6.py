#Importa bibliotecas necessarias
#biblioteca picamera possui funçoes úteis de manipulação de imagem 
from picamera import PiCamera, Color
#get() acessa os dados climaticos em java
from requests import get 
#sleep() possibilita delay na captura de imagem 
from time import sleep
#pprint() imprime os dados coletados od URL 
from pprint import pprint
#Módulo json extrai dados relevantes
import json

#Configuração da camera
camera=PiCamera()
#Rotaciona camera em 180º
camera.rotation = 180
#Inicia a visualização da camera
camera.start_preview()
#Registra os NUSP no display da camera 
camera.annotate_text = "11352737 e 11279728"
#Conta 5s antes da captura 
sleep(5)
#Captura a imagem 
camera.capture('/home/sel/SEL0337/carlosejoao.jpg')
#Encerra a visualização da camera
camera.stop_preview()

#Inicia a visualização da camera
camera.start_preview()
#Registra os NUSP no display da camera
camera.annotate_text = "11352737 e 11279728"
#Inicia a gravação
camera.start_recording('/home/sel/SEL0337/videocarlosejoao.h264')
#conta 5s
sleep(5)
#Encerra a gravação
camera.stop_recording()
#Encerra a visualização da camera
camera.stop_preview()

#URL da Oracle com o ID da UFSC
weather = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/966583'
#Acessa os dados climaticos 
my_weather = get(weather).json()['items']
#Imprime os dados climasticos no terminal 
pprint(my_weather)