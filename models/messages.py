from utils.db import db


class messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=True)
    apellido = db.Column(db.String(50), nullable=True)
    correo = db.Column(db.String(50), nullable=True)
    mensaje = db.Column(db.String(50), nullable=True)

    def __init__(self, id, nombre, apellido, correo, mensaje) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.mensaje = mensaje

    def __repr__(self) -> str:
        return f"Order({self.id}, '{self.nombre}', '{self.apellido}', '{self.correo}', '{self.mensaje}')"