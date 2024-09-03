from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Iniciando a aplicação e o banco
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///e-commerce.db'
db = SQLAlchemy(app)
CORS(app)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)


@app.route('/api/products/add', methods=["POST"])
def add_product():
    data = request.get_json()
    if 'name' in data and 'price' in data:
        product = Product(
            name=data["name"],
            price=data["price"],
            description=data.get("description", "")
        )
        db.session.add(product)
        db.session.commit()
        return jsonify({"message": "Product added successfully"}), 200
    return jsonify({"message": "invalid product data"}), 400


@app.route('/api/products/delete/<int:product_id>', methods=["DELETE"])
def delete_product(product_id: int):
    product = Product.query.get(product_id)
    if product:
        db.session.delete(product)
        db.session.commit()
        return jsonify({"message": "Product deleted successfully"}), 200
    return jsonify({"message": "product not found"}), 404


@app.route("/api/products/<int:product_id>", methods=["GET"])
def get_products_details(product_id: int):
    product = Product.query.get(product_id)
    if product:
        return jsonify({
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "description": product.description
        })
    return jsonify({"message": "product not found"}), 404

@app.route('/api/products/update/<int:product_id>', methods=["PUT"])
def update_products(product_id: int):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"message": "Product not found"}), 404
    data = request.get_json()
    if "name" in data:
        product.name = data["name"]
    if "price" in data:
        product.price = data["price"]
    if "description" in data:
        product.description = data['description']

    db.session.commit()

    return jsonify({"message": "product updated successfully"})

@app.route('/api/products', methods=["GET"])
def get_products():
    products = Product.query.all()
    product_list = []
    for product in products:
        product_list.append({
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "description": None if not product.description else product.description
        })
    return jsonify(product_list)


if __name__ == "__main__":
    app.run(debug=True)
