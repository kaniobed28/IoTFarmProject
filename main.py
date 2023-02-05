from machine import Pin
import time
import network
from umqtt.simple import MQTTClient
import dht


def on_message(topic, msg):
    print("Topic: {}, Message: {}".format(topic, msg.decode()))


pin15 = Pin(15,Pin.OUT)
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('DESKTOP-OS6KTER 0020', '33333333')
while not sta_if.isconnected():
    print('...')
    time.sleep(2)
print('Connection successful')
print('Network config:', sta_if.ifconfig())
#from umqtt.simple import MQTTClient

def sub_cb(topic, msg):
    print((topic, msg))

client = MQTTClient("clientId-LYP4YjRWAj", "10.76.11.239",keepalive=10)
client.set_callback(on_message)
client.connect()
print('mqtt connected')
client.subscribe(b"testtopic/1")
#client.publish(b"testtopic/1", b"hello")
while True:
    client.check_msg()
    print('checking')
    time.sleep(2)
