from models.user import user
import cx_Oracle

class user_dao():
    def __init__(self):
        self.db = cx_Oracle.connect('mgrant/csrocks33@//csc325.cjjvanphib99.us-west-2.rds.amazonaws.com:1521/ORCL')

    def select(self, username):
        print 'user_dao.py : in select() method'
        sql = 'SELECT * FROM Users WHERE username = :username'
        params = {'username':username}
        cursor = self.db.cursor()
        cursor.execute(sql, params)
        row = cursor.fetchone()
        cursor.close()
        if row:
            return user_dao.rowToUser(row)
        else:
            return None

    @staticmethod
    def rowToUser(row):
        username = row[0]
        password = row[1]
        return user(username, password)
