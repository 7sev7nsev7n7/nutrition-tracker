# userdata.py
'''
store and access user's data
this module allows users to register new information
or consult information already available
module must be called on user registry
'''
from auth import auth
from usercheck import check
filepath = "./data/userinfo"

def readData(username=None):
    try:
        file = open(filepath,'r')
    except FileNotFoundError:
        print("user information file not found, creating dummy file")
        open(filepath,'w')

    mode = None
    with open(filepath,'r') as file:
        if len(file.readlines()) == 0:
            print("no entries")
            mode = 0
        else:
            mode = 1
