"""EE 250L Lab 07 Skeleton Code

Run vm_subscriber.py in a separate terminal on your VM."""

import paho.mqtt.client as mqtt
import time
from pynput import keyboard

def ultrasonic_callback(client, userdata, message):
    newMessage = (str(message.payload, "utf-8"))
    print(newMessage)
def button_callback(client, userdata, message):
    print("Button pressed")

def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

    #subscribe to the ultrasonic ranger topic here
    client.subscribe("anrg-pi2/ultrasonicRanger")
    client.subscribe("anrg-pi2/button")
    client.message_callback_add("anrg-pi2/ultrasonicRanger", ultrasonic_callback)
    client.message_callback_add("anrg-pi2/button", button_callback)
#Default message callback. Please use custom callbacks.
def on_message(client, userdata, msg):
    print("on_message: " + msg.topic + " " + str(msg.payload))

def on_press(key):
    if __name__ == '__main__':
        #this section is covered in publisher_and_subscriber_example.py
        client = mqtt.Client()
        client.on_message = on_message
        client.on_connect = on_connect
        client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)
        client.loop_start()

        while True:
            print("delete this line")
            time.sleep(1)

if __name__ == '__main__':
    #this section is covered in publisher_and_subscriber_example.py
    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)
    client.loop_start()

    while True:
        print("delete this line")
        time.sleep(1)
            

