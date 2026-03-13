import paho.mqtt.client as mqtt
from paho.mqtt.properties import Properties
from paho.mqtt.packettypes import PacketTypes
import time
import uuid

broker = "broker.emqx.io"
request_topic = "uma/mqtt5/request_topic"
response_topic = "uma/mqtt5/response/" + str(uuid.uuid4())

def on_message(client, userdata, msg):
    print("Respuesta recibida:", msg.payload.decode())
    print("Correlacion: "+msg.properties.CorrelationData.decode())

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, protocol=mqtt.MQTTv5)
client.on_message = on_message
client.connect(broker, 1883)
client.subscribe(response_topic)

props = Properties(PacketTypes.PUBLISH)
props.ResponseTopic = response_topic

client.loop_start()

print("ResponseTopic =", response_topic)
while True:
    correlation_id = str(uuid.uuid4()).encode()
    props.CorrelationData = correlation_id

    client.publish(request_topic, payload="ping", qos=1, properties=props)

    print("Solicitud enviada con Correlation =", correlation_id)
    time.sleep(5)
