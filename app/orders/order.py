from flask import request, jsonify, render_template, redirect, flash, session, url_for
from app.models import Order, Product, db , OrderItem
from app.orders import bp
from flask_login import login_required


@bp.route('/checkout', methods=['POST'])
def create_order():
    if 'user_id' not in session:
        flash('Login to continue')
        return redirect(url_for('user.login'))

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
        orderid = new_order.id
        ordered_items = []
        for product_id, value in session['cart'].items():
            order_item = OrderItem(
                order_id=orderid,
                product_id=product_id,
                quantity=value['quantity']
            )
            db.session.add(order_item)
            db.session.commit()
            ordered_items.append(order_item)
            
        #return jsonify({'message': 'Order created successfully!'}), 201
        return render_template('summary.html', order=new_order, order_items=ordered_items)
    else:
        return jsonify({'message': 'login first!'}), 400

@bp.route('/order_summary/<int:order_id>')
#@login_required
def order_summary(order_id):
    order = Order.query.get_or_404(order_id)
    order_items = OrderItem.query.filter_by(order_id=order_id).all()
    return render_template('summary.html', order=order, order_items=order_items)
    return redirect(url_for('index'))
    


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
    
        
    #print(session)
    quantity = 1 #request.args.get('quantity', default=1)
    dict_items = {product_id: {'quantity': quantity}}
    if 'cart' in session:
        if product_id in session['cart']:
            dict_items[product_id]['quantity'] += session['cart'][product_id]['quantity']
            session['cart'] = merge(session['cart'], dict_items)
        else:
            #print('before', session['cart'])
            session['cart'] = merge(session['cart'], dict_items)

            #print('after', session['cart'])
            return redirect(url_for('products.shop_products'))
           
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
        print(session['cart'])
        
        if product_id in session['cart']:
            print(session['cart']['product_id'])
            print(product_id)
            del session['cart'][product_id]
        else:
            print('Product not in cart')
        return redirect(url_for('index'))
    else:
        print('Cart is empty')
        return redirect(url_for('index'))



