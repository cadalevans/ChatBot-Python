import json
import numpy
import pickle
import random
import nltk
from nltk.stem import WordNetLemmatizer
import numpy as np
import tensorflow

from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from tensor_flow import TensorFlow
from flask import Flask, request, jsonify

resp = TensorFlow(intents="intents.json")
app = Flask(__name__)


@app.route('/', methods=['POST'])
def chat():
    tag, data = resp.response(request.json['message'])
    response_dto = dict()
    response_dto["type"] = tag
    if tag == "riddles":
        response_data = dict()
        response_data["question"] = data["question"]
        response_data["answer"] = data["answer"]
        response_dto["data"] = response_data
    else:
        response_data = dict()
        response_data["message"] = data
        response_dto["data"] = response_data

    response = jsonify(response_dto)
    response.status_code = 200
    return response


if __name__ == '__main__':
    app.run(host='localhost', port=8000, debug=True)




