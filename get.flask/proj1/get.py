

from flask import*
app=Flask(__name__)

@app.route('/login',methods=['GET'])
def login():
    uname=request.args.get('uname')
    password=request.args.get('pass')
    if uname=="ayush" and password =="google":
        return "Welcome %s" %uname
