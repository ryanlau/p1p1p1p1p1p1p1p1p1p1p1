try:
    from .db import query_db
except:
    from db import query_db


def create_watchlist_table(): 
    query_db("DROP TABLE IF EXISTS watchlist")
    query_db("CREATE TABLE watchlist (username TEXT, ticker TEXT, company_name TEXT)")


def add_ticker(username, tick, comp_name):
    query_db("INSERT INTO  watchlist VALUES (?,?,?)",(username,tick,comp_name))


def get_watchlist(username): 
    vals = query_db("SELECT ticker,company_name FROM watchlist WHERE username = ?",(username,), all=True)
    return vals

def remove_ticker(username, tick):
    query_db("DELETE FROM watchlist WHERE username = ? AND ticker = ?",(username,tick))


def delete_watchlist_table(): 
    query_db("DROP TABLE IF EXISTS watchlist")
    


if __name__ == "__main__":
    create_watchlist_table()
    add_ticker("epaperno", "AAPL", "Apple")
    add_ticker("r", "GOOG", "google")
    print(get_watchlist("epaperno"))
    print(get_watchlist("r"))
    remove_ticker("epaperno", "AAPL")
    print(get_watchlist("epaperno"))
    print(get_watchlist("r"))
    delete_watchlist_table()



