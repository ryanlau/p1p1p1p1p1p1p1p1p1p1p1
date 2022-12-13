try:
    from .db import query_db
except:
    from db import query_db

def create_todo_table(): 
    query_db(f"DROP TABLE IF EXISTS todos")
    query_db(f"CREATE TABLE todos (todo_id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, item TEXT, completion_status INTEGER)")


def add_todo(username, item, completion_status): 
    query_db("INSERT INTO todos (username, item, completion_status) VALUES (?, ?, ?);", (username, item, completion_status))


def get_all_todos(username):
    vals = query_db("SELECT item FROM todos WHERE username = ?",(username,), all=True)
    formatted_items = []
    for i in range(len(vals)): 
        formatted_items.append(vals[i][0])
    return formatted_items


def update_completion_status(todo_id, bool_val): 
    # marks item as bool_val 
    # bool_val should be passed in as 1 for true and 0 for false
    query_db("UPDATE todos SET completion_status = ? WHERE todo_id = ?;",(bool_val, todo_id))


def get_completion_status(todo_id):
    status = query_db("SELECT completion_status FROM todos WHERE todo_id= ?", (todo_id,))[0]
    return status


def delete_todo(todo_id): 
    query_db("DELETE FROM todos WHERE todo_id = ?;",(todo_id,))


if __name__ == "__main__":
    create_todo_table()
    add_todo("epaperno", "hi", 0)
    add_todo("epaperno", "bye", 0)
    print(get_all_todos("epaperno"))
    update_completion_status(1,1)
    print(get_completion_status(1))
    print(get_completion_status(2))
    delete_todo(1)
    print(get_all_todos("epaperno"))