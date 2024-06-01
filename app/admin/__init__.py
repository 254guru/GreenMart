from flask import Blueprint

admin_custom_bp = Blueprint('admin_custom', __name__)

from app.admin import admin