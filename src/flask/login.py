# login.py
'''
login user based on authentication and user existence
'''

from auth import auth
from usercheck import check

def login(u, p):
    # once confirmed user exists, authenticate
    if auth(u, p):
        return u # return username if successfully registered, for use in scripts
    else:
        return 0
