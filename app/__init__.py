from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from datetime import datetime

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    # --- Importar modelos antes de crear tablas ---
    from app.models.usuario import Usuario
    from app.models.rol import Rol

    # --- Importar rutas ---
    from app.routes.usuario_routes import usuario_bp
    from app.routes.auth_routes import auth_bp
    from app.routes.rol_routes import rol_bp
    from app.routes.dashboard_routes import dashboard_bp

    # --- Registrar blueprints ---
    app.register_blueprint(usuario_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(rol_bp)
    app.register_blueprint(dashboard_bp)

    # --- Crear tablas y datos base ---
    with app.app_context():
        db.create_all()

        # Crear roles si no existen
        if not Rol.query.first():
            admin_rol = Rol(nombre="admin")
            user_rol = Rol(nombre="user")
            db.session.add_all([admin_rol, user_rol])
            db.session.commit()
            print("✅ Roles creados: admin / user")

        # Crear usuario admin si no existe
        if not Usuario.query.filter_by(correo='admin@mail.com').first():
            admin_rol = Rol.query.filter_by(nombre="admin").first()
            admin = Usuario(
                nombre="Administrador",
                correo="admin@mail.com",
                activo=True,
                rol=admin_rol
            )
            admin.set_password("admin123")
            db.session.add(admin)
            db.session.commit()
            print("✅ Usuario administrador creado con rol admin")

        # --- Probar conexión ---
        try:
            db.engine.connect()
            print("✅ Conexión exitosa a SQL Server")
        except Exception as e:
            print("❌ Error de conexión:", e)

        # 👉 Añadimos el context processor aquí (fuera del if)
        @app.context_processor
        def inject_now():
            return {'now': datetime.now}

    return app
