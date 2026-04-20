from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "db"),
        database=os.getenv("DB_NAME", "appdb"),
        user=os.getenv("DB_USER", "appuser"),
        password=os.getenv("DB_PASSWORD", "apppassword"),
        port=os.getenv("DB_PORT", "5432")
    )

def init_db():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id SERIAL PRIMARY KEY,
                nombre VARCHAR(100),
                email VARCHAR(100)
            )
        """)
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error iniciando DB: {e}")

@app.route("/")
def home():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT version();")
        version = cur.fetchone()[0]
        cur.close()
        conn.close()
        return jsonify({
            "estado": "Aplicación funcionando correctamente",
            "database": "PostgreSQL conectado",
            "version": version
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/data")
def data():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, nombre, email FROM usuarios;")
        filas = cur.fetchall()
        cur.close()
        conn.close()
        usuarios = [
            {"id": f[0], "nombre": f[1], "email": f[2]}
            for f in filas
        ]
        return jsonify({"total": len(usuarios), "usuarios": usuarios})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/insert")
def insert():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO usuarios (nombre, email)
            VALUES ('Usuario Demo', 'demo@correo.com')
            RETURNING id;
        """)
        nuevo_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({
            "mensaje": "Usuario insertado correctamente",
            "id": nuevo_id
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)
