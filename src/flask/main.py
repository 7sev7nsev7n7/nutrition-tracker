# main.py

'''
main program to run and execute flask site
'''

from flask import Flask, render_template, jsonify, request, redirect, url_for
app = Flask(__name__,static_url_path='')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run()
