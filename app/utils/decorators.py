from functools import wraps
from flask import session, redirect, url_for, flash

# 🔹 Requiere login
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'usuario_id' not in session:
            flash('Debes iniciar sesión para acceder a esta sección.', 'warning')
            return redirect(url_for('auth_bp.login'))
        return f(*args, **kwargs)
    return decorated_function


# 🔹 Requiere rol específico (por ejemplo, admin)
def role_required(*roles):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            user_role = session.get('rol')
            if not user_role:
                flash('Debes iniciar sesión para acceder a esta sección.', 'warning')
                return redirect(url_for('auth_bp.login'))

            if user_role not in roles:
                flash('No tienes permisos para acceder a esta sección.', 'danger')

                # ⚠️ Cambiado: antes redirigía a un endpoint inexistente
                # Debe redirigir a un panel o vista válida
                if user_role == 'admin':
                    return redirect(url_for('dashboard_bp.dashboard'))
                else:
                    return redirect(url_for('auth_bp.bienvenido'))

            return f(*args, **kwargs)
        return decorated_function
    return decorator
