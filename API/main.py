from fastapi import FastAPI
from confluent_kafka import Producer, Consumer, KafkaException

app = FastAPI()

# Конфигурация Kafka
KAFKA_BROKER = "localhost:9092"
TOPIC = "example-topic"

# Kafka Producer
producer = Producer({'bootstrap.servers': KAFKA_BROKER})

@app.get("/send")
def send_message(message: str):
    try:
        producer.produce(TOPIC, message.encode('utf-8'))
        producer.flush()
        return {"status": "Message sent", "message": message}
    except Exception as e:
        return {"status": "Error", "message": str(e)}

# Kafka Consumer
@app.get("/receive")
def receive_message():
    consumer = Consumer({
        'bootstrap.servers': KAFKA_BROKER,
        'group.id': 'example-group',
        'auto.offset.reset': 'earliest'
    })
    consumer.subscribe([TOPIC])
    messages = []
    try:
        for _ in range(5):  # Получить 5 сообщений
            msg = consumer.poll(1.0)
            if msg is None:
                break
            if msg.error():
                if msg.error().code() == KafkaException._PARTITION_EOF:
                    break
                else:
                    raise KafkaException(msg.error())
            messages.append(msg.value().decode('utf-8'))
        consumer.close()
        return {"messages": messages}
    except Exception as e:
        return {"status": "Error", "message": str(e)}
