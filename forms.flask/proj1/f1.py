from flask import Flask, render_template

app=Flask(__name__)
@app.route("/form")
def forms():
    return render_template('forms.html')

