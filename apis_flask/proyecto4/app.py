from flask import Flask, request, render_template, url_for, redirect, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# configurar la integracion con la base de datos
USER_DB = os.getenv('USER_DB')
PASSWORD_DB = os.getenv('PASSWORD_DB')
URL_DB = os.getenv('URL_DB')
NAME_DB = os.getenv('NAME_DB')
FULL_URL_DB = f'postgresql://{USER_DB}:{PASSWORD_DB}@{URL_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# inicializamosel objeto de base de datos de sqlAlchemy
db = SQLAlchemy(app)

# configurando las migraciones y mapeo para la base de datos

migrate = Migrate()
migrate.init_app(app, db)

# clase de modelo
class Persona(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(20), nullable = False)
    apellido = db.Column(db.String(20), nullable = False)
    email = db.Column(db.String(50), unique = True, nullable = False)

    def __str__(self):
        return (
            f'Id: {self.id}, '
            f'Nombre: {self.nombre}, ' 
            f'Apellido: {self.apellido}, ' 
            f'Email: {self.email}'
        )

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def health():
    return jsonify({'status': 'OK'})

@app.route('/api/vi/#')
def inicio():
    # listado de personas
    personas = Persona.query.all()
    total_personas = Persona.query.count()
    app.logger.debug(f"Personas: {personas}")
    app.logger.debug(f"Total personas: {total_personas}")
    return render_template('index.html', personas = personas, total_personas = total_personas)

@app.route('/api/vi/personas/')
def personas_json():
    # listado de personas
    personas = Persona.query.all()
    data_persona = []
    for persona in personas:
        data_persona.append({
            "id":persona.id,
            "nombre":persona.nombre,
            "apellido":persona.apellido,
            "email":persona.email
        })
    total_personas = Persona.query.count()
    mostrar_personas = {
        "total_personas": total_personas,
        "personas": data_persona
    }
    app.logger.debug(f"Personas: {mostrar_personas}")
    return jsonify(mostrar_personas)