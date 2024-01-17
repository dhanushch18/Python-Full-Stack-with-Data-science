""""
Flask-Mail Extension
Considering the fact that flask is a micro framework, it has its limitations in providing the facilities to the developer. Although, there are several extensions to the flask like Mail, WTF, SQLite, SQLAlchemy, etc. which facilitates the developer to provide some basic facilities to the user.

A web application must be capable of sending emails to users. The flask-mail extension provides the simple interface for the developer and the email server to send the email through the web application.


SN	Parameter	Description
1	MAIL_SERVER	It represents the name or IP address of the email server. The default is localhost.
2	MAIL_PORT	It represents the port number of the server. Default port number is 25.
3	MAIL_USE_TLS	It is used to enable or disable the transport security layer description. The default is false.
4	MAIL_USE_SSL	It is used to enable or disable the secure socket layer description. The default value is false.
5	MAIL_DEBUG	It is used to provide the debug support to the mail application. The default value is None.
6	MAIL_USERNAME	It represents the user name of the sender. The default value is None.
7	MAIL_PASSWORD	It represents the password of the server email id. The default value is None.
8	MAIL_DEFAULT_SENDER	It is used to set the default sender id for the multiple emails. The default value is None.
9	MAIL_MAX_EMAILS	It is used to set the maximum number of email to be sent. The default value is None.
10	MAIL_SUPPRESS_SEND	Sending the mail is suppressed if the app.testing is set to the true.
11	MAIL_ASCII_ATTACHMENTS	If it is set to true, attached file names are converted to ASCII. The default is False.
"""
from mailbox import Message
from random import randint

import Mail as Mail
from flask import Flask, render_template, request

app = Flask(__name__)
mail = Mail(app)

app.config["MAIL_SERVER"]='smtp.gmail.com'
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] = 'username@gmail.com'
app.config['MAIL_PASSWORD'] = '*************'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)
otp = randint(000000,999999)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/verify',methods = ["POST"])
def verify():
    email = request.form["email"]

    msg = Message('OTP',sender = 'username@gmail.com', recipients = [email])
    msg.body = str(otp)
    mail.send(msg)
    return render_template('verify.html')

@app.route('/validate',methods=["POST"])
def validate():
    user_otp = request.form['otp']
    if otp == int(user_otp):
        return "<h3>Email verified successfully</h3>"
    return "<h3>failure</h3>"
