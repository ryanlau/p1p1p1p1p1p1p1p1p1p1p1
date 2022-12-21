try:
    from .db import query_db
except:
    from db import query_db

def create_user_info_table(): 
    # creates user_info and story_info 
    query_db("CREATE TABLE IF NOT EXISTS user_info (username TEXT PRIMARY KEY, password TEXT, lat TEXT, lon TEXT, city TEXT, zip TEXT)")

def add_new_user(username, password, lat, lon, city, zip): 
    query_db("INSERT INTO user_info VALUES (?, ?, ?, ?, ?, ?);", (username, password, lat, lon, city, zip))

def check_username_availability(username):
    user = query_db("SELECT * FROM user_info WHERE username = ?", (username,))
    return user is None

def check_creds(username, password):
    user = query_db("SELECT * FROM user_info WHERE username = ? AND password = ?", (username, password))
    return user is not None

def get_location(username):
    location = query_db("SELECT lat, lon, city, zip FROM user_info WHERE username = ?", (username,))
    return location
    
# LINES BELOW ONLY GET RUN IF "EXPLICITY RAN" with `python app/db/auth.py`
if __name__ == "__main__":
    create_user_info_table()
    print(check_username_availability("epap"))
    add_new_user("epap", "hi", "123")
    print(check_creds("epap", "hi"))
    print(check_creds("epap", "hi2"))
    print(check_username_availability("epap"))
    # print(get_zipcoe("epap"))



