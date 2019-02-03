from flask import *

app = Flask(__name__)

auth_users = []

@app.route('/')
def hello():
    user = request.args.get('key')
    
    if str(user) in auth_users:
        return f'Authorised'
    else:
        return 'False, make GET request to /create/<your_key>'

@app.route("/create/<newkey>")
def data(newkey):
    newkey = request.view_args['newkey']
    auth_users.append(newkey)
    return f'Created, {newkey}'