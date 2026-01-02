import sqlite3

conexion = sqlite3.connect("data/gastos.db")
cursor = conexion.cursor()

cursor.execute("""
INSERT INTO gastos (fecha, categoria, monto, descripcion)
VALUES (?, ?, ?, ?)
""", ("2025-01-15", "Comida", 18000, "Almuerzo"))

conexion.commit()

cursor.execute("SELECT * FROM gastos")
for fila in cursor.fetchall():
    print(fila)

conexion.close()
