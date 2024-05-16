from flask import render_template,request, redirect,session,flash
from pickup_project import app

@app.route('/')
def home_page():
    return render_template('home.html')