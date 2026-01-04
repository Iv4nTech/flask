from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column
from flask_migrate import Migrate
from datetime import date 

app = Flask(__name__)

#DATOS PARA CONECTAR A LA BD

USER_DB = 'usuario'
USER_PASSWORD = 'usuario1234'
SERVER_DB = 'localhost'
NAME_DB = 'bd_flask'

FULL_URL_DB = f'postgresql://{USER_DB}:{USER_PASSWORD}@{SERVER_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB

db = SQLAlchemy(app)


#Migrar modelo a BD
migrate = Migrate()
migrate.init_app(app, db)

#Modelo de datos

class Alumno(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] 
    apellidos: Mapped[str] 
    fecha_nac: Mapped[date]

    def __str__(self):
        return f'ID: {self.id} Nombre: {self.nombre}'
    

@app.route('/')
def inicio():
    #Recogemos todas las filas de alumnos
    alumnos = Alumno.query.all()
    total_alumnos = Alumno.query.count()
    return render_template('inicio.html', alumnos=alumnos, total_alumnos=total_alumnos)