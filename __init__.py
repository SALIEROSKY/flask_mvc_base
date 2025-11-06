from flasgger import Swagger

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    # Swagger configuración básica
    app.config['SWAGGER'] = {
        'title': 'Flask MVC Base - API',
        'uiversion': 3
    }
    Swagger(app)

    # Registrar blueprint de usuarios
    from app.routes.usuario_routes import usuario_bp
    app.register_blueprint(usuario_bp)

    return app
    with app.app_context():
        try:
            db.engine.connect()
            print("✅ Conexión exitosa a SQL Server")
        except Exception as e:
            print("❌ Error de conexión:", e)

        # Registrar rutas
        from app.routes.usuario_routes import usuario_bp
        app.register_blueprint(usuario_bp)