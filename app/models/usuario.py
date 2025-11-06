from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)  # 👈 campo real
    activo = db.Column(db.Boolean, default=True)

    # --- Métodos de contraseña ---
    def set_password(self, password):
        """Genera y guarda el hash de una contraseña"""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Verifica si una contraseña coincide con el hash"""
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<Usuario {self.nombre}>"
