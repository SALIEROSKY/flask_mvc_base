from app import create_app, db
from app.models.usuario import Usuario
from app.models.rol import Rol

app = create_app()

with app.app_context():
    print("🧹 Eliminando tablas existentes...")
    db.drop_all()
    db.create_all()

    print("🛠 Creando roles base...")
    rol_user = Rol(nombre="user")
    rol_admin = Rol(nombre="admin")

    db.session.add_all([rol_user, rol_admin])
    db.session.commit()

    print("✅ Roles creados con éxito.")

    # Crear usuario administrador
    if not Usuario.query.first():
        print("🧑‍💼 Creando usuario administrador...")
        admin = Usuario(
            nombre="Administrador",
            correo="admin@mail.com",
            activo=True,
            rol_id=rol_admin.id  # 🔗 asignar rol de administrador
        )
        admin.set_password("admin123")
        db.session.add(admin)
        db.session.commit()
        print("✅ Usuario administrador creado con éxito.")
    else:
        print("ℹ️ Ya existen usuarios en la base de datos.")
    print("🎉 ¡Tablas creadas y datos iniciales insertados con éxito!")