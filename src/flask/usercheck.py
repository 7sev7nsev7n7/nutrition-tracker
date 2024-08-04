# usercheck.py
'''
module to check whether user is in auth database or not
useful for registering, authentication and checking permissions
'''
users = []
def getUsers():
    try:
        file = open("auth","r")
    except FileNotFoundError:
        print("auth file not found!")
        print("creating dummy file")
        file = open("auth","w")
        file.write("0,0,0\n")


    with open("auth",'r') as file:
        for line in file:
            user = line.split(',')
            user[-1] = user[-1].replace('\n','')
            users.append(user)

# check if user exists in auth database, returns user object if true, else false
def check(usr):
    getUsers()
    if usr in [user[0] for user in users]:
        uid = [user[0] for user in users].index(usr)
        return users[uid]
    else:
        return 0
