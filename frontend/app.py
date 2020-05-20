from flask import Flask, render_template, request
import pickle
import numpy as np



app = Flask(__name__, template_folder='templates', static_folder='static')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/prediction')
def prediction():
    return render_template('prediction.html')