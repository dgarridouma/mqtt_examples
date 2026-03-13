import paho.mqtt.client as mqtt
import json

broker = "broker.emqx.io"
topic = "uma/mqtt5/payload_format"

def on_message(client, userdata, msg):
    props = msg.properties
    fmt = props.PayloadFormatIndicator
    tipo = "texto (UTF-8)" if fmt == 1 else "binario" if fmt == 0 else "no especificado"
    print(f"Recibido: {msg.payload.decode(errors='ignore')}")
    print(f"Formato indicado: {tipo}")

    content_type = getattr(props, "ContentType", None) # por si no lleva ContentType
    if fmt == 1 and content_type == "application/json":
        try:
            print(f"ContentType: {content_type}")
            data = json.loads(msg.payload.decode())
            print(data)
        except Exception as e:
            print("Error interpretando JSON:", e)


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, protocol=mqtt.MQTTv5)
client.on_message = on_message
client.connect(broker, 1883)
client.subscribe(topic)
client.loop_forever()

