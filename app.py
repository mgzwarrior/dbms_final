from flask import Flask
from flask import abort, redirect, url_for, request, render_template, session
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
            session['username'] = username
            return redirect(url_for('home'))
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
            return redirect(url_for('home'))
        else:
            error = 'Error: Username ' + username + ' is taken'
            return render_template('create.html', error=error)
    else:
        return render_template('create.html')

@app.route('/home', methods=['POST', 'GET'])
def home():
    username = session['username']
    dao = StudentDAO()
    students = dao.selectAll()
    return render_template('home.html', username=username, students=students)

@app.route('/logout')
def logout():
    session.pop('username', None)
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
    student_id = request.args.get('student_id', None)
    dao = StudentDAO()
    student = dao.select(student_id)
    return render_template('student.html', student=student)

@app.route('/delete-student', methods=['POST', 'GET'])
def deleteStudent():
    student_id = request.args.get('student_id', None)
    dao = StudentDAO()
    if dao.delete(student_id):
        return redirect(url_for('home'))
    else:
        error = "ERROR"
        return redirect(url_for('student', student=dao.select(student_id), error=error))

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
    app.secret_key = '=fvf#k!x7&heo!$(y#&0dpz%agn39nl7u=v8&az4@*d1yd#+2q'
    app.run(host='0.0.0.0', port=8081)
