from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///ejemplo_flask.db"
db.init_app(app)

from app_module.products.product_view import product
app.register_blueprint(product)

with app.app_context():
    db.create_all()

# you can create your own personal filter here o implementing in blueprint to use
@app.template_filter('reverse_to_do')
def reverse(s):
    print(s)
    return s[::-1]    