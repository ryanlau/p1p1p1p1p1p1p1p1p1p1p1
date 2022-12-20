try:
    from .db import query_db
except:
    from db import query_db


def create_watchlist_table(): 
    query_db("CREATE TABLE IF NOT EXISTS watchlists (username TEXT, ticker TEXT, company_name TEXT)")


def add_ticker(username, tick, comp_name):
    query_db("INSERT INTO  watchlists VALUES (?,?,?)",(username,tick,comp_name))


def get_watchlist(username): 
    vals = query_db("SELECT ticker,company_name FROM watchlists WHERE username = ?",(username,), all=True)
    return vals

def remove_ticker(username, tick):
    query_db("DELETE FROM watchlists WHERE username = ? AND ticker = ?",(username,tick))


def delete_watchlist_table(): 
    query_db("DROP TABLE IF EXISTS watchlists")
    


# LINES BELOW ONLY GET RUN IF "EXPLICITY RAN" with `python app/db/watchlists.py`
if __name__ == "__main__":
    create_watchlist_table()
    add_ticker("epap", "AAPL", "Apple")
    add_ticker("epap", "GOOG", "google")
    print(get_watchlist("epap"))
    print(get_watchlist("r"))
    remove_ticker("epap", "AAPL")
    print(get_watchlist("epap"))
    print(get_watchlist("r"))



