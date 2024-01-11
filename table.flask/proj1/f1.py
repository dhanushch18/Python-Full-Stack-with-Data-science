from flask import Flask, render_template

app=Flask(__name__)




@app.route("/table/<int:num>")
def table (num):
    return render_template('table.html',n=num)
