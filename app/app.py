from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "changes made successfully with commit code, doesn't changed in server"


