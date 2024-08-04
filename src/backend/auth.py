# auth.py
'''
this module handles access to the user auth, updating and modifying
entries when necessary. also handles permissions
'''
from usercheck import check
from hashlib import md5

# authenticate user using user and password
# function returns true if successfully authed, false otherwise
def Auth(u, p):
    if check(u): # first check whether user is in auth database
        uhash = check(u)[1] # extract user hash from auth database
        if (md5(p.encode()).hexdigest() == uhash): # compare hash for authentication
            return 1
        else:
            return 0
    else:
        print("user is not registered")
        return 0
