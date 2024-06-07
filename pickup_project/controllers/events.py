from flask import render_template,redirect,request,session,flash
from pickup_project import app
from pickup_project.models.event import Event

@app.route('/create/event')
def create_event():
    
    return render_template('create_event.html')