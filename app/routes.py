from flask import render_template, request
from app import app
from app.forms import LoginForm, RegistrationForm
from flask import render_template, flash, redirect, url_for

from flask_login import current_user, login_user
import sqlalchemy as sa
from app import db
from app.models import User
from flask_login import logout_user, login_required
from urllib.parse import urlsplit

@app.route('/')
@app.route('/index')
@login_required
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
    return render_template('index.html', title='Home', posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = LoginForm()
    
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data))
        
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password', 'error')
            return redirect(url_for('login'))
        
        login_user(user, remember=form.remember_me.data)

        #An attacker could insert a URL to a malicious site 
        # in the next argument, so the application only redirects 
        # when the URL is relative, which ensures that the redirect 
        #  within the same site as the application. To determine if the 
        # URL is absolute or relative, I parse it with Python's 
        # urlsplit() function and then check if the netloc component is set or not.
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('index')
        
        return redirect(next_page)
    
    # For GET requests or form validation failure, render the login form
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
