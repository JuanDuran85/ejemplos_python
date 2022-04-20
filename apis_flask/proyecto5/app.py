"""_summary_

    Ejemplo utilizando flask

"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def main() -> str:
    return "<h1>Mensaje desde Flask</h1>"

@app.route("/ejemplo")
def ejemplo() -> str:
    return "<h2>Ejemplo de mensaje en al ruta Ejemplo</h2>"

@app.route("/dinamica/<nombre>")
def dinamica(nombre: str) -> str:
    return f"<h2>El nombre es: {nombre} y la letra en la posicion 5 es {nombre[5]}</h2>"

@app.route("/longitud/<nombre>")
def longitud(nombre: str) -> str:
    return f"<h3>La longitud del nombre {nombre} es: {len(nombre)}</h3>"

@app.route("/edad/<nombre>/<edad>")
def edad(nombre: str, edad: str) -> str:
    return f"{nombre} tiene {edad} años"

@app.route("/sumar/<n1>/<n2>")
def sumar(n1: str, n2: str) -> str:
    return f"La suma de {n1} y {n2} es: {int(n1) + int(n2)}"

if __name__ == "__main__":
    app.run(debug=True, port=4000)