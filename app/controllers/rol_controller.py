from app import db
from app.models.rol import Rol

def obtener_roles():
    """Devuelve todos los roles registrados."""
    return Rol.query.order_by(Rol.id.asc()).all()

def obtener_rol_por_id(rol_id):
    """Devuelve un rol específico por ID."""
    return Rol.query.get(rol_id)

def crear_rol(nombre):
    """Crea un nuevo rol si no existe otro con el mismo nombre."""
    if Rol.query.filter_by(nombre=nombre).first():
        return None  # Ya existe
    nuevo = Rol(nombre=nombre)
    db.session.add(nuevo)
    db.session.commit()
    return nuevo

def actualizar_rol(rol_id, nombre):
    """Actualiza el nombre de un rol existente."""
    rol = Rol.query.get(rol_id)
    if not rol:
        return None
    rol.nombre = nombre
    db.session.commit()
    return rol

def eliminar_rol(rol_id):
    """Elimina un rol si no está asignado a usuarios."""
    rol = Rol.query.get(rol_id)
    if not rol:
        return None

    if rol.usuarios and len(rol.usuarios) > 0:
        return False  # No puede eliminarse si tiene usuarios asignados

    db.session.delete(rol)
    db.session.commit()
    return True
