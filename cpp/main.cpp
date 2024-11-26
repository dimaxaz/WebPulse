#include <iostream>
#include <librdkafka/rdkafkacpp.h>

int main() {
    std::cout << "C++ Kafka Producer Example" << std::endl;

    std::string brokers = "localhost:9092";
    std::string topic = "example-topic";

    RdKafka::Conf* conf = RdKafka::Conf::create(RdKafka::Conf::CONF_GLOBAL);
    conf->set("bootstrap.servers", brokers, nullptr);

    RdKafka::Producer* producer = RdKafka::Producer::create(conf, nullptr);

    if (!producer) {
        std::cerr << "Failed to create producer" << std::endl;
        return 1;
    }

    for (int i = 0; i < 10; i++) {
        std::string message = "Message #" + std::to_string(i);
        producer->produce(topic, RdKafka::Topic::PARTITION_UA, RdKafka::Producer::RK_MSG_COPY,
            const_cast<char*>(message.c_str()), message.size(), nullptr, 0, 0, nullptr, nullptr);
        std::cout << "Sent: " << message << std::endl;
    }

    producer->flush(1000);
    delete producer;
    delete conf;

    return 0;
}
