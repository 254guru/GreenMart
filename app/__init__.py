from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager
import datetime

# Initialize Flask extensions
db = SQLAlchemy()
migrate = Migrate()

app = Flask(__name__)

# Configure app settings
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://app_fqsv_user:hneVmfUWdUFCiWK586NzKD4JJX0YwhT8@dpg-cpaadjv109ks73al8cag-a.oregon-postgres.render.com/app_fqsv'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'c328ef68141cff6e6166915d3cefe'

# Initialize Flask extensions with the app
db.init_app(app)
migrate.init_app(app, db)
#login_manager = LoginManager(app)



# Register blueprints
from app.products import bp as products_bp
from app.users import bp as user_bp
from app.orders import bp as order_bp
from app.admin import admin_custom_bp
from app.route import bp as main_bp

app.register_blueprint(products_bp, url_prefix='/products')
app.register_blueprint(user_bp, url_prefix='/users', name='user_bp')
app.register_blueprint(orders_bp, url_prefix='/orders')
app.register_blueprint(admin_custom_bp, url_prefix='/admin_custom')
app.register_blueprint(main_bp)

# Initialize Flask-Admin
admin = Admin(app, name='Admin panel', template_mode='bootstrap3')

# Import models for Flask-Admin views
from app.models import User, Product, Order, OrderItem, Category

# Add Flask-Admin views
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Product, db.session))
admin.add_view(ModelView(Order, db.session))
admin.add_view(ModelView(OrderItem, db.session))
admin.add_view(ModelView(Category, db.session))

# Import routes
from app import route
