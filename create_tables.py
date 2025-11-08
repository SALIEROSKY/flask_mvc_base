from app import create_app, db
from app.models.usuario import Usuario
from app.models.rol import Rol  # 🔹 importa también el modelo Rol

app = create_app()

with app.app_context():
    print("🧹 Eliminando tablas existentes...")
    db.drop_all()  # 🔥 borra todas las tablas
    db.create_all()  # 🚀 crea todas las tablas nuevamente

    # Crear roles base
    if not Rol.query.first():
        admin_role = Rol(nombre="admin")
        user_role = Rol(nombre="user")
        db.session.add_all([admin_role, user_role])
        db.session.commit()
        print("✅ Roles creados: admin / user")

    # Crear usuario administrador
    if not Usuario.query.filter_by(correo='admin@mail.com').first():
        admin_role = Rol.query.filter_by(nombre="admin").first()
        admin = Usuario(
            nombre="Administrador",
            correo="admin@mail.com",
            activo=True,
            rol_id=admin_role.id
        )
        admin.set_password("admin123")
        db.session.add(admin)
        db.session.commit()
        print("✅ Usuario administrador creado correctamente.")
