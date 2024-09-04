from flask import request, jsonify
from models.models_product import Product, db


def controller_add_product():
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


def controller_delete_product(product_id: int):
    product = Product.query.get(product_id)
    if product:
        db.session.delete(product)
        db.session.commit()
        return jsonify({"message": "Product deleted successfully"}), 200
    return jsonify({"message": "product not found"}), 404


def controller_get_products_details(product_id: int):
    product = Product.query.get(product_id)
    if product:
        return jsonify({
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "description": product.description
        })
    return jsonify({"message": "product not found"}), 404


def controller_update_products(product_id: int):
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


def controller_get_products():
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
