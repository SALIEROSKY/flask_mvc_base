import os
from dotenv import load_dotenv

# Cargar variables desde el .env
load_dotenv()

class Config:
    # === Clave secreta para sesiones y mensajes flash ===
    SECRET_KEY = os.getenv("SECRET_KEY", "dev_key_flask_123")

    # === Configuración de Base de Datos (Windows Authentication) ===
    DB_DRIVER = os.getenv("DB_DRIVER")
    DB_SERVER = os.getenv("DB_SERVER")
    DB_NAME = os.getenv("DB_NAME")
    DB_TRUSTED = os.getenv("DB_TRUSTED", "yes")

    SQLALCHEMY_DATABASE_URI = (
        f"mssql+pyodbc://@{DB_SERVER}/{DB_NAME}"
        f"?driver={DB_DRIVER}&trusted_connection={DB_TRUSTED}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

