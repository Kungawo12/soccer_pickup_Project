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
def new_matches():
    data = {
        'name': request.form['name'],
        'location_name': request.form['location_name'],
        'date': request.form['date'],
        'user_id': session['user_id']
    }
    Event.insert_new(data)
    return redirect('/dashboard')

@app.route('/show/event/<int:id>')
def show_event(id):
    data = {
        'id': id
    }
    event = Event.get_one_event(data)
    return render_template('show_event.html',event=event)

@app.route('/edit/event/<int:id>')
def edit_event(id):
    user_data = {
        'id': session['user_id']
    }
    data ={
        'id': id
    }
    user = User.get_one_user(user_data)
    event = Event.get_one_event(data)
    return render_template('edit_event.html',user=user,event=event)

@app.route('/update/event/<int:id>',methods=['POST'])
def update_event(id):
    data = {
        "id": id,
        'name': request.form['name'],
        'location_name': request.form['location_name'],
        'date': request.form['date']
    }
    Event.update_event(data)
    return redirect('/dashboard')

@app.route('/delete/event/<int:id>')
def delete_event(id):
    data = {
        'id': id
    }
    Event.delete_event(data)
    return redirect('/dashboard')