import os

from flask import Flask
from flask_cors import CORS
from models.models_product import db
from dotenv import load_dotenv

from controllers import controller_product

load_dotenv(override=True)
string_conn = os.getenv("POSTGRES_STRING_CONN")


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = string_conn
CORS(app)
db.init_app(app)


@app.route('/api/products/add', methods=["POST"])
def add_product():
    return controller_product.controller_add_product()


@app.route('/api/products/delete/<int:product_id>', methods=["DELETE"])
def delete_product(product_id: int):
    return controller_product.controller_delete_product(product_id)


@app.route("/api/products/<int:product_id>", methods=["GET"])
def get_products_details(product_id: int):
    return controller_product.controller_get_products_details(product_id)


@app.route('/api/products/update/<int:product_id>', methods=["PUT"])
def update_products(product_id: int):
    return controller_product.controller_update_products(product_id)


@app.route('/api/products', methods=["GET"])
def get_products():
    return controller_product.controller_get_products()


if __name__ == "__main__":
    app.run(debug=True)
