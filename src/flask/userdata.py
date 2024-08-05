# userdata.py
'''
store and access user's data
this module allows users to register new information
or consult information already available
module must be called on user registry
'''
from auth import auth
from usercheck import check
filepath = "./data/userdata"

# all operations are specific to a single user, so username must be passed as an argument
def readData(username,json=True): # returns json data
    try:
        with open(filepath,'r') as file:
            for entry in file:
                if entry.split(':')[0] == username:
                    if json==True:
                        return entry.replace(f"{username}:",'').replace('\n','') # remove username from data list
                    else:
                        return entry
        return 0
    except FileNotFoundError:
        print("file not found, creating empty database")
        open(filepath,'a')
        return 0


def writeData(username, **kwargs): # arguments to write, other than username all else are optional
    # python dictionary with all entries
    data = f"{username}:{kwargs}" # username separated by : to make delimiting easier
    data = data.replace('\'','"')
    if readData(username) == 0: # if user is found in userdata file
        with open(filepath,'a') as file:
            file.write(str(data));file.write('\n') # write newline to keep every user entry on single line
        print(f"successfully wrote data for {username}")
        return 1
    else:
        print(f"user {username} already in system, use updateData() to change information")
        return 0

def delData(username): # deletes user data. important to only use this function when deleting user login entry.
    newdata = open(filepath,'r').readlines()
    userdata = f'{readData(username,json=False)}'
    if userdata in newdata:
        newdata.remove(userdata)
        with open(filepath,'w') as file:
            file.write('')
            for entry in newdata:
                file.write(str(entry))

        print(f"successfully deleted data for user {username}")
        return 1
    else:
        print("failed to remove user data")
        return 0

def updateData(username,**fields):
    cdata = readData(username).split(','); cdata[-1] = cdata[-1].replace('\n','') # remove newline char from last entry
    print(cdata)
