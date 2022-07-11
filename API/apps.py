import os
import json
import logging
from flask import Flask, app, request
from flask_cors import CORS, cross_origin
import numpy as np


app = Flask(__name__)
cors = CORS(app)

TEXT_TOPIC = "spark-transformed-text"
TEXT_AUDIO_PAIR_TOPIC = "text.audio.pair"
BROKER_ADDRESS = 'localhost:39092'

try:
        producer = KafkaProducer(bootstrap_servers=BROKER_ADDRESS,
                                 value_serializer=lambda x: dumps(x).encode('utf-8'))
        consumer = KafkaConsumer(TEXT_TOPIC,
                                 bootstrap_servers=BROKER_ADDRESS,
                                 auto_offset_reset='earliest',
                                 enable_auto_commit=False,
                                 value_deserializer=lambda x: loads(x.decode('utf-8')))
except NoBrokersAvailable:
        print("NoBrokersAvailable")

@app.route('/get-text', methods=["GET"])
def get_text():
        print("sending text")
        try:
            for s in consumer:
                print(s.value)
                article = s.value
                return jsonify(text=article)
        except NameError:
            print("Consumer not init")
            return 404

@app.route('/send-audio', methods=["POST"])
def publish_text_audio_pair():
        audio = request.files['audio']
        article = audio.filename
        audio = extract_audio(audio)
        print(audio.shape)
        audio = audio.tolist()
        id = get_uuid()
        data = {
            "id": id,
            "article": article,
            "audio": audio
        }
        try:
            res = producer.send(TEXT_AUDIO_PAIR_TOPIC, value=data)
            print(res)
        except NameError:
            print("Producer not created")

        # pprint(data)

        return "200"

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
