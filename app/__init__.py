import os
from flask import Flask
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager



app = Flask(__name__)


#bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://app_fqsv_user:hneVmfUWdUFCiWK586NzKD4JJX0YwhT8@dpg-cpaadjv109ks73al8cag-a.oregon-postgres.render.com/app_fqsv'

# postgres://app_fqsv_user:hneVmfUWdUFCiWK586NzKD4JJX0YwhT8@dpg-cpaadjv109ks73al8cag-a.oregon-postgres.render.com/app_fqsv
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'c328ef68141cff6e6166915d3cefe'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
#login_manager = LoginManager(app)
#login_manager.login_view = 'user.login'
#login_manager.init_app(app)
#from app.models import User

#@login_manager.user_loader
#def load_user(user_id):
   # return User.get(user_id)


# Register blueprints here
from app.products import bp as products_bp
from app.users import bp as user_bp
from app.orders import bp as order_bp

app.register_blueprint(products_bp)
app.register_blueprint(user_bp)
app.register_blueprint(order_bp)

from app import route



