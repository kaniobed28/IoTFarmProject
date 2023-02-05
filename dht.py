import network
from umqtt.simple import MQTTClient
from time import sleep
import random
import json
from machine import Pin
import dht

# function to generate random numbers for experiment
def random_dht():
    temp = random.randint(0,35)
    
    humd = random.randint(0,35)
    print(temp,humd)
    data = {
        'temp':temp,
        'humd':humd
        }
    return json.dumps(data)
#function to read data from the dht sensor
def read_dht_data(pin_num):
    d = dht.DHT11(Pin(pin_num,Pin.IN))
    for i in range(3):
        try:
            d.measure()
            temperature = d.temperature()
            humidity = d.humidity()
            print("Temperature: %.1f C" % temperature)
            print("Humidity: %.1f %%" % humidity)
            return
        except OSError as e:
            if e.args[0] == 116:
                print("Timed out, attempting to read again...")
                continue

#function to connect to wifi
def wifi_connect(ssid,password):
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("Connecting to network...")
        sta_if.active(True)
        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            print('...')
            sleep(2)
    print("Connected to network:", sta_if.ifconfig())
#function to connect to mqtt broker   
def mqtt_connect(client_id,broker):
    client = MQTTClient(client_id,broker)
    client.connect()
    print('mqtt connected')
    return client
#function to publish a message
def mqtt_publish(client,topic,message):
    client.publish(topic,message)
    #client.disconnect()
 
#function to subscribe to a message 
def mqtt_subscribe(client,topic):
    client.connect()
    client.set_callback(on_message)
    client.subscribe(topic)
    return client

#deals with what happens when a msg is received
def on_message(topic,msg):
    print(f'{topic.decode()} : {msg.decode()}')

wifi_connect('DESKTOP-OS6KTER 0020','33333333')
client = mqtt_connect('dhtclient','broker.mqttdashboard.com')
mqtt_publish(client,'mytopic','this is a message')
sub_client = mqtt_subscribe(client,'dhtclient')
while True:
    mqtt_publish(client,'mytopic',(random_dht()))
    random_dht()
    sub_client.check_msg()
    sleep(2)
    #read_dht_data(15)


