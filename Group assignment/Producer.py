import json
from faker import Faker
from kafka import KafkaProducer
import time
import random

# Create a Faker instance globally
faker = Faker()

# Function to generate fake data
def generate_data():
    data = {
        'user_id': random.getrandbits(32),
        'event_type': random.choice(['click', 'view', 'purchase']),
        'country': faker.country_code(),
        'city': faker.city(),
        'device': random.choice(['mobile', 'desktop', 'tablet']),
        'product_id': random.getrandbits(32),
        'price': round(random.uniform(5, 500), 2),
        'quantity': random.randint(1, 100),
        'timestamp': round(time.time())
    }

    return data

# Main function to send data to Kafka
if __name__ == '__main__':
    topic_name = 'ecommerce10'
    producer = KafkaProducer(
        bootstrap_servers = ['localhost:29092', 'localhost:39092'],
        api_version=(3,8,1),
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    count = 0
    while count < 10:
        # Generate random data
        rec = generate_data()
        # Send the record to Kafka
        producer.send(topic_name, value=rec)
        count += 1
        print(f'Record[{count}]: {rec}')
        time.sleep(1)
        # Ensure data is flushed to Kafka
        producer.flush()
