from flask import Flask, render_template, redirect, url_for, request, session
import os

app = Flask(__name__)    #create Flask object
app.secret_key = os.urandom(32) #create random key

def user_info():
    username = session['username']
    # ~
    page_theme = getInfo(session['username'], "theme")
    # print(f"PAGE THEME:, {page_theme}")
    theme = updateTheme(page_theme, "light")
    # print(theme)
    home_widgets = updateWidget(session['username'])
    return username, theme, home_widgets

def logged_in():
    return "username" in session
  
@app.route('/')
@app.route("/home")
def home():
    return("Hello, world!")
    
  
if __name__ == "__main__":
    app.debug = True
    app.run()
