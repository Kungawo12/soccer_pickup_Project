from flask import render_template,request, redirect,session,flash
from pickup_project import app
from pickup_project.models.user import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/login_register')
def register_page():
    return render_template('register.html')

@app.route('/user/register', methods=['POST'])
def register_user():
    # if not User.validate_user(request.form):
    #     return redirect('/register')
    
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    user_id = User.insert(data)
    session['user_id'] = user_id
    return redirect('/dashboard')

@app.route('/user/login', methods=['POST'])
def login_user():
    data = {
        "email": request.form['email'],
        "password": request.form['password']
    }
    user = User.get_by_email(data)
    # if not user:
    #     flash("Invalid credentials")
    #     return redirect('/login')
    session['user_id'] = user.id
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    from pickup_project.models.event import Event
    data = {
        'id': session['user_id']
    }
    users =User.get_all_users()
    user_events = Event.get_all_events()
    return render_template('dashboard.html',user=User.get_one_user(data), users=users, user_events=user_events)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
    
    