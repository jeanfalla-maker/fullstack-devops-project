from flask import Flask
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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
