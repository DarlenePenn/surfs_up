from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello world'
@app.route('/')   
def skill_drill():
    return 'I am learning new things'