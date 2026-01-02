import sqlite3

DB_PATH = "data/gastos.db"

def conectar():
    return sqlite3.connect(DB_PATH)

# CREATE
def insertar_gasto(fecha, categoria, monto, descripcion):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO gastos (fecha, categoria, monto, descripcion)
        VALUES (?, ?, ?, ?)
    """, (fecha, categoria, monto, descripcion))
    conn.commit()
    conn.close()

# READ
def obtener_gastos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM gastos")
    datos = cursor.fetchall()
    conn.close()
    return datos

# UPDATE
def actualizar_gasto(id_gasto, monto):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE gastos SET monto = ?
        WHERE id = ?
    """, (monto, id_gasto))
    conn.commit()
    conn.close()

# DELETE
def eliminar_gasto(id_gasto):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM gastos WHERE id = ?", (id_gasto,))
    conn.commit()
    conn.close()

