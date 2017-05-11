from flask import Flask
from flask import abort, redirect, url_for, request, render_template
from models import *
from dao.user_dao import user_dao

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/', methods=['POST', 'GET'])
def index():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if isValid(username, password):
            print 'app.py : in index() method'
            return redirect(url_for('home'))
        else:
            error = 'Error: Invalid username/password'
            return render_template('index.html', error=error)
    else:
        return render_template('index.html')

@app.route('/home', methods=['POST', 'GET'])
def home():
    return render_template('home.html')

def isValid(username, password):
    print 'app.py : in isValid() method'
    dao = user_dao()
    user = dao.select(username)
    return password == user.getPassword()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
