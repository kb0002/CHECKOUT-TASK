from flask import Flask, request, jsonify
from models import db, Product, seed_database

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Initialize database and seed data
with app.app_context():
    db.create_all()
    seed_database()

@app.route('/checkout', methods=['POST'])
def checkout():
    data = request.get_json()
    
    if not data or 'items' not in data:
        return jsonify({"error": "Invalid input"}), 400

    cart = {}

    # Count each item occurrence
    for item in data['items']:
        cart[item] = cart.get(item, 0) + 1

    total_price = 0

    for item, quantity in cart.items():
        product = Product.query.filter_by(name=item).first()
        if not product:
            return jsonify({"error": f"Invalid product: {item}"}), 400

        # Apply bulk pricing if applicable
        if product.bulk_quantity and quantity >= product.bulk_quantity:
            bulk_sets = quantity // product.bulk_quantity
            remaining_units = quantity % product.bulk_quantity
            total_price += (bulk_sets * product.bulk_price) + (remaining_units * product.unit_price)
        else:
            total_price += quantity * product.unit_price

    return jsonify({"total_price": total_price})

if __name__ == '__main__':
    app.run(debug=True)
