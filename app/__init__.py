from flask import Flask, render_template, redirect, url_for, request, session
import os

app = Flask(__name__)    #create Flask object
app.secret_key = os.urandom(32) #create random key
  
@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")
    
@app.route('/play')
def play():
    return render_template("play.html")
    
@app.route('/login')
def login():
    return render_template("login.html")
    
@app.route('/logout')
def logout():
    return render_template("logout.html")
    
@app.route('/leaderboard')
def leaderboard():
    return render_template("leaderboard.html")
    
@app.route('/settings')
def settings():
    return render_template("settings.html")
  
if __name__ == "__main__":
    app.debug = True
    app.run()
