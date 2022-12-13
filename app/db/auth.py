try:
    from .db import query_db
except:
    from db import query_db

def create_user_info_table(): 
    # creates user_info and story_info 
    query_db("DROP TABLE IF EXISTS user_info")
    query_db("CREATE TABLE user_info (user_id TEXT PRIMARY KEY, password TEXT)")

def add_new_user(username, password): 
    query_db("INSERT INTO user_info VALUES (?, ?);", (username, password))

def check_username_availability(username):
    user = query_db("SELECT * FROM user_info WHERE user_id = ?", (username,))
    return user is None

def check_creds(username, password):
    user = query_db("SELECT * FROM user_info WHERE user_id = ? AND password = ?", (username, password))
    return user is not None


    
# LINES BELOW ONLY GET RUN IF "EXPLICITY RAN" with `python auth.py`
if __name__ == "__main__":
    create_user_info_table()
    print(check_username_availability("epap"))
    add_new_user("epap", "hi")
    print(check_creds("epap", "hi"))
    print(check_creds("epap", "hi2"))
    print(check_username_availability("epap"))


