from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World of flask fsadfas"

@app.route('/test/<int:task_id>')
def nextfunction(task_id):
    print("task_id",task_id)
    return render_template('main.html')

@app.route('/testajax')
def json():
    return render_template('main.html')

@app.route('/background_process_test')
def background_process_test():
    print ("Hello")
    return ("nothing")
