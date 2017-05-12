from flask import Flask
from flask import abort, redirect, url_for, request, render_template
from models.user import User
from models.student import Student
from dao.user_dao import UserDAO
from dao.student_dao import StudentDAO

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
        if insertUser(username, password):
            return redirect(url_for('home', username=username))
        else:
            error = 'Error: Username ' + username + ' is taken'
            return render_template('create.html', error=error)
    else:
        return render_template('create.html')

@app.route('/home/<username>', methods=['POST', 'GET'])
def home(username):
    dao = StudentDAO()
    students = dao.selectAll()
    return render_template('home.html', username=username, students=students)

@app.route('/logout')
def logout():
    return redirect(url_for('index'))

@app.route('/insert-student', methods=['POST', 'GET'])
def insertStudent():
    if request.method == 'POST':
       student_id = request.form['student_id']
       major = request.form['major']
       minor = request.form['minor']
       name = request.form['name']
       phone = request.form['phone']
       street = request.form['street']
       city = request.form['city']
       state = request.form['state']
       zip_code = request.form['zip_code']
       student = Student(student_id, major, minor, name, phone, street, city, state, zip_code)
       if insertStudent(student):
           return redirect(url_for('home'))
       else:
           error = 'ERROR'
           return render_template('insert-student.html', error=error)
    else:
        return render_template('insert-student.html')

@app.route('/student', methods=['POST', 'GET'])
def student():
    return render_template('student.html')

def isValid(username, password):
    dao = UserDAO()
    user = dao.select(username)
    if user == None:
        return False
    return password == user.getPassword()

def insertUser(username, password):
    dao = UserDAO()
    user = dao.insert(User(username, password))
    if user == None:
        return False
    return username == user.getUsername() and password == user.getPassword()

def insertStudent(student):
    dao = StudentDAO()
    student = dao.insert(student)
    if student == None:
        return False
    return True
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
