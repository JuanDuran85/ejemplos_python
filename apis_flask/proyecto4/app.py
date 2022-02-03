import os
from dotenv import load_dotenv
from database import db

from flask import Flask, render_template, jsonify
from flask_migrate import Migrate

from models import Persona
from froms import PersonaForm

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

# configuracion de flasl-wtf
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# inicializamosel objeto de base de datos de sqlAlchemy
# db = SQLAlchemy(app)
db.init_app(app)

# configurando las migraciones y mapeo para la base de datos

migrate = Migrate()
migrate.init_app(app, db)

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def health():
    return jsonify({'status': 'OK'})

@app.route('/api/v1')
def inicio():
    # listado de personas
    personas = Persona.query.all()
    total_personas = Persona.query.count()
    app.logger.debug(f"Personas: {personas}")
    app.logger.debug(f"Total personas: {total_personas}")
    return render_template('index.html', personas = personas, total_personas = total_personas)

@app.route('/api/v1/personas')
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

@app.route('/api/v1/personas/<int:id>')
def ver_personas(id):
    # recuperamos la persona segun el id proporcionado
    # persona = Persona.query.get(id)
    persona = Persona.query.get_or_404(id)
    print(f"{persona = }")
    app.logger.debug(f"{persona = }")
    return render_template('detalle.html', persona = persona)

@app.route('/api/v1/agregar', methods=['GET', 'POST'])
def agregar():
    # utilizando wtforms para los formularios
    persona = Persona()
    persona_form = PersonaForm(obj=persona)
    return render_template('agregar.html', forma = persona_form)
    