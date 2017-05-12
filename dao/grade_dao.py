from models.grade import Grade
import cx_Oracle

class GradeDAO():
    def __init__(self):
        self.db = cx_Oracle.connect('mgrant/csrocks33@//csc325.cjjvanphib99.us-west-2.rds.amazonaws.com:1521/ORCL')

    def select(self, student_id, course_id):
        sql = 'SELECT * FROM Grades WHERE student_id = :student_id && course_id = :course_id'
        params = {'student_id':student_id, 'course_id':course_id}
        cursor = self.db.cursor()
        cursor.execute(sql, params)
        row = cursor.fetchone()
        cursor.close()
        if row:
            return GradeDAO.rowToGrade(row)
        return None

    def selectAll(self):
        sql = 'SELECT * FROM Grades'
        cursor = self.db.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        cursor.close()
        if rows:
            return GradeDAO.rowsToGrades(rows)
        return None

    def insert(self, grade):
        sql = 'INSERT INTO Grades ' \
                '(grade, student_id, course_id)' \
                'VALUES (:grade, :student_id, :course_id)'
        params = grade.__dict__
        print params
        cursor = self.db.cursor()
        cursor.execute(sql, params)
        self.db.commit()
        cursor.close()
        return self.select(grade.getGradeId())

    def update(self, grade):
        sql = 'UPDATE Grades SET grade = :grade, student_id = :student_id, course_id = :course_id)'
        params = grade.__dict__
        cursor = self.db.cursor()
        cursor.execute(sql, params)
        self.db.commit()
        cursor.close()
        return self.select(grade.getGradeId())

    def delete(self, student_id, course_id):
        if grade == None:
            return False
        sql = 'DELETE FROM Grades WHERE student_id = :student_id && course_id = :course_id'
        params = {'student_id':student_id, 'course_id':course_id}
        cursor = self.db.cursor()
        cursor.execute(sql, params)
        self.db.commit()
        cursor.close()
        if self.select(student_id, course_id):
            return False
        return True

    @staticmethod
    def rowToGrade(row):
        grade = row[0]
        student_id = row[1]
        course_id = row[2]
        return Grade(grade, student_id, course_id)

    @staticmethod
    def rowsToGrades(rows):
        Grades = []
        for row in rows:
            Grades.append(GradeDAO.rowToGrade(row))
        return Grades

    def __del__(self):
        self.db.close()
