from flask import Flask, redirect,request,render_template




app=Flask(__name__)


@app.route('/auth')
def hello():
        return(render_template("loginServ.html"))