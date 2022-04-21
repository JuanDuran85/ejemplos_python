"""_summary_

    Using Flask with templates

"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index() -> str:
    """Return homepage."""
    return render_template("index.html")

@app.route("/pagina1")
def pagina_uno() -> str:
    """Return pagina1."""
    return render_template("pagina1.html")

@app.route("/pagina2")
def pagina_dos() -> str:
    """Return pagina2."""
    return render_template("pagina2.html")

if __name__ == "__main__":
    app.run(debug=True, port=4000)