from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
def customer():
    return render_template('customer.html')

@app.route('/success',methods =['POST','GET'])
def print_data():
    if request.method == 'POST':
        result = request.form
        return render_template("result_data.html",result=result)
