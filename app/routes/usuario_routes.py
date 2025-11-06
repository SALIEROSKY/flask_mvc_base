from flask import Blueprint, jsonify, request, render_template, redirect, url_for, flash
from app.controllers.usuario_controller import (
    obtener_usuarios,
    obtener_usuario_por_id,
    crear_usuario,
    actualizar_usuario,
    eliminar_usuario
)

usuario_bp = Blueprint('usuario_bp', __name__, template_folder='../templates', static_folder='../static')

# ------------------- API JSON ------------------- #

@usuario_bp.route('/usuarios', methods=['GET'])
def listar_usuarios():
    usuarios = obtener_usuarios()
    data = [{"id": u.id, "nombre": u.nombre, "correo": u.correo, "activo": u.activo} for u in usuarios]
    return jsonify(data), 200


@usuario_bp.route('/usuarios/<int:usuario_id>', methods=['GET'])
def obtener_usuario(usuario_id):
    usuario = obtener_usuario_por_id(usuario_id)
    if not usuario:
        return jsonify({"mensaje": "Usuario no encontrado"}), 404
    return jsonify({
        "id": usuario.id,
        "nombre": usuario.nombre,
        "correo": usuario.correo,
        "activo": usuario.activo
    }), 200


@usuario_bp.route('/usuarios', methods=['POST'])
def crear():
    data = request.get_json()
    nuevo = crear_usuario(data["nombre"], data["correo"])
    return jsonify({"mensaje": "Usuario creado", "id": nuevo.id}), 201


@usuario_bp.route('/usuarios/<int:usuario_id>', methods=['PUT'])
def actualizar(usuario_id):
    data = request.get_json()
    usuario = actualizar_usuario(
        usuario_id,
        nombre=data.get("nombre"),
        correo=data.get("correo"),
        activo=data.get("activo")
    )
    if not usuario:
        return jsonify({"mensaje": "Usuario no encontrado"}), 404
    return jsonify({"mensaje": "Usuario actualizado"}), 200


@usuario_bp.route('/usuarios/<int:usuario_id>', methods=['DELETE'])
def eliminar(usuario_id):
    resultado = eliminar_usuario(usuario_id)
    if not resultado:
        return jsonify({"mensaje": "Usuario no encontrado"}), 404
    return jsonify({"mensaje": "Usuario eliminado"}), 200


# ------------------- VISTAS HTML ------------------- #

@usuario_bp.route('/usuarios/html', methods=['GET'])
def vista_usuarios():
    usuarios = obtener_usuarios()
    return render_template('usuarios/index.html', usuarios=usuarios)


@usuario_bp.route('/usuarios/nuevo', methods=['GET', 'POST'])
def nuevo_usuario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        crear_usuario(nombre, correo)
        flash("Usuario creado con éxito.", "success")
        return redirect(url_for('usuario_bp.vista_usuarios'))
    return render_template('usuarios/nuevo.html')


@usuario_bp.route('/usuarios/<int:usuario_id>/editar', methods=['GET', 'POST'])
def editar_usuario(usuario_id):
    usuario = obtener_usuario_por_id(usuario_id)
    if not usuario:
        flash("Usuario no encontrado.", "danger")
        return redirect(url_for('usuario_bp.vista_usuarios'))

    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        activo = 'activo' in request.form
        actualizar_usuario(usuario_id, nombre=nombre, correo=correo, activo=activo)
        flash("Usuario actualizado con éxito.", "success")
        return redirect(url_for('usuario_bp.vista_usuarios'))

    return render_template('usuarios/editar.html', usuario=usuario)