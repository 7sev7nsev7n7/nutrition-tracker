# main.py

'''
main program to run and execute flask site
'''

from flask import Flask, render_template, request, redirect
from login import login
app = Flask(__name__,static_url_path='')

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/login', methods=['GET','POST'])
def userLogin():
    username = request.form['username']
    password = request.form['password']
    if login(username, password):
        print("success!")
        return redirect('/home')
    else:
        return redirect('/')

@app.route("/home")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run()
