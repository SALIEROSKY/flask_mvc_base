from flask import Blueprint, render_template, session, redirect, url_for
from app.models.usuario import Usuario
from app.models.rol import Rol
from app.utils.decorators import login_required, role_required

dashboard_bp = Blueprint('dashboard_bp', __name__, template_folder='../templates', static_folder='../static')

@dashboard_bp.route('/dashboard')
@login_required
@role_required('admin')
def dashboard():
    # Datos del panel
    total_usuarios = Usuario.query.count()
    total_activos = Usuario.query.filter_by(activo=True).count()
    total_roles = Rol.query.count()

    return render_template(
        'admin/dashboard.html',
        nombre=session.get('nombre'),
        total_usuarios=total_usuarios,
        total_activos=total_activos,
        total_roles=total_roles
    )
