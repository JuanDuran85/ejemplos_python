from flask import Blueprint

index = Blueprint('index',__name__)

@index.route('/')
def index_function():
    return "Pagina Index"