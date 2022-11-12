from flask import Blueprint

meet = Blueprint('meet',__name__)

@meet.route('/meet')
def meet_function():
    return "Pagina ruta de meet"