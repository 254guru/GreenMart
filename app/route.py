from flask import render_template, request, redirect, url_for, send_from_directory, session
from app import app
from app.orders import order


@app.route('/')
def index():
    cart_items = order.fetch_cart()
    total_price = order.calculate_total_price()
    return render_template('index.html', cart_items=cart_items, total_price=total_price)


@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/static/CSS/style.css')
def serve_css():
    return send_from_directory('static', 'CSS/style.css')

@app.route('/static/CSS/responsive.css')
def serve_responsive_css():
    return send_from_directory('static', 'CSS/responsive.css')

@app.route('/static/CSS/login_form.css')
def serve_form_css():
    return send_from_directory('static', 'CSS/login_form.css')

@app.route('/static/CSS/profile.css')
def serve_profile_css():
    return send_from_directory('static', 'CSS/profile.css')

@app.route('/static/js/script.js')
def serve_js():
    return send_from_directory('static', 'js/script.js')

@app.route('/static/js/login_form.js')
def serve_login_js():
    return send_from_directory('static', 'js/login_form.js')

@app.route('/static/images/<filename>')
def get_image(filename):
    return send_from_directory('static/images', filename)
