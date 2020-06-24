# Proton JS - Proton.py
# by Acropolis Point

# module imports
import os
# import modules from bigger modules
from flask import Flask, jsonify, request, render_template # should we just do import *?

app = Flask(__name__)

@app.route('/new', methods=['POST'])

# new() function definition
def new():
    os.system("python3 window.py " + request.get_data(as_text = True))
    return 'OK', 200

@app.route('/shell', methods=['POST'])

# shell() function definition
def shell():
    os.system(request.get_data(as_text = True))
    return 'OK', 200
