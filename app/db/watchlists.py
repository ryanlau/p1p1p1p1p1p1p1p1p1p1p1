import sqlite3   #enable control of an sqlite database
from . import dbFuncs

def createWatchlistTable(): 
    # creates user_info and story_info 
    conn =  dbFuncs.establishConnection()
    c = conn[0]
    db = conn[1]
    c.execute("DROP TABLE IF EXISTS watchlist")
    c.execute("CREATE TABLE watchlist (username TEXT, ticker TEXT)")
    dbFuncs.disconnect(db)

def addTicker(username, tick):
    conn =  dbFuncs.establishConnection()
    c = conn[0]
    db = conn[1]
    c.execute("INSERT INTO  watchlists VALUES (?,?)",(username,tick))
    dbFuncs.disconnect(db)

def getListTickers(username): 
    conn =  dbFuncs.establishConnection()
    c = conn[0]
    db = conn[1]
    vals = c.execute("SELECT ticker FROM watchlist").fetchall()
    dbFuncs.disconnect(db)
    formatted_tickers = []
    for i in range(len(vals)): 
        formatted_tickers.append(vals[i][0])
    return formatted_tickers

def removeTicker(username, tick):
    return True

def deleteWatchlistTable(): 
    return True
