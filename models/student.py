class Student():
    def __init__(self, student_id, major, minor, name, phone, street, city, state, zip_code):
        self.student_id = student_id
        self.major = major
        self.minor = minor
        self.name = name
        self.phone = phone
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code

    def getStudentId(self):
        return self.student_id

    def setStudentId(self, student_id):
        self.student_id = student_id

    def getMajor(self):
        return self.major

    def setMajor(self, major):
        self.major = major

    def getMinor(self):
        return self.minor

    def setMinor(self, minor):
        self.minor = minor

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getPhone(self):
        return self.phone

    def setPhone(self, phone):
        self.phone = phone

    def getStreet(self):
        return self.street

    def setStreet(self, street):
        self.street = street

    def getCity(self):
        return self.city

    def setCity(self, city):
        self.city = city

    def getState(self):
        return self.state

    def setState(self, state):
        self.state = state

    def getZipCode(self):
        return self.zip_code

    def setZipCode(self, zip_code):
        self.zip_code = zip_code

    def __str__(self):
        return 'id = ' + self.getStudentId() + \
                'major = ' + self.getMajor() + \
                'minor = ' + self.getMinor() + \
                'name = ' + self.getName() + \
                'phone = ' + self.getPhone() + \
                'street = ' + self.getStreet() + \
                'city = ' + self.getCity() + \
                'state = ' + self.getState() + \
                'zip = '
