from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index(): 
    user = {'username': 'JRod'}
    posts = [
        {
            'author': {'username': 'Billy'},
            'body': 'Excellent form, Mrs. Wheeler.'
        },
        {
            'author': {'username': 'El'},
            'body': "Friends don't lie."
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)