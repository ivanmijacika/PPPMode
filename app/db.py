# PPP Mode: Ivan Mijacika, Qina Liu, Justin Morrill, Noakai AronestyS
# SoftDev pd2
# P02 -- Snake++

import sqlite3

DB_file = "discobandit.db"

def add_score(username, score):
    '''Adds a new highscore to the database'''
    
    db = sqlite3.connect(DB_file)
    c = db.cursor
    
    c.execute("SELECT usernames FROM scores")
    users = []
    for a_tuple in c.fetchall():
        users.append(a_tuple[0])
    
    if username in users:
    	c.execute("SELECT highscores FROM scores WHERE usernames = username")
    	if score > c.fetchone():
            c.execute("UPDATE scores SET highscores WHERE usernames = username")
    else:
    	c.execute("INSERT INTO scores VALUES (?, ?);")
