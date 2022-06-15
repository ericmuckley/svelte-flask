from flask import Flask, render_template, send_from_directory
import random

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route("/getrandomnumber")
def getrandomnumber():
    return str(random.randint(0, 10000))



@app.route("/s")
def base():
   """Redirect to main svelte page"""
   return send_from_directory('client/public', 'index.html')


@app.route("/<path:path>")
def staticpath(path):
   """Read path to all static svelte files"""
   return send_from_directory('client/public', path)