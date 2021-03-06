# PPP Mode: Ivan Mijacika, Qina Liu, Justin Morrill, Noakai Aronesty
# SoftDev pd2
# P02 -- Snake++

from os import urandom
from flask import Flask, render_template, request, session, redirect, url_for, jsonify 
from auth import *
from db import *
import sqlite3

app = Flask(__name__)    #create Flask object
app.secret_key = urandom(32) #create random key
  
@app.route('/')
@app.route('/home')
def home():
    ''' Loads the landing page '''
    if 'username' in session: 
        ''' usernames, basic, obstacles, wrap, peace, flying, poison'''
        ''' <h4>Basic: {{basic}} </h4>
                    <h4>Obstacle: {{obstacle}} </h4>
                    <h4>Border Wrap: {{wrap}} </h4>
                    <h4>Peace: {{peace}} </h4>
                    <h4>Flying: {{flying}} </h4>
                    <h4>Flying: {{flying}} </h4>'''
        scores = list(get_user_scores(session['username']))
        '''
        for i in range(len(scores))[1:]:
            if scores[i] == None:
                scores[i] = 0
            elif scores[i] < 0:
                scores[i] = 0
        '''
        return render_template("home.html", basic = scores[1], obstacle = scores[2], wrap = scores[3], flying= scores[5], poison= scores[6])
    return render_template("home.html")

def set_settings():
    print("setting settings")
    session['speed'] = 'medium'
    session['size'] = 'medium'
    session['mode'] = 'basic'

@app.route('/play', methods = ['GET', 'POST'])
def play():
    method = request.method
    
    print(session)
    # if no settings are in session, then add default ones
    if not ('speed' in session):
        set_settings()

    # form data from settings.html 
    if method == 'POST':
        speed = request.form.get('gameSpeed')
        size = request.form.get('mapSize')
        mode = request.form.get('gameMode')
        # adjusts settings in session to what is requested in form
        session['speed'] = speed
        session['size'] = size
        session['mode'] = mode

        # testing 
        print(session['speed'])
        print(session['size'])
        print(session['mode'])


    return render_template("play.html", mode=session['mode'].capitalize())
    
@app.route('/login')
def login():
    ''' Displays login page '''
    return render_template("login.html")

@app.route("/register")
def register():
    ''' Displays register page '''
    return render_template('register.html')
    
@app.route('/leaderboard', methods = ['GET', 'POST'])
def leaderboard():
    # for testing
    get_db()

    # top_n returns tuple of lists 
    data = top_n(5, 'basic')
    scores = data[0]
    users = data[1]

    return render_template("leaderboard.html")
    #, score0=scores[0], score1 = scores[1], score2 = scores[2], score3 = scores[3], score4 = scores[4], user0 = users[0], user1 = users[1], user2 = users[2], user3 = users[3], user4 = users[4])

@app.route('/leaderboard_data', methods=['GET', 'POST'])
def leaderboard_data():
    method = request.method
    # print(method)

    #get mode from js, send back mode data to js
    if method == 'POST':
        #request.get_json gives dictionary; ex: {'mode': 'basic'}
        mode = request.get_json()['mode']
        # print(mode)
        data = top_n(5, mode)
        return jsonify(data)

@app.route('/score_data', methods = ['GET', 'POST'])
def score_data():
    method = request.method
    print(method)
    # js giving score 
    if method == 'POST':
        data = request.get_json()
        #print(data)
        username = data['username']
        score = data['score']
        mode = data['mode']
        #print(username, score, mode)
        add_score(username, score, mode)
        return jsonify("OK")


@app.route('/play_data')
def play_data():
    data = session
    return jsonify(data)

'''
@app.route('/play_data', methods=['GET', 'POST'])
def play_data():
    method = request.method
    print(method)

    #get mode from js, send back mode data to js
    if method == 'POST':
        # request.get_json gives dictionary; ex: {'mode': 'basic'}
         score = request.get_json()['score']
'''
        

@app.route('/settings')
def settings():
    return render_template("settings.html")
  
@app.route("/logout")
def logout():
    ''' Logout user by deleting user from session dict. Redirects to loginpage '''
    # Delete user. This try... except... block prevent an error from ocurring when the logout page is accessed from the login page
    try:
        session.pop('username')
    except KeyError:
        return redirect(url_for('home'))
    # Redirect to login page
    return redirect(url_for('home'))

# authetication of login
@app.route("/auth", methods=['GET', 'POST'])
def authenticate():
    ''' Checks whether method is get, post. If get method, then redirect to
       loginpage. If post, then authenticate the username and password, rendering
       the error page if incorrect and the response.html if correct username/pass. '''

    # Variables
    method = request.method
    username = request.form.get('username')
    password = request.form.get('password')

    # Get vs Post
    if method == 'GET':
        return redirect(url_for('home'))

    auth_state = auth_user(username, password)
    if auth_state == True:
        session['username'] = username
        return redirect(url_for('home'))
    elif auth_state == "bad_pass":
        return render_template('login.html', input="bad_pass")
    elif auth_state == "bad_user":
        return render_template('login.html', input="bad_user")

@app.route("/rAuth", methods=['GET', 'POST'])
def rAuthenticate():
    ''' Authentication of username and passwords given in register page from user '''

    method = request.method
    username = request.form.get('username')
    password0 = request.form.get('password0')
    password1 = request.form.get('password1')

    if method == 'GET':
        return redirect(url_for('register'))

    if method == 'POST':
        # error when no username is inputted
        if len(username) == 0:
            return render_template('register.html', given="username")
        # error when no password is inputted
        elif len(password0) == 0:
            return render_template('register.html', given="password")
        elif len(password0) < 8:
            return render_template('register.html', given="password greater than 8 characters")
        # a username and password is inputted
        # a username and password is inputted
        else:
            # if the 2 passwords given don't match, will display error saying so
            if password0 != password1:
                return render_template('register.html', mismatch=True)
            else:
                # creates user account b/c no fails
                if create_user(username, password0):
                    return render_template('login.html', input='success')
                # does not create account because create_user failed (username is taken)
                else:
                    return render_template('register.html', taken=True)

'''
add_score("Rob", 0, "basic")
add_score("Rob1", 100, "basic")
add_score("Rob1", 100, "poison")
add_score("Rob1", 100, "peace")
add_score("not Rob", 100, "poison")
'''

if __name__ == "__main__":
    app.debug = True
    app.run()
