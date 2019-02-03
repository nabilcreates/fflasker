from flask import *

app = Flask(__name__)

auth_users = []

@app.route('/')
def hello():
    return 'hey'