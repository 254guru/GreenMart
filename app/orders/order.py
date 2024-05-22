from flask import request, jsonify, render_template, redirect, flash, session, url_for
from app.models import Order, Product, db
from app.orders import bp
from flask_login import login_required


@bp.route('/create_order', methods=['POST'])
@login_required
def create_order():
    user_id = request.form.get('user_id')
    total_price = request.form.get('total_price')
    
    
    if user_id and total_price:
        new_order = Order(
            user_id=user_id,
            total_price=total_price,
            #status=status,
            payment_status=payment_status

        )
        db.session.add(new_order)
        db.session.commit()
        return jsonify({'message': 'Order created successfully!'}), 201
        return render_template('shop.html')
    else:
        return jsonify({'message': 'Incomplete data provided!'}), 400




@bp.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    quantity = request.args.get('quantity', default=1, type=int)
    if 'cart' not in session:
        session['cart'] = {}
        
    if product_id in session['cart']:
       session['cart'][product_id] += quantity
    else:
       session['cart'][product_id]= quantity
    print(session)
    #flash('Product added to cart')
    view_cart = fetch_cart()
    print(view_cart)
    
    return redirect(url_for('products.shop_products'))

def fetch_cart():
    cart = session.get('cart', {})
    cart_items = []
    for product_id, quantity in cart.items():
        product = Product.query.get(product_id)
        cart_items.append({
            'product_id': product_id,
            'product_name': product.name,
            'price': product.price,
            'quantity': quantity,
            'image_url': product.image_url,
            'total_price': product.price * quantity
        })
    return cart_items


#

def calculate_total_price():
    cart_items = fetch_cart()
    total_price = 0
    for item in cart_items:
        total_price += item['total_price']
    return total_price