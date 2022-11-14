"""_summary_

    General functions

"""
from werkzeug import exceptions
from app_module.products.models.products_model import PRODUCTS

def get_one_product_by_id(id: int = 0):
    product_find = PRODUCTS.get(id, None)
    return product_find or exceptions.abort(404)