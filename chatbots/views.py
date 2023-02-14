from django.shortcuts import render
from flask import Flask, render_template, request,jsonify
from chatbots.chat import get_response
from flask_cors import CORS

app= Flask(__name__)
CORS(app)


@app.route("/predict",methods=["POST"])
def predict():
        text= request.get_json().get("message")
        response= get_response(text)
        message ={"answer":response}
        return render(jsonify(message))

