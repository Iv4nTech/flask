from datetime import date
from app import db
from sqlalchemy.orm import Mapped, mapped_column

class Alumno(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] 
    apellidos: Mapped[str] 
    fecha_nac: Mapped[date]

    def __str__(self):
        return f'ID: {self.id} Nombre: {self.nombre}'
    