from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy


application = Flask(__name__)


@application.route('/')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    application.run(host='0.0.0.0')