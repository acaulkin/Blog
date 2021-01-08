from flask import render_template, url_for, flash, redirect, request
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm, UpdateAccountForm
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

# Example blog postings
posts = [
    {
        'author': 'Andrew Caulkins',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'December 4, 2020'
    } ,
    {  
         'author': 'Trevor Sauve',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2025'
    }
]

# Root page of website
@app.route('/') 
@app.route('/home')
def home():
    return render_template('home.html', posts=posts, title='Home')

# About page
@app.route('/about/') 
def about():
    return render_template('about.html', title='About')
    
 # Registration form
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user = User(username = form.username.data, 
                        email = form.email.data, 
                        password = hashed_password)
            db.session.add(user)
            db.session.commit()
            flash('Your account has been created! You can now log into the blog.', 'success')
            return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
    
# Login page
@app.route('/login', methods = ['GET', 'POST']) 
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember = form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login unsuccessful, please check email and password','danger')
    return render_template('login.html', title = 'Login', form = form)

 # Logout route
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

 # Account route
@app.route("/account")
@login_required
def account():
    form = UpdateAccountForm()
    image_file = url_for('static', filename = 'profile_pics/' + current_user.image_file)
    return render_template('account.html', title = 'Account', image_file = image_file, form = form)






