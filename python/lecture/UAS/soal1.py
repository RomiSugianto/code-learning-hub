import auth

user=input('masukan username:')
passwd=input('masukan password:')

authentication=auth.Login(user,passwd)
print(authentication.Auth())