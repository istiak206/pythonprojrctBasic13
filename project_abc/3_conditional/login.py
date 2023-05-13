default_username = 'admin'
default_password = '123456'

username = input('username: ')
password = input ('Password: ')

if username == default_username and password == default_password:
    print("login successful")
else :
    print("login failed")