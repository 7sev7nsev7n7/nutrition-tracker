# auth.py
'''
this module handles access to the user auth, updating and modifying
entries when necessary. also handles permissions
'''
from hashlib import md5

# initially load list of all users
users = []
try:
    with open("auth", 'r') as file:
        for line in file: # each line stores data for a single user
            user = line.split(',')
            user[-1] = user[-1].replace('\n','') # remove newline char from last element
            users.append(user)
except Exception as ex: # create auth file if nonexistant
    open("auth",'w')

# authenticate user using user and password
# function returns true if successfully authed, false otherwise
def Auth(u, p):
    if u in users[0]: # first check whether user is in auth database
        uid = users[0].index(u) # get user position in list
        if (md5(p.encode()).hexdigest() == users[uid][1]): # compare hash to database for authentication
            return 1
        else:
            return 0
    else:
        print("user is not registered")
        return 0
