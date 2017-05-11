class User():
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def getUsername(self):
        return self.username

    def setUsername(self, username):
        self.username = username

    def getPassword(self):
        return self.password

    def setPassword(self, password):
        self.password = password

    def __str__(self):
        return 'username = ' + self.getUsername() + \
                'password = ' + self.getPassword()
