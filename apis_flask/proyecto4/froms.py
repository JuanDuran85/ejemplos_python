# clase para formulario
from flask_wtf import FlaskForm
import wtforms
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class PersonaForm(FlaskForm):
    nombre = StringField('Nombre', wtforms.validators[DataRequired()])
    apellido = StringField('Apellido', wtforms.validators[DataRequired()])
    email = StringField('Email', wtforms.validators[DataRequired()])
    enviar = SubmitField('Enviar', wtforms.validators[DataRequired()])