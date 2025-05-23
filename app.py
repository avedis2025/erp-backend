from flask import Flask, request, jsonify
from models import db, Customer, Product, Sale
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///erp.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.route("/")
def home():
    return "ERP API is running!"

@app.route("/add_customer", methods=["POST"])
def add_customer():
    data = request.json
    new_customer = Customer(name=data["name"], category=data["category"])
    db.session.add(new_customer)
    db.session.commit()
    return jsonify({"message": "Customer added!"})

@app.route("/add_product", methods=["POST"])
def add_product():
    data = request.json
    new_product = Product(name=data["name"], price=data["price"])
    db.session.add(new_product)
    db.session.commit()
    return jsonify({"message": "Product added!"})

@app.route("/add_sale", methods=["POST"])
def add_sale():
    data = request.json
    new_sale = Sale(customer_id=data["customer_id"], product_id=data["product_id"])
    db.session.add(new_sale)
    db.session.commit()
    return jsonify({"message": "Sale recorded!"})

@app.route("/products", methods=["GET"])
def get_products():
    products = Product.query.all()
    return jsonify([{"id": p.id, "name": p.name, "price": p.price} for p in products])

if __name__ == "__main__":
    app.run()
