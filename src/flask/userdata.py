# userdata.py
'''
store and access user's data
this module allows users to register new information
or consult information already available
module must be called on user registry
'''
from auth import auth
from usercheck import check
import json
filepath = "./data/userdata"

# all operations are specific to a single user, so username must be passed as an argument
def readData(username): # returns json data
    try:
        with open(filepath,'r') as file:
            for entry in file:
                if json.loads(entry)["username"] == username:
                    return entry.replace('\n','')
        return 0
    except FileNotFoundError:
        print("file not found, creating emtpy database")
        return 0


def writeData(username,  # arguments to write, other than username all else are optional
              height=None,
              weight=None, 
              sex=None):
    # python dictionary with all entries
    data = {"username": username,
            "height": height,
            "weight": weight,
            "sex": sex}
    if readData(username) == 0: # if user is found in userdata file
        with open(filepath,'a') as file:
            file.write(json.dumps(data));file.write('\n') # write newline to keep every user entry on single line
        print(f"successfully wrote data for {username}")
        return 1
    else:
        print(f"user {username} already in system, use updateData() to change information")
        return 0

def delData(username): # deletes user data. important to only use this function when deleting user login entry.
    newdata = open(filepath,'r').readlines()
    userdata = f'{readData(username)}\n'
    if userdata in newdata:
        newdata.remove(userdata)
        with open(filepath,'w') as file:
            file.write('')
            for entry in newdata:
                file.write(str(entry))

        print("successfully deleted user data")
        return 1
    else:
        print("failed to remove user data")
        return 0
