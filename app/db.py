# PPP Mode: Ivan Mijacika, Qina Liu, Justin Morrill, Noakai AronestyS
# SoftDev pd2
# P02 -- Snake++

import sqlite3

DB_file = "discobandit.db"

def add_score(username, score, mode):
    '''Adds a new highscore to the database'''
    highscore_name = "highscore_" + mode
    
    db = sqlite3.connect(DB_file)
    c = db.cursor()
    
    c.execute("SELECT usernames FROM scores;")
    users = []
    for a_tuple in c.fetchall():
        users.append(a_tuple[0])

    if username in users:
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
    '''
    if username in users:
        c.execute("SELECT (?) FROM scores WHERE usernames = (?);", (highscore_name, username))
        if score > c.fetchone():
            c.execute("UPDATE scores SET (?) = (?) WHERE usernames = (?);", (highscore_name, score, username))
        db.commit()
    else:
    	c.execute("INSERT INTO scores VALUES (?, ?, ?, ?, ?, ?, ?, ?);", (username, 0, 0, 0, 0, 0, 0, 0))
    	#c.execute("UPDATE scores SET (?) = (?) WHERE usernames = (?);", (highscore_name, score, username))
    	#c.execute("UPDATE scores SET highscore_basic = 7652 WHERE usernames = Robert;")
    '''

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

