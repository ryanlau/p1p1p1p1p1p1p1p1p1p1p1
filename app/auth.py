import sqlite3   #enable control of an sqlite database
import dbFuncs

def createUserTable(): 
    # creates user_info and story_info 
    conn =  dbFuncs.establishConnection()
    c = conn[0]
    db = conn[1]
    c.execute(f"DROP TABLE IF EXISTS user_info")
    c.execute(f"CREATE TABLE user_info (user_id TEXT PRIMARY KEY, password TEXT)")
    dbFuncs.disconnect(db)

def addNewUser(username, password): 
    # adds new user and password to user_info table
    conn =  dbFuncs.establishConnection()
    c = conn[0]
    db = conn[1]
    c.execute("INSERT INTO user_info VALUES (?, ?);", (username, password))
    dbFuncs.disconnect(db)

def getUserList():
    # returns list of existing users
    conn =  dbFuncs.establishConnection()
    c = conn[0]
    db = conn[1]
    vals = c.execute("SELECT user_id FROM user_info").fetchall()
    dbFuncs.disconnect(db)
    formatted_users = []
    for i in range(len(vals)): 
        formatted_users.append(vals[i][0])
    return formatted_users

def getUserPassword(user):
    conn =  dbFuncs.establishConnection()
    c = conn[0]
    db = conn[1]
    passw = c.execute("SELECT password FROM user_info WHERE user_id = ?", (user,)).fetchall()[0][0]
    dbFuncs.disconnect(db)
    return passw

def isUsernameAvail(user):
    exsistingUsers = getUserList()
    if user in exsistingUsers: 
        return True
    return False

def testing():
    createUserTable()
    addNewUser("epap", "hi")
    print(getUserList())
    print(getUserPassword("epap"))
    print(isUsernameAvail("epap"))
    print(isUsernameAvail("epap1"))

#testing()


