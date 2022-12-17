import serial
import paho.mqtt.publish as publish
from time import sleep

LoRa = serial.Serial("/dev/ttyS0", 9600)
host = "localhost"

def Recebe_dados():
    tamanho_file = LoRa.inWaiting    
    while tamanho_file > 1:
        comandoLido = LoRa.read(tamanho_file)

    return comandoLido


while True:
    dados = Recebe_dados()
    publish.single(topic="telemetria", payload= dados, hostname=host)
    sleep(5)

