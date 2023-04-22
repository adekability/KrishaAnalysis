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
    street = db.Column(db.String)
    house_num = db.Column(db.String)
    date = db.Column(db.String)

    def __init__(self, price, rooms, is_mortgaged, building, building_type, count_of_floor, square, priv_dormitory, renovation, telephone_type, internet_type, bathroom_type, balcony, balcony_glazed, door_type, parking, furniture, floor_type, ceiling_height, security, map_complex, has_change, city, district, street, house_num, date):
        self.price = price
        self.rooms = rooms
        self.is_mortgaged = is_mortgaged
        self.building = building
        self.building_type = building_type
        self.count_of_floor = count_of_floor
        self.square = square
        self.priv_dormitory = priv_dormitory
        self.renovation = renovation
        self.telephone_type = telephone_type
        self.internet_type = internet_type
        self.bathroom_type = bathroom_type
        self.balcony = balcony
        self.balcony_glazed = balcony_glazed
        self.door_type = door_type
        self.parking = parking
        self.furniture = furniture
        self.floor_type = floor_type
        self.ceiling_height = ceiling_height
        self.security = security
        self.map_complex = map_complex
        self.has_change = has_change
        self.city = city
        self.district = district
        self.street = street
        self.house_num = house_num
        self.date = date
