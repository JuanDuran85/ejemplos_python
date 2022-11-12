from my_app import app


# views
@app.route('/')
def index() -> str:
    return "Primera ruta con Flask - index"