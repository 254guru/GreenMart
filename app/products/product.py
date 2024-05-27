from flask import Flask, request, jsonify, render_template
from app.models import Product
from app import app, db
from app.products import bp

@bp.route('/shop')
def shop_products():
    products = Product.query.all()
    return render_template('shop.html', products=products)


@bp.route('/create_new', methods=['GET'])
def create_new():
    try:
        # Create instances of Product
        product = Product(name='potato', description='vegies', price=10.0, image_url='images/botato.jpg', category_id=8)
        #product = Product(name='banana', description='yellow fruit', price=1.0, image_url='images/banana.jpg', category_id=3)
        

        # Add instances to the session
        db.session.add(product)
       # db.session.add(product2)

        # Commit the session to persist changes to the database
        db.session.commit()

        return f'{product.name} added successfully!'
    except Exception as e:
         # Log the error for debugging
        print(f'Error adding new products: {str(e)}')
        return 'Error adding new products'
    

    # Route for deleting a product
@bp.route('/delete_product/<int:product_id>', methods=['GET'])
def delete_product(product_id):
    try:
        # Query the product to be deleted
        product = Product.query.get_or_404(product_id)

        # Delete the product from the database
        db.session.delete(product)
        db.session.commit()

        # Return a success message
        return jsonify({'message': f'{product.name} deleted successfully'}), 200
    except Exception as e:
        # Handle exceptions
        return jsonify({'error': str(e)}), 500



@bp.route('/update_product', methods=['GET'])
def update_product():
    product_id = request.args.get('id')
    new_price = request.args.get('price')

    if product_id is None or new_price is None:
        return jsonify({"error": "Product ID and price are required"}), 400

    try:
        product = Product.query.filter_by(id=product_id).first()
        if product:
            product.price = float(new_price)
            db.session.commit()
            return jsonify({"message": "Product updated successfully"}), 200
        else:
            return jsonify({"error": "Product not found"}), 404
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
