from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from flask_login import login_required
from app import db
from app.models import User, Product, Category, Order, OrderItem
from app.admin import admin_custom_bp

@admin_custom_bp.route('/')
#@login_required()

def index():
    if 'user_id' not in session:
        flash('Please login to access the admin dashboard')
        return redirect(url_for('user_bp.login'))


    return render_template('admin_dashboard.html')

@admin_custom_bp.route('/users')
#@login_required
def users():
    if 'user_id' not in session:
        flash('Please login to access users page')
        return redirect(url_for('user_bp.login'))

    users = User.query.all()
    return render_template('admin_users.html', users=users)

@admin_custom_bp.route('/products')
#@login_required
def products():
    products = Product.query.all()
    categories = Category.query.all()

    return render_template('admin_product.html', products=products)

@admin_custom_bp.route('/orders')
#@login_required
def orders():
    orders = Order.query.all()
    return render_template('admin_orders.html', orders=orders)

@admin_custom_bp.route('/categories')
@login_required
def categories():
    categories = Category.query.all()
    return render_template('admin_categories.html', categories=categories)

# Add, edit, delete routes for users, products, orders, categories
# Example for adding a product
@admin_custom_bp.route('/products/add', methods=['GET', 'POST'])
#@login_required
def add_product():
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
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    flash('Product deleted successfully!', 'success')
    return redirect(url_for('admin_custom.products'))

@admin_custom_bp.route('/item')
#@login_required
def order_items():
    item = OrderItem.query.all()
    return render_template('order_item.html', item=item)