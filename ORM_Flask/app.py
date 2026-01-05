from flask import Flask, render_template, request, redirect, url_for
from flask_migrate import Migrate
from database import db 
from models import Alumno
from forms import AlumnoForm

app = Flask(__name__)

#FILTRO PARA JINJA

# @app.add_template_filter
# def cambiar_e_por_3(alumno):
#     return str(alumno).replace('e', '3')

def cambiar_e_por_3(alumno):
    return str(alumno).replace('e', '3')

app.add_template_filter(cambiar_e_por_3, 'cambiar_e_por_3')


#Funciones en plantilla
# @app.add_template_global
# def multiplicar_caracteres(str, veces):
#     return str * veces

def multiplicar_caracteres(str, veces):
    return str * veces

app.add_template_global(multiplicar_caracteres, 'multiplicar_caracteres')

#DATOS PARA CONECTAR A LA BD

USER_DB = 'usuario'
USER_PASSWORD = 'usuario1234'
SERVER_DB = 'localhost'
NAME_DB = 'bd_flask'

FULL_URL_DB = f'postgresql://{USER_DB}:{USER_PASSWORD}@{SERVER_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB

#Crear clave secreta

app.config['SECRET_KEY'] = 'f3a6231a840fe5c8dc8931d9fa5da010cbbf54c9c5460302bd12b7e7e9c0a2ad'

db.init_app(app)

#Migrar modelo a BD
migrate = Migrate()
migrate.init_app(app, db)

@app.route('/')
def inicio():
    #Recogemos todas las filas de alumnos
    alumnos = Alumno.query.order_by('id')
    total_alumnos = Alumno.query.count()
    return render_template('inicio.html', alumnos=alumnos, total_alumnos=total_alumnos)

@app.route('/alumno/<int:id>')
def detalle_alumno(id):
    alumno = Alumno.query.get_or_404(id, 'No se encontro el alumno')
    return render_template('detalle_alumno.html', alumno=alumno)

@app.route('/insertar_alumno', methods=['GET', 'POST'])
def insertar_alumno():
    alumno = Alumno()
    alumno_form = AlumnoForm(obj=alumno)

    if request.method == 'POST':
        if alumno_form.validate_on_submit():
            alumno_form.populate_obj(alumno)
            db.session.add(alumno)
            db.session.commit()
            return redirect(url_for('inicio'))
        else:
            print(alumno_form.errors)
        
    return render_template('insertar_alumno.html', form = alumno_form)


@app.route('/alumno/editar/<int:id>', methods=['GET', 'POST'])
def editar_alumno(id):

    alumno = Alumno.query.get_or_404(id, 'No se encontro el alumno que quieres editar')
    alumno_form = AlumnoForm(obj=alumno)

    if request.method == 'POST':
        if alumno_form.validate_on_submit:
            alumno_form.populate_obj(alumno)
            db.session.commit()
            return redirect(url_for('inicio'))

    return render_template('editar_alumno.html', form=alumno_form)

@app.route('/alumno/eliminar/<int:id>')
def eliminar_alumno(id):
    alumno = Alumno.query.get_or_404(id, 'El alumno que quiere eliminar no se ha encontrado')
    db.session.delete(alumno)
    db.session.commit()
    return redirect(url_for('inicio'))