from extensions import *
from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView
from flask_login import current_user
from models import *


@babel.localeselector
def get_locale():
    return 'ru'


class UserModelView(ModelView):
    column_labels = dict(id='ID',
                         email="Почта",
                         password="Пароль",
                         name="Имя")

    def is_accessible(self):
        return current_user.is_authenticated


class ParameterModelView(ModelView):
    pass

    def is_accessible(self):
        return current_user.is_authenticated


class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated


admin.index_view = MyAdminIndexView()
admin.add_view(UserModelView(User, db.session, 'Пользователи'))
admin.add_view(ParameterModelView(Parameter, db.session, 'Параметры'))
