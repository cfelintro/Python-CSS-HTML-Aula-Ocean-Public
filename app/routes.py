from app import app
from flask import render_template, request


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Caio'}
    posts = [
        {'autor' : {'username':'Maria'}, 'body': 'Olá da Maria'},
        {'autor' : {'username':'Caio'}, 'body': 'Ola'}
    ]

    return render_template("index.html", user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'] )
def login():
    if request.method == 'POST':
        print(request.values.get('user'), request.values.get('pass'), request.values.get('remember'))
    return render_template("login.html", title='Login')