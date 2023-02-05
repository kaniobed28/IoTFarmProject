import paho.mqtt.client as mqtt
import time
import json

# Define the callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("mytopic")

# Define the callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload.decode()))
    with open('data.txt', 'a') as f:
        data = msg.payload.decode()
        data = data[1:-1]
        f.writelines(data +'\n')

# Create a new instance of the client.
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Connect to the broker.
client.connect("broker.mqttdashboard.com", 1883, 60)

# Start the network loop.
# client.loop_start()

# Publish a message to the broker.


# Wait for the message to be sent.
# client.loop_stop()
client.loop_forever()
client.publish("farm", "Hello World")
time.sleep(2)