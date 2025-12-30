import sqlite3
import pandas as pd

conexion = sqlite3.connect("data/gastos.db")

# Ver tablas
tablas = pd.read_sql_query(
    "SELECT name FROM sqlite_master WHERE type='table';",
    conexion
)
print("\n TABLAS:")
print(tablas)

# Ver estructura
estructura = pd.read_sql_query(
    "PRAGMA table_info(gastos);",
    conexion
)
print("\n ESTRUCTURA:")
print(estructura)

# Ver datos
df = pd.read_sql_query("SELECT * FROM gastos", conexion)
print("\n DATOS:")
print(df)

conexion.close()

