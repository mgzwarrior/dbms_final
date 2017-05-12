from flask import Flask
from flask import abort, redirect, url_for, request, render_template, session
from models.user import User
from models.student import Student
from models.course import Course
from models.grade import Grade
from dao.user_dao import UserDAO
from dao.student_dao import StudentDAO
from dao.course_dao import CourseDAO
from dao.grade_dao import GradeDAO

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
    dao = CourseDAO()
    courses = dao.selectAll()
    dao = GradeDAO()
    grades = dao.selectAll()
    return render_template('home.html', username=username, students=students, courses=courses, grades=grades)

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

@app.route('/insert-course', methods=['POST', 'GET'])
def insertCourse():
    if request.method == 'POST':
       course_id = request.form['course_id']
       name = request.form['name']
       department = request.form['department']
       professor = request.form['professor']
       classroom = request.form['classroom']
       course = Course(course_id, name, department, professor, classroom,)
       if insertCourse(course):
           return redirect(url_for('home'))
       else:
           error = 'ERROR'
           return render_template('insert-course.html', error=error)
    else:
        return render_template('insert-course.html')

@app.route('/course', methods=['POST', 'GET'])
def course():
    course_id = request.args.get('course_id', None)
    dao = CourseDAO()
    course = dao.select(course_id)
    return render_template('course.html', course=course)

@app.route('/delete-course', methods=['POST', 'GET'])
def deleteCourse():
    course_id = request.args.get('course_id', None)
    dao = CourseDAO()
    if dao.delete(course_id):
        return redirect(url_for('home'))
    else:
        error = "ERROR"
        return redirect(url_for('course', course=dao.select(course_id), error=error))

@app.route('/insert-grade', methods=['POST', 'GET'])
def insertGrade():
    if request.method == 'POST':
       grade = request.form['grade']
       student_id = request.form['student_id']
       course_id = request.form['course_id']
       grade = Grade(grade, student_id, course_id)
       if insertGrade(grade):
           return redirect(url_for('home'))
       else:
           error = 'ERROR'
           return render_template('insert-grade.html', error=error)
    else:
        return render_template('insert-grade.html')

@app.route('/grade', methods=['POST', 'GET'])
def grade():
    student_id = request.args.get('student_id', None)
    course_id = request.args.get('course_id', None)
    dao = CourseDAO()
    course = dao.select(student_id, course_id)
    return render_template('grade.html', grade=grade)

@app.route('/delete-grade', methods=['POST', 'GET'])
def deleteGrade():
    student_id = request.args.get('student_id', None)
    course_id = request.args.get('course_id', None)
    dao = CourseDAO()
    if dao.delete(student_id, course_id):
        return redirect(url_for('home'))
    else:
        error = "ERROR"
        return redirect(url_for('grade', grade=dao.select(student_id, course_id), error=error))

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

def insertCourse(course):
    dao = CourseDAO()
    course = dao.insert(course)
    if course == None:
        return False
    return True

def insertGrade(grade):
    dao = GradeDAO()
    grade = dao.insert(grade)
    if grade == None:
        return False
    return True
    
if __name__ == '__main__':
    app.secret_key = '=fvf#k!x7&heo!$(y#&0dpz%agn39nl7u=v8&az4@*d1yd#+2q'
    app.run(host='0.0.0.0', port=8081)
