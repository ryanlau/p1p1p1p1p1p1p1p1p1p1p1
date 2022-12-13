import sqlite3   #enable control of an sqlite database
from . import dbFuncs

def createTodoTable(): 
    # creates user_info and story_info 
    conn =  dbFuncs.establishConnection()
    c = conn[0]
    db = conn[1]
    c.execute(f"DROP TABLE IF EXISTS todos")
    c.execute(f"CREATE TABLE todos (todo_id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, item TEXT, completion_status INTEGER)")
    dbFuncs.disconnect(db)

def addItem(username, item, completion_status): 
    conn =  dbFuncs.establishConnection()
    c = conn[0]
    db = conn[1]
    c.execute("INSERT INTO todos (username, item, completion_status) VALUES (?, ?, ?);", (username, item, completion_status))
    dbFuncs.disconnect(db)

def getListItems(username):
    conn =  dbFuncs.establishConnection()
    c = conn[0]
    db = conn[1]
    vals = c.execute("SELECT item FROM todos WHERE username = ?",(username,)).fetchall()
    dbFuncs.disconnect(db)
    formatted_items = []
    for i in range(len(vals)): 
        formatted_items.append(vals[i][0])
    return formatted_items

def updateCompletionStatus(todo_id, bool_val): 
    # marks item as bool_val 
    # bool_val should be passed in as 1 for true and 0 for false
    conn =  dbFuncs.establishConnection()
    c = conn[0]
    db = conn[1]
    c.execute("UPDATE todos SET completion_status = ? WHERE todo_id = ?;",(bool_val, todo_id))
    dbFuncs.disconnect(db)

def getCompletionStatus(todo_id):
    conn =  dbFuncs.establishConnection()
    c = conn[0]
    db = conn[1]
    status = c.execute("SELECT completion_status FROM todos WHERE todo_id= ?", (todo_id,)).fetchall()[0][0]
    dbFuncs.disconnect(db)
    return status

def deleteItem(todo_id): 
    #deletes item from table
    conn =  dbFuncs.establishConnection()
    c = conn[0]
    db = conn[1]
    c.execute("DELETE FROM todos WHERE todo_id = ?;",(todo_id,))
    dbFuncs.disconnect(db)

def testing():
    createTodoTable()
    addItem("epaperno", "hi", 0)
    addItem("epaperno", "bye", 0)
    print(getListItems("epaperno"))
    updateCompletionStatus(1,1)
    print(getCompletionStatus(1))
    print(getCompletionStatus(2))
    deleteItem(1)
    print(getListItems("epaperno"))

testing()