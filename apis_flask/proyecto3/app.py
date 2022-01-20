from flask import Flask, request, render_template, url_for, redirect, flash, jsonify

app = Flask(__name__)

@app.route('/')
def health():
    print("Health check - logged checks")
    app.logger.info(f'Entramos al path {request.path}')
    app.logger.info('Health check')
    app.logger.error('Health check error')
    app.logger.warning('Health check warning')
    app.logger.debug('Health check debug')
    return 'OK'

@app.route('/mostrar/<nombre>', methods=['GET', 'POST'])
def mostrar_nombre(nombre):
    return render_template('index.html', nombre_a_mostrar=nombre)

@app.route('/edad/<int:edad>')
def edad_usuario(edad):
    return f'Tu edad es: {edad}.'

# para redireccionar de forma directa
@app.route('/redireccionar')
def redireccionar():
    return redirect(url_for('health'))

@app.route('/redireccionar_nombre')
def redireccion_nombre():
    return redirect(url_for('mostrar_nombre', nombre='Juan'))
