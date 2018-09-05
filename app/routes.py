from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index(): 
    user = {'username' : 'Sergio'}
    posts = [
        {
            'author': {'username': 'LeBron'},
            'body': 'Beautiful day in Los Angeles!'
        },
        {
            'author': {'username': 'Amanda'},
            'body': 'Sorry to Bother You was a good movie!'
        },
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if (form.validate_on_submit()):
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data
        ))
        # Todo: add error message when validation fails
        return redirect('/index')

    return render_template('login.html', title='Sign In', form=form)
