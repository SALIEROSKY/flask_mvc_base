from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    # --- Rutas ---
    from app.routes.usuario_routes import usuario_bp
    from app.routes.auth_routes import auth_bp

    app.register_blueprint(usuario_bp)
    app.register_blueprint(auth_bp)

    # --- Crear tablas y usuario admin ---
    with app.app_context():
        from app.models.usuario import Usuario

        db.create_all()

        # Crear usuario administrador por defecto
        if not Usuario.query.filter_by(correo='admin@mail.com').first():
            admin = Usuario(
                nombre='Administrador',
                correo='admin@mail.com',
                activo=True,
                password_hash=generate_password_hash("admin123")  # 👈 aquí se genera el hash
            )
            db.session.add(admin)
            db.session.commit()
            print("✅ Usuario administrador creado: admin@mail.com / admin123")
        else:
            print("ℹ️ Usuario administrador ya existe")

        # Probar conexión
        try:
            db.engine.connect()
            print("✅ Conexión exitosa a SQL Server")
        except Exception as e:
            print("❌ Error de conexión:", e)

    return app
