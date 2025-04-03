from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), unique=True, nullable=False)
    unit_price = db.Column(db.Integer, nullable=False)
    bulk_quantity = db.Column(db.Integer, nullable=True)  # Quantity required for discount
    bulk_price = db.Column(db.Integer, nullable=True)  # Price for bulk items

# Function to insert default product data
def seed_database():
    if not Product.query.first():  # Only insert if table is empty
        products = [
            Product(name='A', unit_price=50, bulk_quantity=3, bulk_price=130),
            Product(name='B', unit_price=30, bulk_quantity=2, bulk_price=45),
            Product(name='C', unit_price=20),
            Product(name='D', unit_price=15)
        ]
        db.session.bulk_save_objects(products)
        db.session.commit()
        print("Database seeded successfully!")
