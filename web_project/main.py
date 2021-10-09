from flask import Flask, render_template, request, redirect, make_response, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email
from reg_form import RegForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash


logged = False


application = Flask(__name__)

application.config['SECRET_KEY'] = 'secret key'
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

db = SQLAlchemy(application)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)

    def __repr__(self) -> str:
        return f'<Users {self.id}>'


@application.route('/')
def index():
    return render_template('index.html')

@application.route('/register', methods=['get', 'post'])
def register():
    form = RegForm()
    if form.validate_on_submit():

        email = form.email.data
        password = form.password.data
        name = form.name.data
        surname = form.surname.data

        user = Users(name=name, surname=surname, email=email, password=generate_password_hash(password))

        try:
            db.session.add(user)
            db.session.commit()

            return redirect(url_for('login'))
        except:
            return 'Error'

    return render_template('register.html', form=form)

@application.route('/login', methods=['get', 'post'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        curs = db.cursor()
        info = curs.execute('SELECT * FROM users WHERE email=? password=?', (email, generate_password_hash(password)))
        if info.fetchone() is None:
            return redirect(url_for('register'))
        else:
            return redirect(url_for('cabinet'))
    else:
        return render_template('login.html', title='Login', form=form)

@application.route('/')
def cabinet():
    return render_template('cabinet.html')

@application.route('/books/<genre>')
def books(genre):
    return f"All Books in {genre} category"

if __name__ == "__main__":
    application.run(host='0.0.0.0')