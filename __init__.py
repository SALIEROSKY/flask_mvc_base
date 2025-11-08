from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger
from config import Config
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar DB
    db.init_app(app)

    # Configuración de Swagger
    app.config['SWAGGER'] = {
        'title': 'Flask MVC Base - API',
        'uiversion': 3
    }
    Swagger(app)

    # Importar y registrar blueprints
    from app.routes.usuario_routes import usuario_bp
    from app.routes.auth_routes import auth_bp
    from app.routes.rol_routes import rol_bp  # 👈 Nuevo blueprint

    app.register_blueprint(usuario_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(rol_bp)

    # Crear tablas y usuario admin
    with app.app_context():
        from app.models.usuario import Usuario
        from app.models.rol import Rol

        db.create_all()

        # Crear roles base
        if not Rol.query.first():
            admin_rol = Rol(nombre='admin')
            user_rol = Rol(nombre='user')
            db.session.add_all([admin_rol, user_rol])
            db.session.commit()
            print("✅ Roles creados: admin / user")

        # Crear usuario administrador por defecto
        if not Usuario.query.filter_by(correo='admin@mail.com').first():
            admin_role = Rol.query.filter_by(nombre='admin').first()
            admin = Usuario(
                nombre='Administrador',
                correo='admin@mail.com',
                activo=True,
                password_hash=generate_password_hash("admin123"),
                rol_id=admin_role.id  # 👈 relación con rol
            )
            db.session.add(admin)
            db.session.commit()
            print("✅ Usuario administrador creado: admin@mail.com / admin123")
        else:
            print("ℹ️ Usuario administrador ya existe")

        # Probar conexión a SQL Server
        try:
            db.engine.connect()
            print("✅ Conexión exitosa a SQL Server")
        except Exception as e:
            print("❌ Error de conexión:", e)

    return app
