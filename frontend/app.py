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


global loaded_model
loaded_model = pickle.load(open("new_model.sav", "rb"))


@app.route('/result', methods=['POST'])
def result():

    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict = np.array(to_predict_list).reshape(1, 10)
        result = loaded_model.predict(to_predict)
        resultarr = list(result[0])
        tload = "{:.2f}".format(float(resultarr[0]))
        price = "{:.2f}".format(float(resultarr[1]))
        prediction = {"price": price, "load": tload}
    return render_template("result.html", prediction=prediction)


if __name__ == '__main__':
    # app.host = '0.0.0.0', port = 5000
    app.run(debug=True, use_reloader=False)
