class Course():
    def __init__(self, course_id, name, department, professor, classroom):
        self.course_id = course_id
        self.name = name
        self.department = department
        self.professor = professor
        self.classroom = classroom

    def getCourseId(self):
        return self.course_id

    def setCourseId(self, course_id):
        self.course_id = course_id

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getDepartment(self):
        return self.department

    def setDepartment(self, department):
        self.department = department

    def getProfessor(self):
        return self.professor

    def setProfessor(self, professor):
        self.professor = professor

    def getClassroom(self):
        return self.classroom

    def setClassroom(self, classroom):
        self.classroom = classroom

    def __str__(self):
        return 'course_id = ' + self.getCourseId() + \
                'name = ' + self.getName() + \
                'department = ' + self.getDepartment() + \
                'professor = ' + self.getProfessor() + \
                'classroom = ' + self.getClassroom() + \
