# PPP Mode: Ivan Mijacika, Qina Liu, Justin Morrill, Noakai Aronesty
# SoftDev pd2
# P02 -- Snake++

import sqlite3

DB_file = "discobandit.db"

def add_score(username, score, mode):
    '''Adds a new highscore to the database'''
    highscore_name = "highscore_" + mode
    
    db = sqlite3.connect(DB_file)
    c = db.cursor()

    c.execute("SELECT EXISTS(SELECT usernames FROM scores WHERE usernames = ?)", (username,))
    rowExists = c.fetchone()[0]

    if rowExists:
        dbScore = get_score(username, mode)
        if (dbScore is None) or (score > dbScore):
            # no prev score in this mode or new highscore achieved
            c.execute("UPDATE scores SET {mode} = ? WHERE usernames = ?".format(mode=highscore_name), (score, username))
    else:
        # username does not have row yet
        c.execute("INSERT INTO scores (usernames, {mode}) VALUES (?, ?)".format(mode=highscore_name), (username, score,))
    '''
    TIP : SQL parameters can only apply to insert data, not table names; hence .format()
    '''
    db.commit()
    db.close()

def get_score(username, mode):
    '''Gets the players highscore for a certain mode'''
    
    db = sqlite3.connect(DB_file)
    c = db.cursor()
    highscore_name = "highscore_" + mode
    
    c.execute("SELECT {mode} FROM scores WHERE usernames = (?)".format(mode = highscore_name), (username,))
    return c.fetchone()[0]
    	
def top_n_scores(n, mode):
    '''Gets the top n scores'''
    
    db = sqlite3.connect(DB_file)
    c = db.cursor()
    highscore_name = "highscore_" + mode
    
    c.execute("SELECT {mode} FROM scores ORDER BY {mode} DESC".format(mode = highscore_name))
    
    # get all scores in descending order into a tuple
    n_scores = c.fetchall()[0]
    # converts from tuple to list
    n_scores = list(n_scores)
    # list only the top n 
    n_scores = n_scores[0:n-1]
    return n_scores

def top_n_users(n, mode):
    '''Gets the top n players'''
    
    db = sqlite3.connect(DB_file)
    c = db.cursor()
    highscore_name = "highscore_" + mode
    
    c.execute("SELECT {user} FROM scores ORDER BY {user} DESC".format(user= "usernames", mode = highscore_name))
    
    # gets all players in descending order into a tuple 
    n_users = c.fetchall()[0]
    # converts from tuple to list
    n_users = list(n_users)
    # list only the top n 
    n_users = n_users[0:n-1]
    return n_users


# for testing & debugging purposes
def get_db():
    db = sqlite3.connect(DB_file)
    c = db.cursor()

    c.execute("SELECT * from scores")
    print(c.fetchall())

    db.close()

"""
#or testing add_score and get_score, rm db before testing tho
add_score("Rob", 10, "basic")
print(get_score("Rob", "basic"))
get_db()
add_score("Jess", 1000, "jump") # diff username
add_score("Rob", 5, "basic") # should not override 10
get_db()
add_score("Rob", 100, "basic") #override dbScore
add_score("Rob", 100, "jump") #diff mode
get_db()
print(top_n(3, "jump"))
"""
