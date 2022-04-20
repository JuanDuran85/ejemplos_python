"""_summary_

    Usando flask con template

"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home()-> str:
    nombre: str = "Juan"
    return render_template("portada.html",valor=nombre)

@app.route("/valores")
def valores() -> str:
    datos_totales: dict = {
        "nombre":"Juan",
        "lugar":"Lima",
        "edad":22
    }
    return render_template("portada.html",valores=datos_totales)

@app.route("/colores")
def colores()-> str:
    colores: list = ["red", "green", "blue", "yellow", "purple"]
    return render_template("color.html",len=len(colores),colores=colores)

@app.route("/frase/<texto>")
def frase(texto: str) -> str:
    return render_template("frases.html",frase=texto)

if __name__ == "__main__":
    app.run(debug=True, port=4000)