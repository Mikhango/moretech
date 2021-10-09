from flask import Flask, render_template, request, redirect, make_response, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email
from reg_form import RegForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import LoginManager, UserMixin, login_required
from sqlalchemy import MetaData, Table, String, Integer, Column, Text, DateTime, Boolean, engine
from sqlalchemy import insert, select

application = Flask(__name__)

application.config['SECRET_KEY'] = 'secret key'
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(application)

metadata = MetaData()

users = Table('blog', metadata,
    Column('id', Integer(), primary_key=True),
    Column('name', String(100), nullable=False),
    Column('surname', String(100),  nullable=False),
    Column('email', String(100),  nullable=False),
    Column('password    ', Text(), nullable=False),
    Column('created_on', DateTime(), default=datetime.now),
    Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)
)

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/register', methods=['get', 'post'])
def register():
    form = RegForm()
    if request.method == 'POST' and form.validate_on_submit():

        email = form.email.data
        password = form.password.data
        name = form.name.data
        surname = form.surname.data

        try:
            ins = users.insert().values(
                name = 'Dmitriy',
                surname = 'Yatsenko',
                email = 'moseend@mail.com',
                password = '123'
            )
            conn = engine.connect()
            r = conn.execute(ins)

            return redirect(url_for('login'))
        except Exception as e:
            print(e)

    return render_template('register.html', form=form)

@application.route('/login', methods=['get', 'post'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        conn = engine.connect()

        s = select([users])
        r = conn.execute(s)
        print(r.fetchall())

    else:
        return render_template('login.html', title='Login', form=form)

@application.route('/cabinet')
def cabinet():
    return render_template('cabinet.html')

@application.route('/books/<genre>')
def books(genre):
    return f"All Books in {genre} category"

if __name__ == "__main__":
    application.run(host='0.0.0.0')