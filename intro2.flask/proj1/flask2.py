from flask import Flask
app = Flask(__name__)

@app.route('/home')
def home():
    return "hello, welcome to our website";
