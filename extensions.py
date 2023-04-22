from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from app import app

login_manager = LoginManager(app)

db = SQLAlchemy()
db.init_app(app)

migrate = Migrate(app, db)
