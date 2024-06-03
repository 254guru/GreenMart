from flask import render_template, request, redirect, url_for, send_from_directory, session
from app import create_app
from app.orders import order
from flask import Blueprint

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    cart_items = order.fetch_cart()
   # print(cart_items)
    total_price = order.calculate_total_price()
    return render_template('index.html', cart_items=cart_items, total_price=total_price)


@bp.route('/categories')
def categories():
    return render_template('categories.html')

@bp.route('/blog')
def blog():
    return render_template('blog.html')

@bp.route('/profile')
def profile():
    return render_template('profile.html')

@bp.route('/static/CSS/style.css')
def serve_css():
    return send_from_directory('static', 'CSS/style.css')

@bp.route('/static/CSS/responsive.css')
def serve_responsive_css():
    return send_from_directory('static', 'CSS/responsive.css')

@bp.route('/static/CSS/login_form.css')
def serve_form_css():
    return send_from_directory('static', 'CSS/login_form.css')

@bp.route('/static/CSS/profile.css')
def serve_profile_css():
    return send_from_directory('static', 'CSS/profile.css')

@bp.route('/static/js/script.js')
def serve_js():
    return send_from_directory('static', 'js/script.js')

@bp.route('/static/js/login_form.js')
def serve_login_js():
    return send_from_directory('static', 'js/login_form.js')

@bp.route('/static/img/<filename>')
def get_image(filename):
    return send_from_directory('static/img', filename)