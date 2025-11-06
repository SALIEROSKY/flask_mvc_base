from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.models.usuario import Usuario
from app import db

auth_bp = Blueprint('auth_bp', __name__, template_folder='../templates', static_folder='../static')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form['correo']
        password = request.form['password']

        usuario = Usuario.query.filter_by(correo=correo).first()
        if usuario and usuario.check_password(password):
            session['usuario_id'] = usuario.id
            flash("Inicio de sesión exitoso.", "success")
            return redirect(url_for('usuario_bp.vista_usuarios'))
        else:
            flash("Credenciales inválidas.", "danger")

    return render_template('base/login.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    flash("Sesión cerrada correctamente.", "info")
    return redirect(url_for('auth_bp.login'))
