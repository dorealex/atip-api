import pandas as pd
from flask import Flask, jsonify, request
import joblib
import requests

# load model
model = joblib.load('model/model_full_June2020.jl')

# app
app = Flask(__name__)

# routes
@app.route('/api/', methods=['POST'])

def api():
    # get data
    print("request received")
    print(request)
    data = request.get_json(force=True)
    #req = data['text']
    #what = data['what']
    return jsonify(data)
if __name__ == '__main__':
    app.run(port = 5000, debug=True)