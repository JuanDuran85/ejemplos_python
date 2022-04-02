"""_summary_

    Working with FastAPI
    
    Example: Basic CRUD API

"""

from fastapi import FastAPI
import uvicorn

app: FastAPI = FastAPI()

products: list = [
    {"id": 1, "name": "Foo", "price": 100},
    {"id": 2, "name": "Bar", "price": 200},
    {"id": 3, "name": "Baz", "price": 300},
    {"id": 4, "name": "Buz", "price": 400},
]

@app.get("/")
def index() -> dict:
    return {"message": "ok"}

@app.get('/products')
def all_products() -> list:
    return products

@app.get("/products/{id}")
def product_by_id(id: int) -> dict:
    for product in products:
        if product['id'] == id:
            return product
    return {"message": "Product not found"}