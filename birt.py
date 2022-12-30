from flask import (Flask, render_template)

app = Flask(__name__)

@app.route("/")
def welcome():
    return  render_template('index.html')


@app.route("/base")
def base():
    return  render_template('base.html')

@app.route("/login")
def login():
    return  render_template('login.html')
