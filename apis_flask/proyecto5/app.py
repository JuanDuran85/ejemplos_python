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

if __name__ == "__main__":
    app.run(debug=True, port=4000)