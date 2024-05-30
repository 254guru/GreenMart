from flask import Flask, request, jsonify, render_template, redirect, url_for, flash, session
from app import app, db
from app.models import  User 
from app.users import bp, bcrypt
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length,  EqualTo


class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already exists. Please choose a different email.', 'danger')
            return redirect(url_for('user.signup'))

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # Check if the user is signing up as an admin
        if form.is_admin.data:
            role = 'admin'
        else:
            role = 'customer'

        new_user = User(username=username, email=email, password=hashed_password, role=role)
        db.session.add(new_user)
        db.session.commit()
        flash('Account created successfully! You can now log in.', 'success')
        return redirect(url_for('user.login'))
    else:
        print(form.errors)
    return render_template('signup.html', form=form)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()
        if user:
            valid_password = bcrypt.check_password_hash(user.password, password)
            if valid_password:
                session['user_id'] = user.id
                flash('Logged in successfully!', 'success')
                if user.role == 'admin':
                    return redirect(url_for('admin.dashboard'))
                else:
                    return redirect(url_for('index'))
            else:
                flash('Invalid email or password. Please try again.', 'danger')
        else:
            flash('Invalid email or password. Please try again.', 'danger')
    return render_template('login.html', form=form)

@bp.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))