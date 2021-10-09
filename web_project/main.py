from flask import Flask, render_template, request, redirect, make_response, url_for, flash, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
# from werkzeug.datastructures import T
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email
from reg_form import RegForm, LoginForm, DataForm
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
from flask_login import LoginManager, UserMixin, login_required
from sqlalchemy import MetaData, Table, String, Integer, Column, Text, DateTime, Boolean, engine, insert, select
import sqlite3

application = Flask(__name__)


conn = sqlite3.connect('users.db')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS user(
   userid INT PRIMARY KEY,
   fname TEXT,
   lname TEXT,
   email TEXT,
   password TEXT);
""")
conn.commit()
conn.close()

application.config['SECRET_KEY'] = 'secret key'
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(application)

db.create_all()

def add_column(engine, table_name, column):
    column_name = column.compile(dialect=engine.dialect)
    column_type = column.type.compile(engine.dialect)
    engine.execute('ALTER TABLE %s ADD COLUMN %s %s' % (table_name, column_name, column_type))


class User(db.Model):
    userid = db.Column(db.Integer, primary_key = True)
    fname = db.Column(db.String(100), nullable = False)
    lname = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100), nullable = False)
    password = db.Column(db.String(100), nullable = False)

    #def __repr__(self):
    #    return '(<User %r>)' % self.id

#class NewTable(db.Model):
#    new_test_key = db.Column(db.String(100), nullable = False)

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/register', methods=['get', 'post'])
def register():
    form = RegForm()
    if request.method == 'POST' and form.validate_on_submit():

        email = form.email.data
        password = form.password.data
        fname = form.name.data
        lname = form.surname.data

        dann = User(fname=fname, lname=lname, email=email, password=generate_password_hash(password))

        try:
            db.session.add(dann)
            db.session.commit()

            return redirect(url_for('login'))
        except Exception as e:
            print(repr(e))
            return ''
    else:
        return render_template('register.html', form=form)

@application.route('/login', methods=['get', 'post'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        '''
        try:
            print(1)
            all_dann = db.session.query(User).filter_by(email=email).first()[0]
            print(f'... all_dann: {all_dann}')
            if all_dann is not None:
                print(all_dann)
                if check_password_hash(all_dann.password) == password:
                    return redirect(url_for('cabinet'))

            return redirect(url_for('login'))
        except Exception as e:
            print(repr(e))
            return ''
        '''
        return redirect(url_for('cabinet'))

    else:
        return render_template('login.html', title='Login', form=form)

@application.route('/cabinet', methods=['get', 'post'])
def cabinet():
    form = DataForm()
    if request.method == 'POST' and form.validate_on_submit():
        '''
        users = form.users.data.split()
        ussame = form.ussame.data.split()
        for el in users:
            newcol = cur.execute(f"""SELECT {id} FROM users;""")
            column = Column(f'{el}', String(100), primary_key=True)
            # add_column(engine, NewTable, column)
        for el in ussame:
            newcol = cur.execute(f"""SELECT {id} FROM users;""")
            column = Column(f'{el}', String(100), primary_key=True)
            # add_column(engine, NewTable, column)
        '''

        # db.create_all()
        return redirect(url_for('download_file'))
    # print(cur.fetchall())
    else:
        return render_template('cabinet.html', title=cabinet, form=form)

@application.route('/profile/<genre>')
def profile(genre):
    return f"profile number: {genre}"


@application.route('/enter_db')
def download_file():
    return send_file('new_table.db')

@application.route('/personal_account')
def personal():
    return render_template('pers_account.html')

@application.route('/main')
def main_page():
    return render_template('main.html')

if __name__ == "__main__":
    application.run(host='0.0.0.0', debug=True)