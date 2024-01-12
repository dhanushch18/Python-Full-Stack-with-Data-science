from flask import Flask, render_template

app=Flask(__name__)

@app.route("/table")
def table():
    return render_template('table.html')
