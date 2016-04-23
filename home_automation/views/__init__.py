from flask import Blueprint

app = Blueprint('', __name__)
@app.route('/')
def hello_world():
    return 'Hello World!'