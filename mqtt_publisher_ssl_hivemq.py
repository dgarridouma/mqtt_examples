import paho.mqtt.client as mqtt
import random
import time
import json

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, reason_code, properties):
    print("Connected with result code "+str(reason_code))

# The callback is called when a PUBLISH message is received from the server.
def on_publish(client, userdata, mid, reason_code, properties):
    print("Published: "+str(mid))
    
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_publish = on_publish

client.tls_set()
client.username_pw_set(username="YOUR_USERNAME",password="YOUR_PASSWORD")
client.connect("YOUR_BROKER_ADDRESS", 8883, 60)

client.loop_start()

while True:
    msg=dict()
    msg['temperature']=random.randint(25,30)
    msg['humidity']=random.randint(70,90)
    msg['pressure']=random.randint(1000,1030)
    json_data=json.dumps(msg,default=str)

    client.publish("mytopic/dgm", json_data, qos=0, retain=False)

    time.sleep(5)



