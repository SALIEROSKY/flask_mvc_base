# 🧩 Flask MVC Base

## 📘 Descripción General

**Flask MVC Base** es una aplicación base desarrollada en **Flask** que implementa el patrón **Modelo–Vista–Controlador (MVC)**.  
Sirve como plantilla modular y escalable para proyectos web, con autenticación, manejo de sesiones, control de roles y un panel administrativo básico.

Esta base fue diseñada para facilitar el inicio de nuevos proyectos Flask con una arquitectura limpia, reutilizable y enfocada en buenas prácticas de desarrollo backend.

---

## 🏗 Arquitectura del Proyecto

El proyecto sigue la estructura **MVC**, con separación clara entre modelos, vistas y controladores:

flask_mvc_base/
│
├── app/
│ ├── init.py # Configuración principal Flask y DB
│ ├── models/ # Modelos de base de datos (SQLAlchemy)
│ │ ├── usuario.py
│ │ └── rol.py
│ ├── controllers/ # Lógica de negocio
│ ├── routes/ # Blueprints modulares
│ │ ├── auth_routes.py
│ │ ├── usuario_routes.py
│ │ ├── rol_routes.py
│ │ └── dashboard_routes.py
│ ├── templates/ # Vistas HTML (Jinja2)
│ │ ├── base/ # Layout, navbar, sidebar
│ │ ├── auth/ # Login y bienvenida
│ │ ├── usuarios/ # CRUD de usuarios
│ │ └── roles/ # CRUD de roles
│ ├── static/ # Archivos JS, CSS, imágenes
│ └── utils/ # Decoradores y funciones auxiliares
│
├── config.py # Configuración global (DB, claves)
├── run.py # Punto de entrada principal
├── requirements.txt # Dependencias del proyecto
└── README.md # Documentación


---

## 🔐 Funcionalidades Principales

✅ **Autenticación de Usuarios**
- Inicio/cierre de sesión con verificación de credenciales.
- Contraseñas seguras con `Werkzeug` (hash SHA256).
- Control de acceso mediante sesión Flask.

✅ **Gestión de Roles**
- Roles predefinidos: `admin` y `user`.
- Acceso restringido con decoradores personalizados:
  ```python
  @login_required
  @role_required('admin')
✅ Panel Administrativo (Dashboard)

Accesible solo para usuarios con rol admin.

Estadísticas básicas: usuarios totales, activos, roles registrados.

✅ CRUD de Usuarios y Roles
Crear, editar, eliminar y listar usuarios y roles.
Endpoints HTML y API JSON.
Validación de unicidad y estado activo/inactivo.

✅ Seguridad y Control de Sesión
Protección de rutas sensibles.
Manejo de sesión persistente por rol.
Redirección automática según permisos.

✅ Interfaz Moderna
Construida con Bootstrap 5 y MDBootstrap.
Componentes reutilizables (navbar, sidebar, layout).
Íconos integrados con Bootstrap Icons.

📦 Dependencias (requirements.txt)
blinker==1.9.0
click==8.3.0
colorama==0.4.6
Flask==3.1.2
Flask-SQLAlchemy==3.1.1
greenlet==3.2.4
itsdangerous==2.2.0
Jinja2==3.1.6
MarkupSafe==3.0.3
pyodbc==5.3.0
python-dotenv==1.2.1
SQLAlchemy==2.0.44
typing_extensions==4.15.0
Werkzeug==3.1.3

💡 Propósito del Proyecto

Este proyecto fue desarrollado como base estructural para proyectos Flask profesionales, integrando:

Arquitectura modular basada en MVC.
Buenas prácticas de seguridad y manejo de sesiones.
Estandarización de rutas y vistas con Blueprints.
Integración nativa con Microsoft SQL Server.
Listo para escalar con API REST o integración front-end moderna (React, Vue, etc.).


| Categoría            | Tecnologías                                       |
| -------------------- | ------------------------------------------------- |
| **Backend**          | Python 3.x, Flask, Flask-SQLAlchemy               |
| **Frontend**         | HTML5, CSS3, JavaScript, Bootstrap 5, MDBootstrap |
| **Base de Datos**    | Microsoft SQL Server                              |
| **Plantillas**       | Jinja2                                            |
| **Seguridad**        | Werkzeug, Flask Session                           |
| **Patrón de Diseño** | MVC (Modelo-Vista-Controlador)                    |
| **Entorno**          | Visual Studio Code, entorno virtual venv          |
