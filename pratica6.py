from picamera import PiCamera, Color
from requests import get 
from time import sleep
from pprint import pprint
import json

camera=PiCamera()
camera.rotation = 180
camera.start_preview()
camera.annotate_text = "11352737 e 11279728"
sleep(5)
camera.capture('/home/sel/SEL0337/carlosejoao.jpg')
camera.stop_preview()

camera.start_preview()
camera.annotate_text = "11352737 e 11279728"
camera.start_recording('/home/sel/SEL0337/videocarlosejoao.h264')
sleep(5)
camera.stop_recording()
camera.stop_preview()

weather = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/966583'
my_weather = get(weather).json()['items']
pprint(my_weather)