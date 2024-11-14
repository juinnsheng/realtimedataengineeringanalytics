# BDAA Group - Docker and Druid Setup Guide

## Table of Contents
1. [Setup for Mac OS Users](#setup-for-mac-os-users)
2. [Docker Desktop Configuration](#docker-desktop-configuration)
3. [Setup Druid Environment](#setup-druid-environment)
4. [Running Containers](#running-containers)
5. [How to Run Apache Kafka](#how-to-run-apache-kafka)
6. [Accessing Druid, Prometheus, Grafana, and Superset](#accessing-druid-prometheus-grafana-and-superset)
7. [Adding More Monitoring Metrics](#adding-more-monitoring-metrics)
8. [Troubleshooting with Druid Doctor](#troubleshooting-with-druid-doctor)

---

## Setup for Mac OS Users

### Configure `.zshrc` for Docker Compatibility
To ensure compatibility between Docker and your system, configure the Docker platform by adding the following to your `.zshrc` file:

```bash
nano ~/.zshrc
export DOCKER_DEFAULT_PLATFORM=linux/amd64
source ~/.zshrc

Install Docker Desktop
Sign Up for Docker Hub: Docker Hub
Install Docker Desktop: Docker Desktop
Login with your Docker Hub credentials.
Docker Desktop Configuration
Open Settings → Resources → Advanced → Set Memory Limit to 7.5 GB (or adjust based on your system's RAM).
Open Network → Enable Host Networking. This is required for Port Forwarding, which allows Docker containers to communicate with your local host machine.
Refer to the following resources for more information on Docker networking:

Docker Networking - Standalone Tutorial
Host Networking in Docker
Setup Druid Environment

Obtain the Druid setup from Druid Docker Environment.
Modify the environment configuration to match your setup.
If you want to emit additional metrics, refer to Druid Metrics Documentation to add them to your environment configuration. These metrics will be emitted to Prometheus, where they can be monitored in Grafana.
Running Containers

After configuring your environment, you can start your containers based on your system's available resources.

For High-performance Laptops (8GB RAM and above):
Run all containers at once using the following command:

docker-compose up -d
Wait for a few minutes for all containers to initialize.

For Laptops with 8GB RAM or Below:
To manage your system’s resources, start containers separately:

First, run Kafka, Druid, and Superset containers.
After they are running, start Druid, Grafana, and Prometheus containers separately.
Docker Image Login:
If prompted, log in with your Docker Hub credentials to download necessary Docker images like druid-exporter.

To view the running containers, use the following command:

docker ps
How to Run Apache Kafka

Kafka requires Zookeeper, Producer, and Consumer to work. Zookeeper must be healthy for Kafka to function correctly.

Kafka Setup Commands:
Run the following commands to create a Kafka topic and start consuming data from it:
docker exec --workdir /opt/kafka/bin/ -it kafka_broker sh
./kafka-topics.sh --bootstrap-server kafka_broker:19092,kafka_broker_1:19092 --create --topic ecommerce9
./kafka-console-consumer.sh --bootstrap-server kafka_broker:19092,kafka_broker_1:19092 --topic ecommerce9 --from-beginning --partition 0
Activate your Python virtual environment and run your Python Producer:
source .venv/bin/activate
python Producer.py
Important:
Ensure that the Producer’s topic matches the Kafka topic. For instance, if the topic is ecommerce9, your Producer should also use ecommerce9.

Accessing Druid, Prometheus, Grafana, and Superset

You can access the following services locally once the containers are running:

Druid: localhost:8888
Prometheus: localhost:9090 (No metrics will appear initially.)
Prometheus Targets: localhost:9090/targets (Ensure that the Druid Exporter is up and running.)
Grafana: localhost:3000
Superset: localhost:8088
Login Details:
Superset:
Username: user
Password: 333666
Grafana:
Username: user
Password: SomePassword
Adding More Monitoring Metrics

To add more metrics to monitor, you can use the following query in Prometheus:

druid_emitted_metrics{metric_name="query-cpu-time", services="broker"}
These metrics will be collected by Prometheus and displayed in Grafana.


