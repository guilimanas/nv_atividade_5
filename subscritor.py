import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
import json
import time
import configparser
import pygame
import os

pygame.init()

def tocar_audio():
    if os.path.exists('audio.mp3'):
        pygame.mixer.music.load('audio.mp3')
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(5)
        clock = pygame.time.Clock()
        clock.tick(10)
        while pygame.mixer.music.get_busy():
            pygame.event.poll()
            clock.tick(10)
    else:
        print('O arquivo musica.mp3 não está no diretório do script Python')
def on_message(client,userdate,message):
    dados=json.loads(str(message.payload.decode()))
    
    # if dados['field1']=="ABRIU":
    if int(dados['field1'])==1:
        # print(dados['field1'])
        print("ABRIU")
        tocar_audio()

broker="mqtt.thingspeak.com"
port=1883
config=configparser.ConfigParser()
config.read('conf')
topico=config['THINGSPEAK']['TOPICO_SUBSCRIBE']
username=config['THINGSPEAK']['USERNAME']
password=config['THINGSPEAK']['MQTT_API_KEY']
subscribe.callback(on_message,qos=0,topics=topico,hostname=broker,port=port,client_id="clisub",auth={'username':username,'password':password})

while(True):
    time.sleep(15)