from flask_login import UserMixin
from extensions import db


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String)

    def __init__(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name


class Parameter(db.Model):
    __tablename__ = "parameters"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.String)
    rooms = db.Column(db.String)
    is_mortgaged = db.Column(db.String)
    building = db.Column(db.String)
    building_type = db.Column(db.String)
    count_of_floor = db.Column(db.String)
    square = db.Column(db.String)
    priv_dormitory = db.Column(db.String)
    renovation = db.Column(db.String)
    telephone_type = db.Column(db.String)
    internet_type = db.Column(db.String)
    bathroom_type = db.Column(db.String)
    balcony = db.Column(db.String)
    balcony_glazed = db.Column(db.String)
    door_type = db.Column(db.String)
    parking = db.Column(db.String)
    furniture = db.Column(db.String)
    floor_type = db.Column(db.String)
    ceiling_height = db.Column(db.String)
    security = db.Column(db.String)
    map_complex = db.Column(db.String)
    has_change = db.Column(db.String)
    city = db.Column(db.String)
    district = db.Column(db.String)
