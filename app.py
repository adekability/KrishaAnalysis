""" app - main module """
from flask import Flask
from flask_migrate import Migrate
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app.db')
app.config['SECRET_KEY'] = 'your secret key'

from views import *

if __name__ == "__main__":
    app.run()
