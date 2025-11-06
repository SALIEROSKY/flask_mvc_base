from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    activo = db.Column(db.Boolean, default=True)

    # --- Relación con roles ---
    rol_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)
    rol = db.relationship('Rol', back_populates='usuarios')

    # --- Métodos de contraseña ---
    def set_password(self, password):
        """Genera y guarda el hash de una contraseña segura."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Verifica si una contraseña coincide con el hash almacenado."""
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        rol_nombre = self.rol.nombre if self.rol else 'Sin rol'
        return f"<Usuario {self.nombre} ({rol_nombre})>"
