from flask import request, jsonify, render_template, redirect, url_for, flash, session
from app import db
from app.users import bcrypt, bp
from app.models import User
from flask_login import login_user, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    is_admin = StringField('Are you an admin?')
    submit = SubmitField('Sign Up')


@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    """
    This route handles the creation of a new user account. It processes a POST request
    to create a new user account with the provided details. If the email already exists,
    the user is notified to choose a different email. If the account is created successfully,
    the user is redirected to the login page.
    """
    form = SignupForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already exists. Please choose a different email.', 'danger')
            return redirect(url_for('user_bp.signup'))

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        role = 'admin' if form.is_admin.data else 'customer'

        new_user = User(username=username, email=email, password=hashed_password, role=role)
        db.session.add(new_user)
        db.session.commit()
        flash('Account created successfully! You can now log in.', 'success')
        return redirect(url_for('user_bp.login'))
    return render_template('login.html', form=form)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    """
    This route handles user login. It processes a POST request to authenticate the user
    based on the provided email and password. If the user is authenticated successfully,
    they are redirected to the main page. If the user is not authenticated, an error
    message is displayed.
    """
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['role'] = user.role
            flash('Logged in successfully!', 'success')
            if user.role == 'admin':
                return redirect(url_for('admin_custom.index'))
            else:
                return redirect(url_for('main.index'))
        else:
            flash('Invalid email or password. Please try again.', 'danger')
    return render_template('login.html', form=form)


@bp.route('/logout')
def logout():
    """
    This route handles user logout. It clears the session data and redirects the user
    to the main page with a logout message.
    """
    session.pop('user_id', None)
    session.pop('role', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('main.index'))