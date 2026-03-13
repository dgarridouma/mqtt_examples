import paho.mqtt.client as mqtt
import time

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, reason_code, properties):
    print("Connected with result code "+str(reason_code))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    #client.subscribe("$SYS/#")

# The callback is called when a PUBLISH message is received from the server.
def on_publish(client, userdata, mid, reason_code, properties):
    print("Published: "+str(mid))

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_publish = on_publish

client.tls_set()
#client.tls_set("ca.crt")
#client.tls_insecure_set(True)
client.username_pw_set(username="YOUR_USERNAME",password="YOUR_PASSWORD")
client.connect("YOUR_BROKER_ADDRESS", 8883, 60)

client.will_set("mytopic/dgm/will","disconnected!") # Use an unique topic
client.loop_start()

for i in range(100):
    print(i)
    msg="Message "+str(i)

    client.publish("mytopic/dgm", msg, qos=0, retain=False)

    # Only for testing purposes
    if i%2==0:
        client.publish("mytopic/dgm/even", msg, qos=0, retain=False)
    time.sleep(5)

client.disconnect()

