from models.user import User
import cx_Oracle

class UserDAO():
    def __init__(self):
        self.db = cx_Oracle.connect('mgrant/csrocks33@//csc325.cjjvanphib99.us-west-2.rds.amazonaws.com:1521/ORCL')

    def select(self, username):
        sql = 'SELECT * FROM Users WHERE username = :username'
        params = {'username':username}
        cursor = self.db.cursor()
        try:
            cursor.execute(sql, params)
        except cx_Oracle.IntegrityError as e:
            error, = e.args
            print(error.code)
            return None
        row = cursor.fetchone()
        cursor.close()
        if row:
            return UserDAO.rowToUser(row)
        else:
            return None

    def insert(self, user):
        sql = 'INSERT INTO Users '\
                '(username, password) '\
                'VALUES (:username, :password)'
        params = user.__dict__
        cursor = self.db.cursor()
        try:
            cursor.execute(sql, params)
        except cx_Oracle.IntegrityError as e:
            error, = e.args
            print(error.code)
            return None
        self.db.commit()
        cursor.close()
        return self.select(user.getUsername())

    @staticmethod
    def rowToUser(row):
        username = row[0]
        password = row[1]
        return User(username, password)
