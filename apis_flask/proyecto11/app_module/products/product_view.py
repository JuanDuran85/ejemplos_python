from flask import Blueprint, render_template
from werkzeug import exceptions
from app_module.products.models.products_model import PRODUCTS

product = Blueprint('product', __name__)

@product.route('/')
@product.route('/home')
def product_function():
    return render_template('products/index.html',products=PRODUCTS)

@product.route('/product/<id>')
def show_product(id: str = ''):
    product_find = PRODUCTS.get(int(id), None)
    if not product_find:
        exceptions.abort(404)
    return render_template('products/show.html',product=product_find)