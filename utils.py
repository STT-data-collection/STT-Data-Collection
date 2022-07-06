import json

##########################################
# producer = KafkaProducer(
#     bootstrap_servers=['192.168.0.106:9092'],
#     value_serializer=json_serializer,
#     partitioner=get_partition
#     )
###############################################


def json_serializer(data):
    return json.dumps(data).encode('utf-8')


def get_partition(key,all,available):
    return 0

