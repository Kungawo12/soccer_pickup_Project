from flask import render_template,request, redirect,session,flash
from pickup_project import app
from pickup_project.models.user import User

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/register')
def register_page():
    return render_template('register.html')

@app.route('/user/register', methods=['POST'])
def register_user():
    if not User.validate_user(request.form):
        return redirect('/register')
    
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": request.form['password']
    }
    user_id = User.insert(data)
    session['user_id'] = user_id
    return redirect('/dashboard')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/user/login', methods=['POST'])
def login_user():
    data = {
        "email": request.form['email'],
        "password": request.form['password']
    }
    user = User.get_user(data)
    if not user:
        flash("Invalid credentials")
        return redirect('/login')
    session['user_id'] = user.id
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    data = {
        'id': session['user_id']
    }
    users =User.get_all_users()
    return render_template('dashboard.html',user=User.get_one_user(data), users=users)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
    
    