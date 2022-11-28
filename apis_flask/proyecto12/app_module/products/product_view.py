from flask import Blueprint, render_template
from app_module.products.utilities.generals_functions import get_one_product_by_id
from app_module.products.models.products_model import PRODUCTS
from app_module.products.models.product import Product

product = Blueprint('product', __name__)

@product.route('/')
@product.route('/home')
def product_function() -> str:
    return render_template('products/index.html',products=PRODUCTS)

@product.route('/product/<id>')
def show_product(id: str = '') -> str:
    try:
        product_find: dict[int,dict] = get_one_product_by_id(int(id))
        return render_template('products/show.html',product=product_find)
    except Exception as e:
        print(e)
        raise e

@product.route('/filter/<id>')
def filter(id: str = '') -> str:
    try:
        product_find = get_one_product_by_id(int(id))
        return render_template('products/filter.html',product=product_find)
    except Exception as e:
        print(e)
        raise e
    
# you can use blueprint to create your own filters to.
@product.app_template_filter('iva')
def iva_filter(price_in: float = 0)-> float:
    return (price_in * .20) + price_in if price_in else 0.0