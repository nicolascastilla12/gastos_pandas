import sqlite3
import pandas as pd

# =========================
#  CONEXIÓN A LA BASE DE DATOS
# =========================
conexion = sqlite3.connect("data/gastos.db")

# =========================
# 2️ LEER DATOS DESDE SQL A PANDAS
# =========================
query = "SELECT * FROM gastos"
df = pd.read_sql_query(query, conexion)

print("\n DATOS DE GASTOS")
print(df)

# =========================
# 3️⃣ RESUMEN GENERAL
# =========================
total = df["monto"].sum()
promedio = df["monto"].mean()

print("\n--- RESUMEN GENERAL ---")
print(f" Total gastado: ${total:,.0f}")
print(f" Gasto promedio: ${promedio:,.0f}")

# =========================
#  GASTOS POR CATEGORÍA
# =========================
gastos_categoria = df.groupby("categoria")["monto"].sum()

print("\n GASTOS POR CATEGORÍA")
print(gastos_categoria)

# =========================
#  CATEGORÍA CON MÁS GASTO
# =========================
categoria_top = gastos_categoria.idxmax()
monto_top = gastos_categoria.max()

print("\n CATEGORÍA TOP")
print(f"Categoría: {categoria_top}")
print(f"Monto: ${monto_top:,.0f}")

# =========================
#  GUARDAR RESUMEN EN CSV
# =========================
gastos_categoria.to_csv("data/resumen_categoria.csv")
print("\n Archivo resumen_categoria.csv guardado")

# =========================
#  CERRAR CONEXIÓN
# =========================
conexion.close()
