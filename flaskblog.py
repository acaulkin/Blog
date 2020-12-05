# Driver code for website.
# Calls Flask class from flask, and uses
# its built in functions to produce the site
# along with some basic python code. 

from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'b8d5d21266873aa3c6c92ba47a8365a3'

# Example Blog Postings 
posts = [
    {
        'author': 'Andrew Caulkins',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'December 4, 2020'
    } ,
    {   'author': 'Jane Doe',
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

# About Page
@app.route('/about/') 
def about():
    return render_template('about.html', title='About')
    
 # Registration Form
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
            flash(f'Account created for {form.username.data}!', 'success')
            return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)
    
# Login Page
@app.route('/login', methods=['GET', 'POST']) 
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful, please check username and password','danger')
    return render_template('login.html', title='Login', form=form)


# Below is only true when running script directly
# from Python; useful for implementing small changes
if __name__ == '__main__':
    app.run(debug=True)