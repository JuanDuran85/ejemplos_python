from flask import Flask, request

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

@app.route('/mensaje')
def mensaje():
    return f'Mensaje desde la ruta: {request.path}'

@app.route('/persona/<nombre>')
def persona(nombre):
    return f'Hola {nombre.upper()}. Bienvenido'

@app.route('/edad/<int:edad>')
def edad_usuario(edad):
    return f'Tu edad es: {edad}.'