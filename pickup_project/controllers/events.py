from flask import render_template,redirect,request,session,flash
from pickup_project import app
from pickup_project.models.event import Event
from pickup_project.models.user import User

@app.route('/create/event')
def create_event():
    data = {
        'id' : session['user_id']
    }
    user = User.get_one_user(data)
    return render_template('new_event.html',user=user)

@app.route('/new/event',methods=['POST'])
def insert_new():
    data = {
        'name': request.form['name'],
        'location_name': request.form['location_name'],
        'date': request.form['date'],
    }
    Event.insert_new(data)
    return redirect('/dashboard')