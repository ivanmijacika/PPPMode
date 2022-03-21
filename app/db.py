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
    	
def top_n(n, mode):
    '''Gets the top n scores and users, Returns a tuple of 2 lists'''
    
    db = sqlite3.connect(DB_file)
    c = db.cursor()
    highscore_name = "highscore_" + mode
    
    c.execute("SELECT {mode} FROM scores ORDER BY {mode} DESC".format(mode = highscore_name))
    n_scores = []
    for i in range(n):
        ith_score = c.fetchone()
        # scores exists, not NoneType
        if ith_score:
            n_scores.append(ith_score[0])
        # no score in this place, fill with holder
        else:
            n_scores.append("-")
    
    c.execute("SELECT {user} FROM scores ORDER BY {mode} DESC".format(user= "usernames", mode = highscore_name))
    n_users = []
    for i in range(n):
        ith_user = c.fetchone()
        # user exists, not NoneType
        if ith_user:
            n_users.append(ith_user[0])
        # no user in this place, filled with holder
        else: 
            n_users.append("-")

    # in case a user has a row but no score in this mode, it's score is None; name and score to be chnaged to holder
    for i in range(n):
        if n_scores[i] == None:
            n_scores[i] = "-"
            n_users[i] = "-"

    return(n_scores, n_users)

def get_user_scores(user): 
    db = sqlite3.connect(DB_file)
    c = db.cursor()

    c.execute("SELECT * FROM scores WHERE usernames = ?", (user,))
    ''' usernames, basic, obstacles, flying, wrap, peace, jump, poison'''
    scores = c.fetchall()
    # username has row in db, gets it, turns any 'None' into 0
    if scores:
        scores = list(scores[0])
        for i in range(len(scores)):
            if scores[i] == None:
                scores[i] = 0
    # username does not have row in db yet 
    else: 
        scores = [user, 0, 0, 0, 0, 0, 0, 0]
    # print(scores)
    return scores

# for testing & debugging purposes
def get_db():
    db = sqlite3.connect(DB_file)
    c = db.cursor()

    c.execute("SELECT * from scores")
    print(c.fetchall())

    db.close()

'''
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

# add_score("J", 5, "basic")
add_score("Tom", 15, "basic")
get_db()
'''

#get_user_scores("Rob")