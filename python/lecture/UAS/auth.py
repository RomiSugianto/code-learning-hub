class Login:
    def __init__(self, user, passwd):
        self.username=user
        self.password=passwd
    
    def SetUsername(self, user):
        self.username=user
    
    def GetUsername(self):
        return self.username
    
    def SetPassword(self, passwd):
        self.password=passwd
    
    def GetPassword(self):
        return self.password
    
    def Auth(self):
        authMsg=''
        uname='romi'
        upasswd='123'
        if self.username==uname and self.password==upasswd:
            authMsg='login successfully'
        else:
            authMsg='username or password false'
            
        return authMsg