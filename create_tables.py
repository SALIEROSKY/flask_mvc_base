from app import create_app, db
from app.models.usuario import Usuario

app = create_app()

with app.app_context():
    print("🧹 Eliminando tablas existentes...")
    db.drop_all()
    db.create_all()

    if not Usuario.query.first():
        print("🛠 Creando usuario administrador...")
        admin = Usuario(nombre="Administrador", correo="admin@mail.com", activo=True)
        admin.set_password("admin123")  # 👈 aquí se genera el hash correctamente
        db.session.add(admin)
        db.session.commit()
        print("✅ Usuario administrador creado con éxito.")
