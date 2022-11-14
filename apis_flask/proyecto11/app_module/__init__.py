from flask import Flask
from app_module.products.product_view import product

app = Flask(__name__)

app.register_blueprint(product)

# you can create your own personal filter here o implementing in blueprint to use
@app.template_filter()
def reverse(s):
    pass    