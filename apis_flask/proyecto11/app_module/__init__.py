from flask import Flask
from app_module.products.product_view import product

app = Flask(__name__)

app.register_blueprint(product)
