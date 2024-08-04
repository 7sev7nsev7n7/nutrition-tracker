# main.py

'''
main program to run and execute flask site
'''

from flask import Flask, render_template, jsonify, request
app = Flask(__name__,static_url_path='')

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
