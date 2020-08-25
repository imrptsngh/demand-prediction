from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd


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

@app.route('/graphs')
def graphs():
    return render_template('graphs.html')


global df
df = pd.read_csv('final.csv', index_col="Unnamed: 0")

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        
        # Fetched date
        data = request.form
        date = data.get("Date")
        
        # Parsed date
        mod_date = date
        parsed_date = pd.to_datetime(mod_date,utc=True)
        
        # Fetching pred 
        predictions_dict = df.loc[str(parsed_date)].to_dict()
    
    return render_template("result.html", prediction=predictions_dict)


if __name__ == '__main__':
    # app.host = '0.0.0.0', port = 5000
    app.run(debug=True, use_reloader=False)
