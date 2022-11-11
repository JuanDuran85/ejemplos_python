"""_summary_

    Flask basic examples

"""

from flask import Flask

app: Flask = Flask(__name__)

@app.route('/')
def index() -> str:
    return 'New flask example ccvc'

@app.route('/hello')
def hello_func() -> str:
    return 'Hello from Flask'

@app.route('/test')
@app.route('/test/<input_one>')
@app.route('/test/<input_one>/<lang>')
def test(input_one: str = "hola...",lang: str = "En") -> str:
    return f'Mensaje: {input_one} + {lang}...'

if __name__ == '__main__':
    app.run(debug=True, port=4000)
