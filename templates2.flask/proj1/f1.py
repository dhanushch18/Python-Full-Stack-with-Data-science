
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def message():
      return render_template('message.html')
