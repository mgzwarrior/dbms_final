from models.course import Course
import cx_Oracle

class CourseDAO():
    def __init__(self):
        self.db = cx_Oracle.connect('mgrant/csrocks33@//csc325.cjjvanphib99.us-west-2.rds.amazonaws.com:1521/ORCL')

    def select(self, course_id):
        sql = 'SELECT * FROM Courses WHERE id = :course_id'
        params = {'course_id':course_id}
        cursor = self.db.cursor()
        cursor.execute(sql, params)
        row = cursor.fetchone()
        cursor.close()
        if row:
            return CourseDAO.rowToCourse(row)
        return None

    def selectAll(self):
        sql = 'SELECT * FROM Courses'
        cursor = self.db.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        cursor.close()
        if rows:
            return CourseDAO.rowsToCourses(rows)
        return None

    def insert(self, course):
        sql = 'INSERT INTO Courses ' \
                '(course_id, name, department, professor, classroom)' \
                'VALUES (:course_id, :name, :department, :professor, :classroom)'
        params = course.__dict__
        print params
        cursor = self.db.cursor()
        cursor.execute(sql, params)
        self.db.commit()
        cursor.close()
        return self.select(course.getCourseId())

    def update(self, course):
        sql = 'UPDATE Courses SET course_id = :course_id, name = :name, department = :department, professor = :professor, classroom = :classroom)'
        params = course.__dict__
        cursor = self.db.cursor()
        cursor.execute(sql, params)
        self.db.commit()
        cursor.close()
        return self.select(course.getCourseId())

    def delete(self, course_id):
        if course_id == None:
            return False
        sql = 'DELETE FROM Courses WHERE course_id = :course_id'
        params = {'course_id':course_id}
        cursor = self.db.cursor()
        cursor.execute(sql, params)
        self.db.commit()
        cursor.close()
        if self.select(course_id):
            return False
        return True

    @staticmethod
    def rowToCourse(row):
        course_id = row[0]
        name = row[1]
        department = row[2]
        professor = row[3]
        classroom = row[4]
        return Course(course_id, name, department, professor, classroom)

    @staticmethod
    def rowsToCourses(rows):
        Courses = []
        for row in rows:
            Courses.append(CourseDAO.rowToCourse(row))
        return Courses

    def __del__(self):
        self.db.close()
