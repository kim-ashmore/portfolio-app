from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return "hellow world"


@app.route('/index')
def index():
    # return 'Hello, World!'
    return render_template("index.html")
