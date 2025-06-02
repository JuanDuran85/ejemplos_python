"""_summary_

    Working with FastAPI
    
    Example: Basic CRUD API

"""

from enum import Enum

from fastapi import FastAPI, Response
from pydantic import BaseModel

app: FastAPI = FastAPI()


class Product(BaseModel):
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """
    name: str
    price: float


class Tags(Enum):
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """
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
    """
    This path operation returns a message saying that the API is working
    """
    
    return {"message": "ok"}


@app.get('/products')
def all_products() -> list:
    """
    This path operation returns a list of all products.

    Returns:
        list: A list of dictionaries, where each dictionary represents a product with its details.
    """

    return products


@app.get("/products/search")
def product_search(name, response: Response) -> list:
    """
    This path operation searches for products by name.

    Args:
        name (str): The name to search for.
        response (Response): The response object to modify the status code.

    Returns:
        list: A list of dictionaries, where each dictionary represents a product that matches the search query.
    """
    found_products = [product for product in products if name.lower() in product['name'].lower()]
    if len(found_products) == 0:
        response.status_code = 404
        return [{"message": "Product not found by Name"}]

    return found_products


@app.get("/products/{id}")
def product_by_id(id: int, response: Response) -> dict:
    """
    This path operation returns a single product by its ID.

    Args:
        id (int): The id of the product to search for.
        response (Response): The response object to modify the status code.

    Returns:
        dict: A dictionary representing the product if found, otherwise a dictionary with a message indicating that the product was not found by id.

    Raises:
        HTTPException: If the product is not found by id.
    """
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
def deleted_product(id_in: int, response: Response) -> list:
    for product in products:
        if product['id'] == id_in:
            products.remove(product)
            response.status_code = 200
            return products

    response.status_code = 404
    return [{"message": PRODUCTS_NOT_FOUND}]


@app.get("/items/", tags=[Tags.items])
async def get_items() -> list:
    return ["Python", "JavaScript"]


@app.get("/users/", tags=[Tags.users])
async def read_users() -> list:
    return ["Jhon", "Doe"]
