from flask import Flask, make_response, session, render_template

app = Flask(__name__)
app.secret_key = "abc"

@app.route('/')
def home():
    res = make_response("<h4>session variable is set, <a href='/get'>Get Variable</a></h4>")
    session['response']='session#1'
    return res;

@app.route('/get')
def getVariable():
    if 'response' in session:
        s = session['response'];
        return render_template('getsession.html',name = s)

