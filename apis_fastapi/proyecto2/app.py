"""_summary_

    Working with FastAPI
    
    Example: Basic CRUD API

"""

from fastapi import FastAPI, Response
from pydantic import BaseModel
from enum import Enum

app: FastAPI = FastAPI()

class Product(BaseModel):
    name: str
    price: float
    
class Tags(Enum):
    items = "items"
    users = "users"

products: list = [
    {"id": 1, "name": "Foo", "price": 100},
    {"id": 2, "name": "Bar", "price": 200},
    {"id": 3, "name": "Baz", "price": 300},
    {"id": 4, "name": "Buz", "price": 400},
]

PRODUCTS_NOT_FOUND: str = "Product not found"

@app.get("/")
def index() -> dict:
    return {"message": "ok"}

@app.get('/products')
def all_products() -> list:
    return products

@app.get("/products/search")
def product_search(name, response: Response) -> list:
    found_products = [product for product in products if name.lower() in product['name'].lower()]
    if len(found_products) == 0:
        response.status_code = 404
        return [{"message": "Product not found by Name"}]

    return found_products

@app.get("/products/{id}")
def product_by_id(id: int, response: Response) -> dict:
    for product in products:
        if product['id'] == id:
            return product
    response.status_code = 404
    return {"message": "Product not found by id"}

@app.post('/products')
def add_product(new_product: Product, response: Response) -> list:
    product_enter = new_product.dict()
    product_enter['id'] = len(products) + 1
    products.append(product_enter)
    response.status_code = 201
    return products

@app.put('/products/{id}')
def put_product(id: int, edited_product: Product, response: Response) -> list:
    for product in products:
        if product['id'] == id:
            product['name'] = edited_product.name
            product['price'] = edited_product.price
            response.status_code = 200
            return product

    response.status_code = 404
    return [{"message": PRODUCTS_NOT_FOUND}]

@app.delete('/products/{id}')
def deleted_product(id: int, response: Response) -> list:
    for product in products:
        if product['id'] == id:
            products.remove(product)
            response.status_code = 200
            return products

    response.status_code = 404
    return [{"message": PRODUCTS_NOT_FOUND}]

@app.get("/items/",tags=[Tags.items])
async def get_items() -> list:
    return ["Python","JavaScript"]

@app.get("/users/",tags=[Tags.users])
async def read_users() -> list:
    return ["Jhon","Doe"]