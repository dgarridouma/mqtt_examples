# 📡 MQTT Examples

A collection of practical Python examples for working with MQTT brokers, including simple pub/sub patterns, SSL connections, Google Cloud Platform (GCP) integration, HiveMQ Cloud, Sense HAT sensor publishing, and Grafana-ready data generation. The `mqtt5/` folder contains additional examples using the MQTT 5 protocol.

---

## Repository Structure

```
mqtt_examples/
├── mqtt5/                            # MQTT 5 protocol examples
├── mqtt_publisher_simple.py          # Basic MQTT publisher
├── mqtt_publisher_simple_gcp.py      # Publisher for GCP IoT Core (plain)
├── mqtt_publisher_ssl_gcp.py         # Publisher for GCP IoT Core (SSL)
├── mqtt_publisher_ssl_hivemq.py      # Publisher for HiveMQ Cloud (SSL)
├── mqtt_publisher_grafana_random.py  # Publisher with random data for Grafana
├── mqtt_subscriber_simple.py         # Basic MQTT subscriber
├── mqtt_subscriber_simple_gcp.py     # Subscriber for GCP IoT Core (plain)
├── mqtt_subscriber_ssl_gcp.py        # Subscriber for GCP IoT Core (SSL)
├── mqtt_subscriber_ssl_hivemq.py     # Subscriber for HiveMQ Cloud (SSL)
├── sensehat_mqtt.py                  # Raspberry Pi Sense HAT sensor publisher
├── docker-compose.yml                # Docker setup (e.g., local broker)
└── .gitignore
```

---

## Getting Started

### Prerequisites

- Python 3.7+
- `paho-mqtt` library

```bash
pip install paho-mqtt
```

For Sense HAT emulator support:

```bash
pip install sense_emu
```

### Running with Docker

A `docker-compose.yml` is included to quickly spin up a local MQTT broker (e.g., Mosquitto):

```bash
docker compose up -d
```

---

## Examples Overview

### Simple Publisher / Subscriber

Basic MQTT pub/sub on a local or public broker.

```bash
python mqtt_publisher_simple.py
python mqtt_subscriber_simple.py
```

### GCP using Virtual Machines

Publish and subscribe using Google Cloud Platform with Virtual Machines.

```bash
python mqtt_publisher_simple_gcp.py
python mqtt_subscriber_simple_gcp.py
```

### GCP using Virtual Machines (SSL)

Secure communication with GCP Virtual Machines using TLS/SSL certificates.

```bash
python mqtt_publisher_ssl_gcp.py
python mqtt_subscriber_ssl_gcp.py
```

### HiveMQ Cloud (SSL)

Publish and subscribe using [HiveMQ Cloud](https://www.hivemq.com/mqtt-cloud-broker/) with TLS encryption.

```bash
python mqtt_publisher_ssl_hivemq.py
python mqtt_subscriber_ssl_hivemq.py
```

> Update the HiveMQ host, username, and password inside the scripts before running.

### Grafana Random Data Publisher

Publishes randomly generated data points, suitable for testing Grafana dashboards with an MQTT datasource.

```bash
python mqtt_publisher_grafana_random.py
```

### Sense HAT Publisher

Reads temperature, humidity, and pressure from a Raspberry Pi Sense HAT emulator and publishes them to an MQTT broker in real time.

```bash
python sensehat_mqtt.py
```

### MQTT 5 Examples

The `mqtt5/` folder contains examples demonstrating MQTT 5 features such as:

- Enhanced authentication
- Message expiry intervals
- Reason codes and user properties
- Topic aliases

```bash
cd mqtt5/
# Run the specific example you want
```

---

## Configuration

Each script typically contains configuration variables at the top that you should update before running:

| Variable | Description |
|---|---|
| `BROKER` | MQTT broker hostname or IP |
| `PORT` | Broker port (default: 1883, SSL: 8883) |
| `TOPIC` | MQTT topic to publish/subscribe to |
| `USERNAME` | Broker username (if required) |
| `PASSWORD` | Broker password (if required) |

---

## Dependencies

| Package | Purpose |
|---|---|
| `paho-mqtt` | MQTT client library for Python |
| `sense_emu` | Raspberry Pi Sense HAT sensor emulator readings |

Install all at once:

```bash
pip install paho-mqtt sense_emu
```

---

## Resources

- [MQTT Protocol Specification](https://mqtt.org/)
- [MQTT 5 New Features](https://www.hivemq.com/mqtt-5/)
- [Paho MQTT Python Docs](https://eclipse.dev/paho/files/paho.mqtt.python/html/index.html)
- [HiveMQ Cloud](https://www.hivemq.com/mqtt-cloud-broker/)
- [Google Cloud Platform](https://cloud.google.com)
- [Grafana MQTT Datasource](https://grafana.com/grafana/plugins/grafana-mqtt-datasource/)

---

## Author

**dgarridouma** · [GitHub Profile](https://github.com/dgarridouma)
