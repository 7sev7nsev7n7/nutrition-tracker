# main.py

'''
main program to run and execute flask site
'''

from flask import Flask, render_template, request, redirect, make_response
from login import login
from register import register
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
            print("success!")
            resp = make_response(redirect('/home'))
            resp.set_cookie('username',value=username)
            print(request.cookies.get('user'))
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
            print("success!")
            return redirect('/')
        else:
            return redirect('/register')
    pass

@app.route("/home") # user home page
def home():
    return render_template("home.html", username = request.cookies.get('username'))

if __name__ == "__main__":
    app.run()
