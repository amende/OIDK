from flask import Flask, redirect,request,render_template




app=Flask(__name__)

@app.route('/')
def indexPage():
        return(render_template("home.html"))





@app.route('/auth')
def auth():
        return(render_template("loginServ.html"))