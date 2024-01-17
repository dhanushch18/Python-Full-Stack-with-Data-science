#In the web applications, there are scenarios where the developer might need to flash the messages to provide feedback to the users for the behavior of the application in different cases.

#Flask provides the flash() method, in the same way, the client-side scripting language like JavaScript uses the alerts or the python GUI framework Tkinter uses the dialogue box or the message box.

#The flash() method is used to generate informative messages in the flask. It creates a message in one view and renders it to a template view function called next.


from flask import *
app = Flask(__name__)
app.secret_key = "abc"

@app.route('/index')
def home():
    return render_template("index.html")

@app.route('/login',methods = ["GET","POST"])
def login():
    error = None;
    if request.method == "POST":
        if request.form['pass'] != 'jtp':
            error = "invalid password"
        else:
            flash("you are successfuly logged in")
            return redirect(url_for('home'))
    return render_template('login.html',error=error)
