from flask import Flask, jsonify, request

app = Flask(__name__)

from products import products

@app.route('/ping')
def ping():
    return jsonify({'status': 'ok'})

@app.route('/')
def new_page():
    return "Welcome to the new page"

@app.route('/products')
def get_products():
    return jsonify({
        "products": products, 
        "status": 'ok', 
        "message":"Product list"
    })
    
@app.route('/products/<string:product_name>')
def get_product(product_name):
    product_found = [product for product in products if product_name == product['name']]
    print(product_found)
    if (len(product_found) > 0):
        return jsonify({'Info Product': product_found})
    else:
        return jsonify({'Info Product': "Not Foud"})
    
@app.route('/products',methods=['POST'])
def create_new_product():
    print(request.json)
    return "Ok"
    
if __name__ == '__main__':
    app.run(debug = True, port = 4000)