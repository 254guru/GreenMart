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


@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    print('Signup route')
    form = SignupForm()
    if form.validate_on_submit():
        print('Form is valid')
        username = form.username.data
        email = form.email.data
        password = form.password.data

        # Check if the username or email is already registered
        existing_user = User.query.filter_by(email=email).first()
        print('checking existing user')
        if existing_user:
            flash('email already exists. Please choose a different email.', 'danger')
            print('Username already exists. Please choose a different username.')
            return redirect(url_for('user.signup'))


           # Hash the password before storing it in the database
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        print(hashed_password)

        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Account created successfully! You can now log in.', 'success')
        print('Account created successfully! You can now log in.')
        return redirect(url_for('user.login'))
    else:
        print(form.errors)  # Print form errors if validation fails
    return render_template('login.html', form=form)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email= form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()
        if user:

            valid_password = bcrypt.check_password_hash(user.password, password)
            if valid_password:
            

        #if user and valid_password ==True:
                session['user_id'] = user.id  # Store user ID in session
                flash('Logged in successfully!', 'success')
                return redirect(url_for('index'))
            else:
                flash('Invalid email or password. Please try again.', 'danger')
        else:
            flash('Invalid email or password. Please try again.', 'danger')
    return render_template('login.html', form=form)
  