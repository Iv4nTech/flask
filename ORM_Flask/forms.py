from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField #Para los difentes inputs
from wtforms.validators import DataRequired #Validar campos requiriendo que tenga datos el input (Aunque esto ya se hace desde el cliente HTML)

class AlumnoForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    apellidos = StringField('Apellidos', validators=[DataRequired()])
    fecha_nac = DateField('Fecha de nacimiento', validators=[DataRequired()])
    guardar = SubmitField('Guardar')