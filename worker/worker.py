import psycopg2
import time
import os

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
        port=DB_PORT
    )

def procesar():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM usuarios;")
        total = cur.fetchone()[0]
        print(f"[Worker] Total usuarios en DB: {total}")
        cur.execute("""
            INSERT INTO usuarios (nombre, email)
            VALUES ('Worker Auto', 'worker@auto.com')
            RETURNING id;
        """)
        nuevo_id = cur.fetchone()[0]
        conn.commit()
        print(f"[Worker] Usuario insertado automaticamente con id: {nuevo_id}")
        cur.close()
        conn.close()
    except Exception as e:
        print(f"[Worker] Error: {e}")

if __name__ == "__main__":
    print("[Worker] Iniciando servicio de procesamiento...")
    while True:
        procesar()
        print("[Worker] Esperando 10 segundos...")
        time.sleep(10)
