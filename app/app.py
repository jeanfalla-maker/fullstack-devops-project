from flask import Flask
<<<<<<< HEAD
import mysql.connector
import os

app = Flask(__name__)

@app.route("/")
def home():
    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST", "db"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", "root"),
            database=os.getenv("DB_NAME", "prueba")
        )
        cursor = conn.cursor()
        cursor.execute("SELECT VERSION()")
        version = cursor.fetchone()[0]
        conn.close()
        return {
            "estado": "Conexión exitosa a MySQL",
            "version_mysql": version,
            "base_de_datos": "prueba"
        }
    except Exception as e:
        return {"error": str(e)}, 500
=======
import os
import psycopg2

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("DB_NAME", "appdb")
DB_USER = os.getenv("DB_USER", "appuser")
DB_PASSWORD = os.getenv("DB_PASSWORD", "apppassword")
DB_PORT = os.getenv("DB_PORT", "5432")


def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT,
    )

@app.route("/")
def home():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT version();")
        version = cur.fetchone()[0]
        cur.close()
        conn.close()
        return {
            "message": "Aplicación desplegada correctamente con Docker, Compose y Kubernetes",
            "database": "PostgreSQL conectado",
            "version": version,
        }
    except Exception as e:
        return {
            "message": "Aplicación funcionando, pero sin conexión a la base de datos",
            "error": str(e),
        }, 500

>>>>>>> c5e3112d4d7246ed49681412bdc7b842a4897666

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
