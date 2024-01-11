from flask import *
app = Flask(__name__)

@app.route('/user/<uname>')
def message(uname):
      return render_template('message.html',name=uname)
