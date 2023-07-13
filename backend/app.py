from flask import Flask, json,request
from matplotlib import pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import csv

# import plotly.graph_objects as go

app=Flask(__name__)


@app.route("/sales",methods=['POST'])
def sales():

    print(request.json)
    data=request.json["data"]
    time=request.json["no_of_days"]
    actual=data.copy()
    
    X = np.array(data[:-1]).reshape(-1, 1)
    y = np.array(data[1:])
    predicted=[]
    
    model = LinearRegression()
    model.fit(X, y)
    for i in range(time):

        temp=model.predict([[data[-1]]])[0]
        data.append(temp)
        predicted.append(temp)

    
    return {"actual":actual,"predicted":predicted}

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


if(__name__=="__main__"):
    app.run(debug=True)