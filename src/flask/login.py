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
    # once confirmed user exists, authenticate
    if auth(u, p):
        return u # return username if successfully registered, for use in scripts
    else:
        return 0
