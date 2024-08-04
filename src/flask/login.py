# login.py
'''
main module to run, which incorporates user authentication,
read/write operations of database and requests from the
frontend applications via simple api
'''

from auth import auth
from register import register
from usercheck import check

usr = input("username: ")
# register user if non-existant
if check(usr) == 0: 
    print("user is not registered, registering now")
    if register(usr, input("please enter a new password: ")):
        print("successfully registered")

# once confirmed user exists, authenticate
if auth(usr, input("please log in with your password: ")):
    print("successfully logged in")
else:
    print("failed to log in")
