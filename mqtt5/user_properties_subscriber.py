import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, reason_code, properties):
    print("Conectado con código:", reason_code)

def on_message(client, userdata, msg):
    print(str(msg))
    print(f"\nMensaje recibido en {msg.topic}: {msg.payload.decode()}")
    print(msg.properties)
    # Verificar si hay propiedades en el mensaje
    if msg.properties and msg.properties.UserProperty:
        print("Propiedades recibidas:")
        for key, value in msg.properties.UserProperty:
            print(f"  - {key}: {value}")

broker = "broker.emqx.io"
#broker = "localhost"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2,protocol=mqtt.MQTTv5)  # Versión 2 para MQTT 5

client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, 1883)
client.subscribe("uma/mqtt5/properties", qos=1)  # Suscribirse al tópico donde llegan mensajes con propiedades

client.loop_forever()
