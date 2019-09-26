from flask import Flask, request
app = Flask(__name__)


cache = {'val': 'foo'}


@app.route('/')
def get():
    return cache['val']


@app.route('/', methods=['POST'])
def set():
    cache['val'] = request.json['val']
    return '\n'
