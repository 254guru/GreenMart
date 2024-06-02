from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from flask_login import login_required
from app import db
from app.models import User, Product, Category, Order, OrderItem
from app.admin import admin_custom_bp


@admin_custom_bp.route('/')
def index():
    """
    This route handles the display of the admin dashboard. It checks if the user is logged in
    and has the 'admin' role. If the user is not logged in or does not have the 'admin' role,
    they are redirected to the login page with an error message.
    """
    if 'user_id' not in session or session.get('role') != 'admin':
        flash('You do not have permission to access the admin dashboard.', 'danger')
        return redirect(url_for('user_bp.login'))
    return render_template('admin_dashboard.html')


@admin_custom_bp.route('/users')
def users():
    """
    This route handles the display of all users in the system. It retrieves all users from the
    database and renders them in the 'admin_users.html' template.
    """
    if 'user_id' not in session:
        flash('Please login to access users page')
        return redirect(url_for('user_bp.login'))
    users = User.query.all()
    return render_template('admin_users.html', users=users)


@admin_custom_bp.route('/products')
def products():
    """
    This route handles the display of all products in the system. It retrieves all products from the
    database and renders them in the 'admin_product.html' template.
    """
    products = Product.query.all()
    categories = Category.query.all()
    return render_template('admin_product.html', products=products)


@admin_custom_bp.route('/orders')
def orders():
    """
    This route handles the display of all orders in the system. It retrieves all orders from the
    database and renders them in the 'admin_orders.html' template.
    """
    orders = Order.query.all()
    return render_template('admin_orders.html', orders=orders)


@admin_custom_bp.route('/item')
def order_items():
    """
    This route handles the display of all order items in the system. It retrieves all order items from the
    database and renders them in the 'order_item.html' template.
    """
    items = OrderItem.query.all()
    return render_template('admin_orderitem.html', order_items=items)


@admin_custom_bp.route('/categories')
@login_required
def categories():
    """
    This route handles the display of all categories in the system. It retrieves all categories from the
    database and renders them in the 'admin_categories.html' template.
    """
    categories = Category.query.all()
    return render_template('admin_categories.html', categories=categories)


@admin_custom_bp.route('/products/add', methods=['GET', 'POST'])
def add_product():
    """
    This route handles the addition of a new product to the system. It processes a POST request
    to create a new product with the provided details. 
    """
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        category_id = request.form['category_id']
        image_url = request.form['image_url']
        new_product = Product(name=name, description=description, price=price, category_id=category_id, image_url=image_url)
        db.session.add(new_product)
        db.session.commit()
        flash('Product added successfully!', 'success')
        return redirect(url_for('admin_custom.products'))
    categories = Category.query.all()
    return render_template('admin_product.html', categories=categories)


@admin_custom_bp.route('/products/edit/<int:product_id>', methods=['GET', 'POST'])
def edit_product(product_id):
    """
    This route handles the editing of an existing product in the system. It processes a POST request
    to update the product details with the provided information.
    """
    product = Product.query.get_or_404(product_id)
    if request.method == 'POST':
        product.name = request.form['name']
        product.description = request.form['description']
        product.price = request.form['price']
        product.category_id = request.form['category_id']
        product.image_url = request.form['image_url']
        db.session.commit()
        flash('Product updated successfully!', 'success')
        return redirect(url_for('admin_custom.products'))
    categories = Category.query.all()
    return render_template('admin_product.html', product=product, categories=categories)


@admin_custom_bp.route('/products/delete/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """
    This route handles the deletion of a product from the system. It processes a DELETE request
    to remove the product with the specified ID from the database.
    """
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    flash('Product deleted successfully!', 'success')
    return redirect(url_for('admin_custom.products'))

