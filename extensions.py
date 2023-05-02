from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from app import app
from flask_admin import Admin
from flask_caching import Cache
from flask_babel import Babel


babel = Babel()
babel.init_app(app)
login_manager = LoginManager(app)

db = SQLAlchemy()
db.init_app(app)
migrate = Migrate(app, db)
admin = Admin(name='Админ-панель', template_mode='bootstrap3')
admin.init_app(app)