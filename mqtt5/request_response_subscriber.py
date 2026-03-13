import paho.mqtt.client as mqtt
from paho.mqtt.properties import Properties
from paho.mqtt.packettypes import PacketTypes

broker = "broker.emqx.io"
request_topic = "uma/mqtt5/request_topic"

def on_message(client, userdata, msg):
    print("Solicitud recibida:", msg.payload.decode())

    response_topic = getattr(msg.properties, "ResponseTopic", None)
    if response_topic:
        print("Respondiendo a:", response_topic)
        response_payload = "pong"

        props_in = msg.properties
        props_out = Properties(PacketTypes.PUBLISH)
        props_out.ResponseTopic = response_topic

        correlation = props_in.CorrelationData
        print("Correlation:", correlation.decode())

        props_out.CorrelationData = correlation

        client.publish(response_topic, payload=response_payload, qos=1, properties=props_out)
    else:
        print("No se especifico ResponseTopic, no se puede responder.")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, protocol=mqtt.MQTTv5)
client.on_message = on_message
client.connect(broker, 1883)
client.subscribe(request_topic)
print("Escuchando solicitudes en", request_topic)
client.loop_forever()
