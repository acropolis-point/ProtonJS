import os
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route('/new', methods=['POST'])
def new():
    os.system("python3 window.py " + request.get_data(as_text = True))
    return 'OK', 200

@app.route('/shell', methods=['POST'])
def shell():
    os.system(request.get_data(as_text = True))
    return 'OK', 200