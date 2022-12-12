import sqlite3   #enable control of an sqlite database
import dbFuncs

def createWatchlistTable(): 
    # creates user_info and story_info 
    conn =  dbFuncs.establishConnection()
    c = conn[0]
    db = conn[1]
    c.execute(f"DROP TABLE IF EXISTS watchlist")