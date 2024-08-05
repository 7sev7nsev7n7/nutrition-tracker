# auth.py
'''
this module authenticates a user against existing entries in auth database
md5 hashes are used to authenticate, to avoid storing plaintext passwords
'''
from usercheck import check
from hashlib import md5

# authenticate user using user and password
# function returns true if successfully authed, false otherwise
def auth(u, p):
    if check(u): # first check whether user is in auth database
        uhash = check(u)[1] # extract user hash from auth database
        if (md5(p.encode()).hexdigest() == uhash): # compare hash for authentication
            return 1
        else:
            return 0
    else:
        print("user is not registered")
        return 0
