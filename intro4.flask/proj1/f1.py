
from flask import Flask, redirect, url_for

app=Flask(__name__)

@app.route('/admin')
def admin():
    return 'admin'

@app.route('/librarion')
def librarion():
    return 'librarion'

@app.route('/student')
def student():
    return 'student'

@app.route('/user/<name>')
def user(name):
    if name=='admin':
        return redirect(url_for('admin'))
    if name=='librarion':
        return redirect(url_for('librarion'))
    if name=='student':
        return redirect(url_for('student'))


