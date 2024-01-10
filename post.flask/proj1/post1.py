from flask import*

app = Flask(__name__)

@app.route('/login',methods=['POST'])
def login():
    uname=request.form['uname']
    password=request.form['pass']
    if uname=="ayush" and password=="google":
        return "Welcome %s" %uname
