# main.py

'''
main program to run and execute flask site
'''

from flask import Flask, render_template, request, redirect, make_response
from login import login
app = Flask(__name__,static_url_path='')

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/login', methods=['POST'])
def userLogin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if login(username, password):
            print("success!")
            resp = make_response("Success")
            resp.set_cookie('username',username)
            return redirect('/home')
        else:
            return redirect('/')

@app.route("/home")
def home():
    return render_template("home.html", user = request.cookies.get('username'))

if __name__ == "__main__":
    app.run()
