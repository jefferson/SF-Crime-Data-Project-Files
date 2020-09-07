from kafka import KafkaProducer
import json
import time


from kafka import KafkaProducer
import json
import time

URI = "localhost:9091"
INPUT_FILE = "police-department-calls-for-service.json"
TOPIC = "service.calls"

class ProducerServer(KafkaProducer):

    def __init__(self, input_file, topic, **kwargs):
        super().__init__(**kwargs)
        self.input_file = input_file
        self.topic = topic

    #TODO we're generating a dummy data
    def generate_data(self):
        with open(self.input_file) as f:
            for line in f:
                message = self.dict_to_binary(line)
                # TODO send the correct data
                record = self.send(topic = self.topic, value = message)
                print(message)
                time.sleep(1)

    # TODO fill this in to return the json dictionary to binary
    def dict_to_binary(self, json_dict):
        return json.dumps(json_dict).encode('utf8')