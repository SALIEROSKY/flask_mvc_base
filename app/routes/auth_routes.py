from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import check_password_hash
from app.models.usuario import Usuario
from app import db

auth_bp = Blueprint('auth_bp', __name__, template_folder='../templates', static_folder='../static')

# ------------------- LOGIN ------------------- #

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    # Si ya hay sesión activa, redirigir según el rol
    if session.get('usuario_id'):
        rol = session.get('rol')
        if rol == 'admin':
            return redirect(url_for('dashboard_bp.dashboard'))
        else:
            return redirect(url_for('auth_bp.bienvenido'))

    if request.method == 'POST':
        correo = request.form.get('correo')
        password = request.form.get('password')

        usuario = Usuario.query.filter_by(correo=correo).first()

        if not usuario or not check_password_hash(usuario.password_hash, password):
            flash("Correo o contraseña incorrectos.", "danger")
            return render_template('auth/login.html')

        if not usuario.activo:
            flash("Tu cuenta está inactiva. Contacta al administrador.", "warning")
            return render_template('auth/login.html')

        # Guardar sesión
        session['usuario_id'] = usuario.id
        session['usuario_nombre'] = usuario.nombre
        session['rol'] = usuario.rol.nombre

        flash(f"Bienvenido, {usuario.nombre}", "success")

        # Redirigir según rol
        if usuario.rol.nombre == 'admin':
            return redirect(url_for('dashboard_bp.dashboard'))
        else:
            return redirect(url_for('auth_bp.bienvenido'))

    return render_template('auth/login.html')


# ------------------- LOGOUT ------------------- #

@auth_bp.route('/logout')
def logout():
    session.clear()
    flash("Has cerrado sesión correctamente.", "info")
    return redirect(url_for('auth_bp.login'))


# ------------------- BIENVENIDA USUARIO (no admin) ------------------- #

@auth_bp.route('/bienvenido')
def bienvenido():
    if 'usuario_id' not in session:
        return redirect(url_for('auth_bp.login'))

    return render_template('auth/bienvenido.html', nombre=session.get('usuario_nombre'))
