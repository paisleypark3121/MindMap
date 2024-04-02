import os
from dotenv import load_dotenv

import networkx as nx
from pyvis.network import Network
import matplotlib.pyplot as plt

from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from MindMapGenerator import *


load_dotenv()

app = Flask(__name__, static_folder='static', static_url_path='/')
CORS(app)

default_model='gpt-3.5-turbo-0613'
#default_model='gpt-4-0613'

@app.route("/")
def home():
    return "Hello World"
    

@app.route("/mm", methods=["POST"])
def mm():
    
    api_key_received = request.headers.get('X-API-Key')
    if api_key_received != os.environ.get('API_KEY'):
        abort(401) 

    data = request.get_json()

    language='en'
    if 'language' in data:
        language = data['language']
    #print(language)

    if 'message' in data:
        message = data['message']
    if message is None:
        return jsonify({"error": "No messages available"}), 404
    #print(message)

    type='small'
    if 'type' in data:
        type = data['type']
    #print(type)

    physics=False
    if 'physics' in data:
        physics = data['physics']
    #print(physics)

    nt = generateInteractiveMindMap(
        language=language,
        type=type,
        text=message,
        physics=physics,
        temperature=0,
        model_name=default_model)

    html = nt.generate_html()
    #print(html)

    return jsonify({"success": True, "html": html}), 200

if __name__ == "__main__":
    app.run(debug=True)
    #app.run("0.0.0.0")