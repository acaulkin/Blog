# Driver code for website.
# Calls Flask class from flask, and uses
# its built in functions to produce the site
# along with some basic python code. 

from flask import Flask, render_template, url_for
app = Flask(__name__)


# Blog postings dictionary
posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    } ,
    {   'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]



@app.route('/') # Root page of website
@app.route('/home')
def home():
    return render_template('home.html', posts=posts, title='Home')


@app.route('/about/') # about page of website
def about():
    return render_template('about.html', title='About')
    


# Below is only true when running script directly
# from Python; useful for implementing small changes
if __name__ == '__main__':
    app.run(debug=True)