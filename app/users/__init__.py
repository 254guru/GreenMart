from flask import Blueprint
from flask_bcrypt import Bcrypt
bp = Blueprint('user', __name__)
bcrypt = Bcrypt()


from app.users import user