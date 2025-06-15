from flask_cors import CORS
from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


CORS(app)