from app import app
from flask import request, render_template, url_for, redirect, flash
from flask_login import login_required, current_user, logout_user, login_user
from werkzeug.security import generate_password_hash, check_password_hash
from services.mapworker import MapWorker
from models import User
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


@app.route('/recognizer')
@login_required
def recognizer():
    return render_template('recognizer.html', name=current_user.name)
