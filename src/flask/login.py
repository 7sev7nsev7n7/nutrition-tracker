# login.py
'''
main module to run, which incorporates user authentication,
read/write operations of database and requests from the
frontend applications via simple api
'''

from auth import auth
from register import register
from usercheck import check

def login(u, p):
    # register user if non-existant
    if check(u) == 0: 
        print("user is not registered, registering now")
        if register(u, input("please enter a new password: ")):
            print("successfully registered")
        else:
            print("failed to register")
            quit()

    # once confirmed user exists, authenticate
    if auth(password, input("please log in with your password: ")):
        return 1 
    else:
        return 0
