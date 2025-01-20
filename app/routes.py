from flask import render_template
from app import app
from app.forms import LoginForm
from flask import render_template, flash, redirect, url_for

@app.route('/')
@app.route('/index')

def index():
    user = {'username': 'Ostap'}
    posts = [
        {
            'author': {'username': 'Danya'},
            'body': 'Beautiful day in Ukraine!'
        },
        {
            'author': {'username': 'Annie'},
            'body': 'Better day in Zhytomyr!'
        },
        {
            'author':{'username':'Alex'},
            'body':'Agreed, Annie!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
