try:
    from .db import query_db
except:
    from db import query_db


def create_watchlist_table(): 
    query_db("DROP TABLE IF EXISTS watchlist")
    query_db("CREATE TABLE watchlist (username TEXT, ticker TEXT)")


def add_ticker(username, tick):
    query_db("INSERT INTO  watchlists VALUES (?,?)",(username,tick))


def get_watchlist(username): 
    vals = query_db("SELECT ticker FROM watchlist", all=True)

    formatted_tickers = []
    for i in range(len(vals)): 
        formatted_tickers.append(vals[i][0])
    return formatted_tickers


def remove_ticker(username, tick):
    return True


def delete_watchlist_table(): 
    return True
