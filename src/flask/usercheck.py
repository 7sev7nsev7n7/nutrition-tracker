# usercheck.py
'''
module to check whether user is in auth database or not
useful for registering, authentication and checking permissions
'''
def getUsers():
    users=[]
    filepath = "./data/auth"
    try:
        file = open(filepath,"r")
    except FileNotFoundError:
        print("auth file not found!")
        print("creating dummy file")
        file = open(filepath,"a")

    with open(filepath,'r') as file:
        for line in file:
            user = line.split(',')
            user[-1] = user[-1].replace('\n','')
            users.append(user)
    return users

# check if user exists in auth database, returns user object if true, else false
def check(usr):
    users = getUsers()
    if usr in [user[0] for user in users]:
        uid = [user[0] for user in users].index(usr)
        return users[uid]
    else:
        return 0
