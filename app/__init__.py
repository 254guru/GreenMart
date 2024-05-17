import os
from flask import Flask
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)


#bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'c328ef68141cff6e6166915d3cefe'

db = SQLAlchemy(app)
migrate = Migrate(app, db)



from app import route
from app.users import bp as user_bp


app.register_blueprint(user_bp)