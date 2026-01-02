import sqlite3
import pandas as pd
from db import insertar_gasto, obtener_gastos, actualizar_gasto, eliminar_gasto
from analytics import cargar_dataframe, resumen
from plots import grafico_categoria

def menu():
    print("""
1. Insertar gasto
2. Ver gastos
3. Actualizar gasto
4. Eliminar gasto
5. Ver resumen
6. Ver gráfica
0. Salir
""")

while True:
    menu()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        fecha = input("Fecha (YYYY-MM-DD): ")
        categoria = input("Categoría: ")
        monto = float(input("Monto: "))
        desc = input("Descripción: ")
        insertar_gasto(fecha, categoria, monto, desc)

    elif opcion == "2":
        for g in obtener_gastos():
            print(g)

    elif opcion == "3":
        id_gasto = int(input("ID del gasto: "))
        nuevo_monto = float(input("Nuevo monto: "))
        actualizar_gasto(id_gasto, nuevo_monto)

    elif opcion == "4":
        id_gasto = int(input("ID del gasto: "))
        eliminar_gasto(id_gasto)

    elif opcion == "5":
        df = cargar_dataframe()
        r = resumen(df)
        print("Total:", r["total"])
        print("Promedio:", r["promedio"])
        print(r["por_categoria"])

    elif opcion == "6":
        df = cargar_dataframe()
        grafico_categoria(df)

    elif opcion == "0":
        break

# 1️ CONEXIÓN A SQLITE
conexion = sqlite3.connect("data/gastos.db")


 # LEER DATOS A PANDAS
df = pd.read_sql_query("SELECT * FROM gastos", conexion)


# TRANSFORMACIONES
# Total y promedio
total = df["monto"].sum()
promedio = df["monto"].mean()

# Gastos por categoría
gastos_categoria = df.groupby("categoria")["monto"].sum().reset_index()

# Gastos por mes
df["fecha"] = pd.to_datetime(df["fecha"])
df["mes"] = df["fecha"].dt.to_period("M")
gastos_mes = df.groupby("mes")["monto"].sum().reset_index()


# EXPORTAR A EXCEL (MULTI-HOJA)

ruta_excel = "data/reporte_gastos.xlsx"

with pd.ExcelWriter(ruta_excel, engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="Gastos", index=False)
    gastos_categoria.to_excel(writer, sheet_name="Por Categoria", index=False)
    gastos_mes.to_excel(writer, sheet_name="Por Mes", index=False)

print(" Archivo Excel creado correctamente:", ruta_excel)


#  CERRAR CONEXIÓN
conexion.close()
