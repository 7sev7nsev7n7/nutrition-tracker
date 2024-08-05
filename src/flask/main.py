# main.py

'''
main program to run and execute flask site
'''

from flask import Flask, render_template, request, redirect, make_response
from login import login
from register import register, unregister
from auth import auth
from usercheck import check
from userdata import readData, updateData
import json
import os

try:
    os.mkdir("data") # make data directory if it does not already exist
except FileExistsError:
    pass
    
app = Flask(__name__,static_url_path='')

@app.route("/", methods=['GET']) # main page
def index():
    return render_template("index.html")

@app.route('/login', methods=['POST']) # login http post
def userLogin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if login(username, password):
            print("login success")
            resp = make_response(redirect('/home'))
            resp.set_cookie('username',value=username, secure=True)
            resp.set_cookie('password',value=password, secure=True)
            return resp
        else:
            return redirect('/')

@app.route('/register', methods=['GET']) # registration page
def userRegister():
    return render_template("register.html")

@app.route('/postregister',methods=['POST']) # registration http post
def postRegister():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if register(username, password):
            print("registration success")
            return redirect('/')
        else:
            return redirect('/register')
    pass

@app.route('/deleteaccount', methods=['GET']) # account deletion page
def userDelete():
    return render_template("delete.html")

@app.route('/postdeleteaccount', methods=['POST']) # account deletion http post
def postDelete():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if unregister(username, password):
            print("account deletion success")
            return redirect('/')
        else:
            return redirect('/home')
    pass

@app.route("/home") # user home page
def home():
    cu = request.cookies.get('username') # cookie username
    cp = (request.cookies.get('password')) # cookie password
    if auth(cu, cp): # on-page authentication to ensure correct logins, and to not expose user information
        data = json.loads(readData(cu))
        return render_template("home.html", username = cu, password = cp, data = data)
    else:
        return redirect('/')

@app.route("/updateinfo", methods=['POST'])
def updateinfo():
    if request.method ==  'POST':
        pass


if __name__ == "__main__":
    app.run()
