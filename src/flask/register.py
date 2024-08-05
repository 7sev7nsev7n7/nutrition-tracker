# register.py
'''
module to register new users
important to check whether user exists prior
default permissions are readonly
'''
from usercheck import check
from hashlib import md5

# registers user if avaliable. returns true upon success, false upon failure
def register(u,p):
    if (check(u) == 0): # check if username is available to register
        with open("./data/auth","a") as auth:
            auth.write(f"{u},{md5(p.encode()).hexdigest()},0\n") # users have 0 permissions by default
        return 1
    else:
        print("username is not available")
        return 0
