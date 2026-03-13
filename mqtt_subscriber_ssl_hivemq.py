import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, reason_code, properties):
    print("Connected with result code "+str(reason_code))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.

    # Utilizad cada uno el topico con el que publique datos en el publicador
    client.subscribe("mytopic/dgm")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))


def on_even(client, userdata, msg):
    print("Even number: "+msg.topic+" "+str(msg.payload))


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

client.tls_set()
#client.tls_set("ca.crt")
#client.tls_insecure_set(True)
client.username_pw_set(username="YOUR_USERNAME",password="YOUR_PASSWORD")
client.connect("YOUR_BROKER_ADDRESS", 8883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
