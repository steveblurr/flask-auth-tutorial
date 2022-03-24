from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db


auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    # --- LOGIN LOGIC CODE HERE --- #
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # --- LOGIC TO CHECK IF USER DOES EXIST IN DB --- #
    # --- ALSO TAKES THE USER SUPPLIED PASSWORD - HASHES IT - COMPARES HASHES W/ DB ENTRY --- #
    if not user or not check_password_hash(user.password, password):
        flash('Please Check Your Login Details And Try Again.')
        return redirect(url_for('auth.login'))

    # --- IF ABOVE CHECK PASSES - WE KNOW USER HAS THE RIGHT CREDENTIALS --- #
    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))


@auth.route('/signup')
def signup():
    return render_template('signup.html')


@auth.route('/signup', methods=['POST'])
def signup_post():
    # ----- CODE TO VALIDATE AND ADD USER TO DB ----
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    # --- RETURNS USER - IF USER ALREADY EXISTS  - THEREFORE EMAIL EXISTS IN DB
    user = User.query.filter_by(email=email).first()

    if user:  # --- IF A USER IS FOUND, REDIRECT TO SIGNUP PAGE - SO USER TRIES AGAIN
        flash('Email Address Already Exists')
        return redirect(url_for('auth.signup'))

    # --- CREATE A NEW USER WITH THE FORM DATA --- #
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    # --- ADDS THE NEW USER TO THE DB --- #
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))