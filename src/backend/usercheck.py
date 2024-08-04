# usercheck.py
'''
module to check whether user is in auth database or not
useful for registering, authentication and checking permissions
'''

users = []
try:
    with open("auth", 'r') as file:
        for line in file: # each line stores data for a single user
            user = line.split(',')
            user[-1] = user[-1].replace('\n','') # remove newline char from last element
            users.append(user)
except Exception as ex:# test?
    open("auth",'w') 

# check if user exists in auth database, returns user object if true, else false
def check(usr):
    if usr in users[0]:
        uid = users[0].index(usr)
        return users[uid]
    else:
        return 0
