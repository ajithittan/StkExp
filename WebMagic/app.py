from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World of flask fsadfas"

@app.route('/test/<int:task_id>')
def nextfunction(task_id):
    print("task_id",task_id)
    return "Hello World of flask test"
