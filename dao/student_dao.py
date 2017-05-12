from models.student import Student
import cx_Oracle

class StudentDAO():
    def __init__(self):
        self.db = cx_Oracle.connect('mgrant/csrocks33@//csc325.cjjvanphib99.us-west-2.rds.amazonaws.com:1521/ORCL')

    def select(self, student_id):
        sql = 'SELECT * FROM Students WHERE id = :student_id'
        params = {'student_id':student_id}
        cursor = self.db.cursor()
        cursor.execute(sql, params)
        row = cursor.fetchone()
        cursor.close()
        if row:
            return StudentDAO.rowToStudent(row)
        return None

    def selectAll(self):
        sql = 'SELECT * FROM Students'
        cursor = self.db.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        cursor.close()
        if rows:
            return StudentDAO.rowsToStudents(rows)
        return None

    def insert(self, student):
        sql = 'INSERT INTO Students ' \
                '(id, major, minor, name, phone, street, city, state, zip, picture)' \
                'VALUES (:student_id, :major, :minor, :name, :phone, :street, :city, :state, :zip_code)'
        params = student.__dict__
        cursor = self.db.cursor()
        cursor.execute(sql, params)
        self.db.commit()
        cursor.close()
        return self.select(student.getStudentId())

    def update(self, student):
        sql = 'UPDATE Students SET id = :student_id, major = :major, minor = :minor, name = :name, phone = :phone, street = :street, city = :city, state = :state, zip = :zip_code)'
        params = student.__dict__
        cursor = self.db.cursor()
        cursor.execute(sql, params)
        self.db.commit()
        cursor.close()
        return self.select(student.getStudentId())

    def delete(self, student_id):
        sql = 'DELETE FROM Students WHERE id = :student_id'
        params = {'id':student_id}
        cursor = self.db.cursor()
        cursor.execute(sql, params)
        self.db.commit()
        cursor.close()
        if self.select(student_id):
            return False
        return True

    @staticmethod
    def rowToStudent(row):
        student_id = row[0]
        major = row[1]
        minor = row[2]
        name = row[3]
        phone = row[4]
        street = row[5]
        city = row[6]
        state = row[7]
        zip_code = row[8]
        return Student(student_id, major, minor, name, phone, street, city, state, zip_code)

    @staticmethod
    def rowsToStudents(rows):
        students = []
        for row in rows:
            students.append(StudentDAO.rowToStudent(row))
        return students

    def __del__(self):
        self.db.close()
