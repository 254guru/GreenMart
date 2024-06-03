from flask import Flask, request, jsonify, render_template
from app.models import Product
from app import app
from app.products import bp

@bp.route('/shop')
def shop_products():
    """
    This route handles the display of all products available in the shop.
    It retrieves all products from the database and renders them in the
    'shop.html' template.

    Returns:
        str: The rendered HTML template for the shop page with the list of products.
    """
    products = Product.query.all()
    return render_template('shop.html', products=products)

    






