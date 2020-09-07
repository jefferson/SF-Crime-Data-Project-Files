# SF-Crime-Statistics

## Project Overview:
In this project, you will be provided with a real-world dataset, extracted from Kaggle, on San Francisco crime incidents, and you will provide statistical analyses of the data using Apache Spark Structured Streaming. You will draw on the skills and knowledge you've learned in this course to create a Kafka server to produce data, and ingest data through Spark Structured Streaming.

You can try to answer the following questions with the dataset:

What are the top types of crimes in San Fransisco?
What is the crime density by location?

## Questions:
1. How did changing values on the SparkSession property parameters affect the throughput and latency of the data?

Kafka emits at the rate of 1/second and with the current sparkSession allowing maxOffsetsPerTrigger=200.

2. What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?

The poperties are:
- spark.sql.shuffle.partitions
- spark.streaming.kafka.maxRatePerPartition
- spark.default.parallelism

To determine if we have reached the optimal group of the above property values we will need to reach the largest possible processedRowsPerSecond.

## Environment Prerequisites:

1. Spark 2.4.3
2. Scala 2.11.x
3. Java 1.8.x
4. Kafka build with Scala 2.11.x
5. Python 3.6.x or 3.7.x

## How to run the project:

0. Unzip ```police-department-calls-for-service.7z``` to ```police-department-calls-for-service.json```

1. Run `./start.sh` to install project requirements. If you use **pip** rather than conda, then use `pip install -r requirements.txt`

2. Start **zookeeper server**: `/usr/bin/zookeeper-server-start config/zookeeper.properties`

3. Open a new terminal and start **kafka server**: `/usr/bin/kafka-server-start.sh config/server.properties`

4. Open a new terminal and run `python kafka_server.py`

5. Open a new terminal and start **kafka-consumer-console**: `/usr/bin/kafka-consumer-console --bootstrap-server localhost:9091 --topic service.calls --from-beginning`

6. Run **spark job**: `spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.3.4 --master local[*] data_stream.py`

