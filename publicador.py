import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import random
import time
import configparser
broker="mqtt.thingspeak.com"
port=1883
config=configparser.ConfigParser()
config.read('conf')
topico=config['THINGSPEAK']['TOPICO_PUBLISH']
valor=0
saida="ABRIU"
while(True):
    valor=random.randint(0, 1)
    if valor==1:
        dados = f"field1={saida}&status=MQTTPUBLISH"
        publish.single(payload=dados, topic=topico, port=port, hostname=broker)
        print("ABRIU")
    else:
        print("FECHOU")
    time.sleep(20)