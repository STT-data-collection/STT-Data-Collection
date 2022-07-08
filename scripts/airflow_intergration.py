from airflow import DAG
from airflow.operators.python import PythonOperator, ShortCircuitOperator

from KafkaClient import KafkaClient
from AWSClient import AWSClient
from logger_creator import CreateLogger

from datetime import datetime
import pandas as pd
from io import StringIO

# Configuration Variables
csv_file_name = 'audio_descriptions.csv'
bucket_name = 'unprocessed-stt-audio'
kafka_servers = [
    '192.168.0.106:9092',
]

# Creating a Consumer using for the KafkaClient
kf_client.create_consumer(
    topics='Text-Audio-input',
    offset='earliest',
    auto_commit=True,
    group_id='airflow-text-audio-input-reader',
    value_deserializer=kf_client.get_json_deserializer(),
    timeout=1000
)

# Creating a AWSClient for uploading(storing) the Data
aws_client = AWSClient()

# DECLARING Airflow DAG CONFIGURATION
DAG_CONFIG = {
    'depends_on_past': False,
    'start_date': datetime(2022, 1, 1),
    'email': ['melakuandarge100@gmail.com'],
    'email_on_failure': True,
    'schedule_interval': '0 0 0/1 ? * * *',
}
# Kafka Data Reader


def _consume_kafka_data(ti):
    try:
        data = kf_client.get_data()

        if(len(data) > 0):
            ti.xcom_push(key='kafka_data', value=data)

            logger.info(
                f'SUCCESSFULLY LOADED {len(data)} DATA VALUES FROM KAFKA\'s "Text-Audio-input" Topic')

            return True

        return False

    except Exception as e:
        logger.exception('FAILED TO READ DATA FROM KAFKA SERVERS')
        return False

