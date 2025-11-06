from app import db
from app.models.usuario import Usuario
from werkzeug.security import generate_password_hash

def obtener_usuarios():
    """Devuelve todos los usuarios, activos e inactivos."""
    return Usuario.query.order_by(Usuario.id.asc()).all()

def obtener_usuario_por_id(usuario_id):
    """Devuelve un usuario específico por su ID."""
    return Usuario.query.filter_by(id=usuario_id).first()

def crear_usuario(nombre, correo, password="123456"):
    """Crea un nuevo usuario con una contraseña por defecto o personalizada."""
    nuevo = Usuario(
        nombre=nombre,
        correo=correo,
        activo=True,
        password_hash=generate_password_hash(password)
    )
    db.session.add(nuevo)
    db.session.commit()
    return nuevo

def actualizar_usuario(usuario_id, nombre=None, correo=None, activo=None):
    """Actualiza los datos de un usuario existente."""
    usuario = Usuario.query.get(usuario_id)
    if not usuario:
        return None
    if nombre:
        usuario.nombre = nombre
    if correo:
        usuario.correo = correo
    if activo is not None:
        usuario.activo = activo
    db.session.commit()
    return usuario

def eliminar_usuario(usuario_id):
    """Elimina un usuario por ID."""
    usuario = Usuario.query.get(usuario_id)
    if not usuario:
        return None
    db.session.delete(usuario)
    db.session.commit()
    return True
