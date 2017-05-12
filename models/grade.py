class Grade():
    def __init__(self, grade, student_id, course_id):
        self.grade = grade
        self.student_id = student_id
        self.course_id = course_id

    def getGrade(self):
        return self.grade

    def setGrade(self, grade):
        self.grade = grade

    def getStudentId(self):
        return self.student_id

    def setStudentId(self, student_id):
        self.student_id = student_id

    def getCourseId(self):
        return self.course_id

    def setCourseId(self, course_id):
        self.course_id = course_id

    def __str__(self):
        return 'grade = ' + self.getGradeId() + \
                'student_id = ' + self.getStudentId() + \
                'course_id = ' + self.getCourseId()
