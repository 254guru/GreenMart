from app import app
from flask import session
from app.models import Product


@app.context_processor
def inject_cart():
    """
    Injects the cart items and total price into the context for all templates.
    """
    cart = session.get('cart', {})
    cart_items = []
    total_price = 0

    for product_id, value in cart.items():
        product = Product.query.get(product_id)
        if product:
            item_total_price = product.price * value['quantity']
            total_price += item_total_price
            cart_items.append({
                'product_id': product_id,
                'product_name': product.name,
                'price': product.price,
                'quantity': value['quantity'],
                'image_url': product.image_url,
                'total_price': item_total_price
            })

    return {
        'cart_items': cart_items,
        'total_price': total_price
    }