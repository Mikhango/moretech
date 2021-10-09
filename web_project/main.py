from flask import Flask, render_template, request, redirect, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email
from reg_form import RegForm, LoginForm


application = Flask(__name__)

application.config['SECRET_KEY'] = 'secret key'

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/registration')
def register():
    form = RegForm()
    return render_template('register.html', title='Register', form=form)

@application.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Log in', form=form)

@application.route('/books/<genre>')
def books(genre):
    return f"All Books in {genre} category"

if __name__ == "__main__":
    application.run(host='0.0.0.0')