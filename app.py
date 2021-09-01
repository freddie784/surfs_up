from flask import Flask

app = Flask(__name__)

@app.route('/')
def helloWorld():
    return 'Hello World'
@app.route("/another1")
def another1():
    return 'Another World'
    