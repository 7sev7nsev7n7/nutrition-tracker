# main.py

'''
main program to run and execute flask site
'''

from flask import Flask, render_template, request, redirect, make_response
from login import login
from register import register
from auth import auth
from usercheck import check
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
            print("registration succes")
            return redirect('/')
        else:
            return redirect('/register')
    pass

@app.route("/home") # user home page
def home():
    cu = request.cookies.get('username')
    cp = (request.cookies.get('password'))
    if auth(cu, cp): # on-page authentication to ensure correct logins, and to not expose user information
        return render_template("home.html", username = cu, password = cp)
    else:
        return redirect('/')

if __name__ == "__main__":
    app.run()
