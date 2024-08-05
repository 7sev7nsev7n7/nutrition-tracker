# register.py
'''
module to register new users
important to check whether user exists prior
default permissions are none
'''
from usercheck import check
from hashlib import md5
from userdata import writeData, delData
from auth import auth
filepath="./data/auth"

# registers user if avaliable. returns true upon success, false upon failure
def register(u,p):
    if (check(u) == 0): # check if username is available to register
        with open(filepath,"a") as auth:
            auth.write(f"{u},{md5(p.encode()).hexdigest()},0\n") # users have 0 permissions by default
            writeData(u,sex="", height="", weight="", timezone="")
            print(f"added userdata entry for {u}")
        return 1
    else:
        print("username is not available")
        return 0

def unregister(username,password):
    if auth(username,password): # authenticate user once more
        if (check(username) != 0): # if user is found in auth file
            newdata = open(filepath,'r').readlines()
            for entry in newdata:
                if username in entry:
                    newdata.remove(entry)
                    break
            with open(filepath,'w') as file:
                file.write('')
                for entry in newdata:
                    file.write(str(entry))
            delData(username)
            print(f"succsessfully unregistered {username}")
        return 1
    else:
        print(f"failed to delete user entry for {username}")
        return 0
