from flask import request, jsonify, render_template, redirect, flash, session, url_for
from app.models import Order, Product, db
from app.orders import bp
from flask_login import login_required


@bp.route('/checkout', methods=['POST'])
def create_order():
    user_id =  session.get('user_id')
    total_price = request.form.get('total_price')
    
    
    if user_id and total_price:
        payment_status = 'paid'
        new_order = Order(
            user_id=user_id,
            total_price=total_price,
            #status=status,
            payment_status=payment_status

        )
        db.session.add(new_order)
        db.session.commit()
        return jsonify({'message': 'Order created successfully!'}), 201
       # return render_template('summary.html')
    else:
        return jsonify({'message': 'Incomplete data provided!'}), 400


def merge(dict1, dict2):
    if isinstance(dict1, list) and isinstance(dict2, list):
        return dict1 + dict2
    elif isinstance(dict1, dict) and isinstance(dict2, dict):
        return dict(list(dict1.items()) + list(dict2.items()))

@bp.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    if request.method == 'POST':
        product_id = request.form.get('product_id')
        #print(product_id)
        
    print(session)
    quantity = 1 #request.args.get('quantity', default=1)
    dict_items = {product_id: {'quantity': quantity}}
    if 'cart' in session:
        if product_id in session['cart']:
            session['cart'][product_id] += quantity
        else:
            #print('before', session['cart'])
            session['cart'] = merge(session['cart'], dict_items)
            #print('after', session['cart'])
            return redirect(url_for('index'))
           
    else:
       session['cart'] = dict_items
    #print(session['cart'])
    #flash('Product added to cart')
   # view_cart = fetch_cart()
    
    #  'cart': {'11': {'quantity': 1}, '12': {'quantity': 1}, '13': {'quantity': 1}, '16': {'quantity': 1}, '18': {'quantity': 1}}}>
    return redirect(url_for('products.shop_products'))

def fetch_cart():
    cart = session.get('cart', {})
    cart_items = []
    for product_id, value in cart.items():
        #print(key, value)
        #print(value['quantity'])
        product = Product.query.get(product_id)

        if product:
            cart_items.append({
            'product_id': product_id,
            'product_name': product.name,
            'price': product.price,
            'quantity': value['quantity'],
            'image_url': product.image_url,
            'total_price': product.price * value['quantity']
        })
    return cart_items


#

def calculate_total_price():
    cart_items = fetch_cart()
    total_price = 0
    for item in cart_items:
        total_price += item['total_price']
    return total_price


@bp.route('/remove_from_cart/<int:product_id>')
def remove_from_cart(product_id):
    if 'cart' in session:
        #print(product_id)
        
        if product_id in session['cart']:
            print(session['cart']['product_id'])
            print(product_id)

        
            session['cart'].pop(product_id)
        return redirect(url_for('index'))
    else:
        print('Cart is empty')
        return redirect(url_for('index'))

