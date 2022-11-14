from flask import Blueprint, render_template
from app_module.products.utilities.generals_functions import get_one_product_by_id
from app_module.products.models.products_model import PRODUCTS

product = Blueprint('product', __name__)

@product.route('/')
@product.route('/home')
def product_function():
    return render_template('products/index.html',products=PRODUCTS)

@product.route('/product/<id>')
def show_product(id: str = ''):
    try:
        product_find = get_one_product_by_id(int(id))
        return render_template('products/show.html',product=product_find)
    except Exception as e:
        raise e

@product.route('/filter/<id>')
def filter(id: str = ''):
    try:
        product_find = get_one_product_by_id(int(id))
        return render_template('products/filter.html',product=product_find)
    except Exception as e:
        raise e