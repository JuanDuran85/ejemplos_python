from my_app import app


# views
@app.route('/second')
def second() -> str:
    return "segunda ruta con Flask"