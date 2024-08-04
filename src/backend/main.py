# main.py
'''
main module to run, which incorporates user authentication,
read/write operations of database and requests from the
frontend applications via simple api
'''

import auth

usr = input("username: ")
pw = input("password: ")
if auth.Auth(usr, pw):
    print(f"logged in successfully as {usr}")
else:
    print("failed to authenticate")
