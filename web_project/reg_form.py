from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email

class RegForm(FlaskForm):
    name = StringField("Name: ", validators=[DataRequired()])
    surname = StringField("Surame: ", validators=[DataRequired()])
    email = StringField("Email: ", validators=[Email()])
    password = StringField("Password: ", validators=[DataRequired()])
    submit = SubmitField("Submit")

class LoginForm(FlaskForm):
    email = StringField("Email: ", validators=[Email()])
    password = StringField("Password: ", validators=[DataRequired()])
    submit = SubmitField("Submit")

class DataForm(FlaskForm):
    users = StringField("First table: ", validators=[DataRequired()])
    ussame = StringField("Second table: ", validators=[DataRequired()])
    submit = SubmitField("Submit")