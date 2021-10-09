from flask import Flask, render_template, request, redirect, make_response, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email
from reg_form import RegForm, LoginForm



def login_accept_function(form):
    email = form.email.data
    password = form.password.data

    # print(email)
    # print(password)
    # здесь логика базы данных
    # print("\nData received. Now redirecting ...")
    return redirect(url_for('index'))


application = Flask(__name__)

application.config['SECRET_KEY'] = 'secret key'

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/registration', methods=['get', 'post'])
def register():
    form = RegForm()
    return render_template('register.html', title='Register', form=form)

@application.route('/login', methods=['get', 'post'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        login_accept_function(form)

    return render_template('login.html', form=form)

@application.route('/books/<genre>')
def books(genre):
    return f"All Books in {genre} category"

if __name__ == "__main__":
    application.run(host='0.0.0.0')