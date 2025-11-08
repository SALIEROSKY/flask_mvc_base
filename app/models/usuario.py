from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'  # opcional, pero recomendable

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    activo = db.Column(db.Boolean, default=True)
    rol_id = db.Column(db.Integer, db.ForeignKey('roles.id'))  # ← corregido aquí
    rol = db.relationship('Rol', back_populates='usuarios', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
