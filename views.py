from app import app
from flask import request, render_template, url_for, redirect, flash
from flask_login import login_required, current_user, logout_user, login_user
from werkzeug.security import generate_password_hash, check_password_hash
from services.mapworker import MapWorker
from models import User, Parameter
from extensions import db, login_manager


@app.route('/login')
def login():
    return render_template('login.html')


@login_manager.user_loader
def load_user(user):
    return User.query.get(int(user))


@app.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('login'))

    login_user(user, remember=remember)
    return redirect(url_for('recognizer'))


@app.route('/signup')
def signup():
    return render_template('register.html')


@app.route('/signup', methods=['POST'])
def signup_post():

    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    if user:
        flash('Email address already exists')
        return redirect(url_for('signup'))

    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('login'))


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route("/map", methods=['GET'])
def get_map():
    """ get_map - main function"""
    longitude = float(request.args.get("lon"))
    latitude = float(request.args.get("lat"))
    return MapWorker(longitude=longitude,
                     latitude=latitude).fetch_map_by_coordinates()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/recognizer', methods=['GET'])
@login_required
def recognizer():
    return render_template('recognizer.html', name=current_user.name)


@app.route('/recognizer', methods=['POST'])
@login_required
def post_recognizer():
    price = request.form.get('price')
    rooms = request.form.get('rooms')
    is_mortgaged = request.form.get('is_mortgaged')
    building = request.form.get('building')
    building_type = request.form.get('building_type')
    count_of_floor = request.form.get('count_of_floor')
    square = request.form.get('square')
    priv_dormitory = request.form.get('priv_dormitory')
    renovation = request.form.get('renovation')
    telephone_type = request.form.get('telephone_type')
    internet_type = request.form.get('internet_type')
    bathroom_type = request.form.get('bathroom_type')
    balcony = request.form.get('balcony')
    balcony_glazed = request.form.get('balcony_glazed')
    door_type = request.form.get('door_type')
    parking = request.form.get('parking')
    furniture = request.form.get('furniture')
    floor_type = request.form.get('floor_type')
    ceiling_height = request.form.get('ceiling_height')
    security = request.form.get('security')
    map_complex = request.form.get('map_complex')
    has_change = request.form.get('has_change')
    city = request.form.get('city')
    district = request.form.get('district')
    street = request.form.get('street')
    house_num = request.form.get('house_num')
    date = request.form.get('date')

    parameter = Parameter(
        price=price,
        rooms=rooms,
        is_mortgaged=is_mortgaged,
        building=building,
        building_type=building_type,
        count_of_floor=count_of_floor,
        square=square,
        priv_dormitory=priv_dormitory,
        renovation=renovation,
        telephone_type=telephone_type,
        internet_type=internet_type,
        bathroom_type=bathroom_type,
        balcony=balcony,
        balcony_glazed=balcony_glazed,
        door_type=door_type,
        parking=parking,
        furniture=furniture,
        floor_type=floor_type,
        ceiling_height=ceiling_height,
        security=security,
        map_complex=map_complex,
        has_change=has_change,
        city=city,
        district=district,
        street=street,
        house_num=house_num,
        date=date
    )
    db.session.add(parameter)
    db.session.commit()

    return {"status": False}
