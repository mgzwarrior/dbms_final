from flask import Flask
from flask import abort, redirect, url_for, request, render_template
from models.user import User
from dao.user_dao import UserDAO

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/', methods=['POST', 'GET'])
def index():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if isValid(username, password):
            return redirect(url_for('home', username=username))
        else:
            error = 'Error: Invalid username/password'
            return render_template('index.html', error=error)
    else:
        return render_template('index.html')

@app.route('/create', methods=['POST', 'GET'])
def create():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        if password != confirm_password:
            error = 'Error: Passwords do not match'
            return render_template('create.html', error=error)
        if insert(username, password):
            return redirect(url_for('home', username=username))
        else:
            error = 'Error: Username ' + username + ' is taken'
            return render_template('create.html', error=error)
    else:
        return render_template('create.html')

@app.route('/home/<username>', methods=['POST', 'GET'])
def home(username):
    return render_template('home.html', username=username)

@app.route('/logout')
def logout():
    return redirect(url_for('index'))

def isValid(username, password):
    dao = UserDAO()
    user = dao.select(username)
    if user == None:
        return False
    return password == user.getPassword()

def insert(username, password):
    dao = UserDAO()
    user = dao.insert(User(username, password))
    if user == None:
        return False
    return username == user.getUsername() and password == user.getPassword()
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
