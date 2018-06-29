

class Credentials:
    def __init__(self, username='', password='', token=''):
        self.username = username
        self.password = password
        self.token = token
        
    def getAuthObj(self):
        return {'username': self.username, 'password': self.password, 'token': self.token}