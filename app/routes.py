from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Caio'}
    posts = [
        {'autor' : {'username':'Maria'}, 'body': 'Olá da Maria'},
        {'autor' : {'username':'Caio'}, 'body': 'Ola'}
    ]

    return render_template("index.html", user=user, posts=posts)