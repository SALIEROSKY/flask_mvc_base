from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from app.utils.decorators import login_required, role_required
from app.controllers.rol_controller import (
    obtener_roles,
    obtener_rol_por_id,
    crear_rol,
    actualizar_rol,
    eliminar_rol
)

rol_bp = Blueprint('rol_bp', __name__, template_folder='../templates', static_folder='../static')

# ------------------- API JSON ------------------- #

@rol_bp.route('/api/roles', methods=['GET'])
def api_listar_roles():
    roles = obtener_roles()
    data = [{"id": r.id, "nombre": r.nombre} for r in roles]
    return jsonify(data), 200


@rol_bp.route('/api/roles', methods=['POST'])
def api_crear_rol():
    data = request.get_json()
    rol = crear_rol(data["nombre"])
    if not rol:
        return jsonify({"mensaje": "El rol ya existe."}), 400
    return jsonify({"mensaje": "Rol creado exitosamente."}), 201


@rol_bp.route('/api/roles/<int:rol_id>', methods=['PUT'])
def api_actualizar_rol(rol_id):
    data = request.get_json()
    rol = actualizar_rol(rol_id, data["nombre"])
    if not rol:
        return jsonify({"mensaje": "Rol no encontrado."}), 404
    return jsonify({"mensaje": "Rol actualizado exitosamente."}), 200


@rol_bp.route('/api/roles/<int:rol_id>', methods=['DELETE'])
def api_eliminar_rol(rol_id):
    resultado = eliminar_rol(rol_id)
    if resultado is None:
        return jsonify({"mensaje": "Rol no encontrado."}), 404
    elif resultado is False:
        return jsonify({"mensaje": "No se puede eliminar: hay usuarios asignados."}), 400
    return jsonify({"mensaje": "Rol eliminado correctamente."}), 200

# ------------------- VISTAS HTML (con seguridad) ------------------- #

@rol_bp.route('/roles/html', methods=['GET'])
@login_required
@role_required('admin')
def vista_roles():
    roles = obtener_roles()
    return render_template('roles/index.html', roles=roles)


@rol_bp.route('/roles/nuevo', methods=['GET', 'POST'])
@login_required
@role_required('admin')
def nuevo_rol():
    if request.method == 'POST':
        nombre = request.form['nombre']
        rol = crear_rol(nombre)
        if not rol:
            flash("Ya existe un rol con ese nombre.", "danger")
        else:
            flash("Rol creado correctamente.", "success")
        return redirect(url_for('rol_bp.vista_roles'))
    return render_template('roles/nuevo.html')


@rol_bp.route('/roles/<int:rol_id>/editar', methods=['GET', 'POST'])
@login_required
@role_required('admin')
def editar_rol(rol_id):
    rol = obtener_rol_por_id(rol_id)
    if not rol:
        flash("Rol no encontrado.", "danger")
        return redirect(url_for('rol_bp.vista_roles'))

    if request.method == 'POST':
        nombre = request.form['nombre']
        actualizar_rol(rol_id, nombre)
        flash("Rol actualizado correctamente.", "success")
        return redirect(url_for('rol_bp.vista_roles'))

    return render_template('roles/editar.html', rol=rol)
