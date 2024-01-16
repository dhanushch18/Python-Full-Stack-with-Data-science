from flask import Flask, render_template, request, redirect, url_for

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/validate',methods = ["POST"])
def validate():
    if request.method == 'POST' and request.form['pass'] =='jtp':
        return redirect(url_for("success"))
    return redirect(url_for("login"))

@app.route('/success')
def success():
    return "logged in successfully"
