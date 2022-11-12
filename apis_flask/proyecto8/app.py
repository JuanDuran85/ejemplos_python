"""_summary_

    Flask basic examples

"""

from flask import Flask, url_for, render_template

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

@app.route('/html')
@app.route('/html/<name>')
def primer_html(name: str = "Juan") -> str:
    return '''
    <html>
        <body>
            <h1>Primer Html</h1>
            <p>Parrafo</p>
            <h3>%s</h3>
        </body>
    </html>
    ''' %name
    
@app.route('/static_file')
def get_static_file():
    return "<img src='./static/img/index.png'>"

@app.route('/static_file_ii')
def get_static_file_ii():
    return f"<img src='{url_for('static',filename='img/index.png')}'>"

@app.route('/index_html')
@app.route('/index_html/<value>')
def index_html(value = None) -> str:
    return render_template('index.html', value=value)

if __name__ == '__main__':
    app.run(debug=True, port=4000)
