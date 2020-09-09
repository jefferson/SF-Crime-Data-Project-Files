import producer_server

FILE = "police-department-calls-for-service.json"

def run_kafka_server():

    producer = producer_server.ProducerServer(
        input_file=FILE,
        topic="service.calls",
        bootstrap_servers="localhost:9091",
        client_id=None
    )

    return producer


def feed():
    producer = run_kafka_server()
    producer.generate_data()


if __name__ == "__main__":
    feed()