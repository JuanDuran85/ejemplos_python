from flask import Flask, jsonify, request

app = Flask(__name__)

from products import products


@app.route("/ping")
def ping():
    return jsonify({"status": "ok"})


@app.route("/")
def new_page():
    return "Welcome to the new page"


@app.route("/products")
def get_products():
    return jsonify({"products": products, "status": "ok", "message": "Product list"})


@app.route("/products/<string:product_name>")
def get_product(product_name):
    product_found = [product for product in products if product_name == product["name"]]
    print(product_found)
    if len(product_found) > 0:
        return jsonify({"Info Products": product_found})
    else:
        return jsonify({"Info Product": "Not Foud"})


@app.route("/products", methods=["POST"])
def create_new_product():
    new_product = {
        "name": request.json["name"],
        "price": request.json["price"],
        "quantity": request.json["quantity"],
    }
    products.append(new_product)
    print(request.json)
    return jsonify({"Info new Products": products, "message": "Product created"})


@app.route("/products/<string:product_name>", methods=["PUT"])
def editproduct(product_name):
    producto_found = [
        product for product in products if product["name"] == product_name
    ]
    if (len(producto_found) > 0):
        producto_found[0]["name"] = request.json["name"]
        producto_found[0]["price"] = request.json["price"]
        producto_found[0]["quantity"] = request.json["quantity"]
        return jsonify({"Info Product Updated": producto_found[0], "message": "Producto edit"})
    else:
        return jsonify({"Info Product for edit": "Not Foud"})
    
@app.route("/products/<string:product_name>", methods=["DELETE"])
def delete_product(product_name):
    product_found = [product for product in products if product["name"] == product_name]
    if (len(product_found) > 0):
        products.remove(product_found[0])
        return jsonify({"Info Product": product_found[0], "message": "Product deleted"})
    else:
        return jsonify({"Info Product for deleted": "Not Foud"})    

if __name__ == "__main__":
    app.run(debug=True, port=4000)
