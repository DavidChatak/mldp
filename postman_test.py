# from typing_extensions import runtime
import re
from flask import Flask, json, request,jsonify, render_template
import pandas as pd
import joblib

model = joblib.load("model.pkl")
columns = joblib.load("columns.pkl")

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return "Flask server is UP & RUNNING"

@app.route("/postman", methods=['GET', 'POST'])
def pred():
    if request.method == 'POST':
        data = {
            "TV":[request.json["TV"]],
            "radio":[request.json["radio"]],
            "newspaper":[request.json["newspaper"]]
            }
        df = pd.DataFrame(data).reindex(columns=columns)
        result=list(model.predict(df))
        return {"post method":str(result)}
    return "GET metot"

@app.route("/predict", methods=['GET', 'POST'])
def predict():

    if request.method == 'POST':
        # data = request.json
        # df = pd.DataFrame(data).reindex(columns=columns)
        # result=list(model.predict(df))
        # return jsonify({"result":str(result)})
        data = {
            "TV":[request.form["TV"]],
            "radio":[request.form["radio"]],
            "newspaper":[request.form["newspaper"]]
            }
        print("*****************debugging*****************")
        print(data)
        print("*****************debugging*****************")
        df = pd.DataFrame(data).reindex(columns=columns)
        result=list(model.predict(df))
        print("predicted sales: ", result)
        # return {"result":str(result)}
        return render_template("result.html", result=result)
    return render_template("predict.html")

    # return "predict sales"

if __name__ == '__main__':
    
    app.run(debug=True, port=80)