import os
from flask import Flask
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView



app = Flask(__name__)


#bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://app_fqsv_user:hneVmfUWdUFCiWK586NzKD4JJX0YwhT8@dpg-cpaadjv109ks73al8cag-a.oregon-postgres.render.com/app_fqsv'

# postgres://app_fqsv_user:hneVmfUWdUFCiWK586NzKD4JJX0YwhT8@dpg-cpaadjv109ks73al8cag-a.oregon-postgres.render.com/app_fqsv
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'c328ef68141cff6e6166915d3cefe'

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app.models import User, Product, Order, OrderItem, Category
    
admin = Admin(app, name='Admin Panel', template_mode='bootstrap3')
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Product, db.session))
admin.add_view(ModelView(Order, db.session))
admin.add_view(ModelView(OrderItem, db.session))
admin.add_view(ModelView(Category, db.session))
    
from app.products import bp as products_bp
from app.users import bp as user_bp
from app.orders import bp as order_bp
from app.context_processors import inject_cart
    
app.register_blueprint(products_bp, url_prefix='/products')
app.register_blueprint(user_bp, url_prefix='/users', name='user_bp')
app.register_blueprint(order_bp, url_prefix='/orders')
app.context_processor(inject_cart)

    

from app import route
    



