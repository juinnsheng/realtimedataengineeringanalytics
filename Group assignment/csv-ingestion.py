import csv
import json
from kafka import KafkaProducer
import time


def ingest_csv_to_kafka(csv_file, topic_name, bootstrap_servers):
    producer = KafkaProducer(
        bootstrap_servers=bootstrap_servers,
        api_version=(3, 8, 1),
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    with open(csv_file, mode='r') as file:
        csv_reader = csv.DictReader(file)
        count = 0
        for row in csv_reader:
            producer.send(topic_name, value=row)
            count += 1
            print(f'Record[{count}]: {row}')
            time.sleep(1)  

        producer.flush()
        print(f"Total records sent: {count}")

if __name__ == '__main__':
    csv_file_path = '/Users/juinnshengna/Desktop/Group assignment/test.csv'
    
    # Kafka topic name
    kafka_topic = 'test2'

    # Kafka bootstrap servers
    kafka_servers = ['localhost:29092', 'localhost:39092']

    # Call the function to ingest data
    ingest_csv_to_kafka(csv_file_path, kafka_topic, kafka_servers)
