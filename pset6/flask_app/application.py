from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tim')
def tim():
    return render_template('tim.html')

@app.route('/login')
def login():
    return render_template('login.html')
