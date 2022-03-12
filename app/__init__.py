# PPP Mode: Ivan Mijacika, Qina Liu, Justin Morrill, Noakai Aronesty
# SoftDev pd2
# P02 -- Snake++

from os import urandom
from flask import Flask, render_template, request, session, redirect, url_for
from auth import *
from db import *
import sqlite3

app = Flask(__name__)    #create Flask object
app.secret_key = urandom(32) #create random key
  
@app.route('/')
@app.route('/home')
def home():
    ''' Loads the landing page '''
    return render_template("home.html")
    
@app.route('/play')
def play():
    return render_template("play.html")
    
@app.route('/login')
def login():
    ''' Displays login page '''
    return render_template("login.html")

@app.route("/register")
def register():
    ''' Displays register page '''
    return render_template('register.html')
    
@app.route('/leaderboard')
def leaderboard():
    return render_template("leaderboard.html")
    
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
# for testing add_score, rm db before testing tho
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
if __name__ == "__main__":
    app.debug = True
    app.run()
