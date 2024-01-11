
from flask import Flask
app=Flask(__name__)
@app.route('/')
def message():
    return "<html><body><h1>Hi,Welcome...!</h1></body></html>"
