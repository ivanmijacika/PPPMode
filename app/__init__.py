from flask import Flask, render_template, redirect, url_for, request, session
import os

app = Flask(__name__)    #create Flask object
app.secret_key = os.urandom(32) #create random key
  
@app.route('/')
def home():
    return("Hello, world!")
    
  
if __name__ == "__main__":
    app.debug = True
    app.run()
