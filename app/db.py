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
    	
def top_n(n):
    '''Gets the top n scores'''

# for testing & debugging purposes
def get_db():
    db = sqlite3.connect(DB_file)
    c = db.cursor()

    c.execute("SELECT * from scores")
    print(c.fetchall())

    db.close()
'''
# for testing add_score and get_score, rm db before testing tho
add_score("Rob", 10, "basic")
print(get_score("Rob", "basic"))
get_db()
add_score("Jess", 1000, "jump") # diff username
add_score("Rob", 5, "basic") # should not override 10
get_db()
add_score("Rob", 100, "basic") #override dbScore
add_score("Rob", 100, "jump") #diff mode
get_db()
'''
