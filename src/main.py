from plots import grafico_categoria, grafico_mensual
from db import conectar_db, cargar_gastos
from analytics import (
    resumen_general,
    gastos_por_categoria,
    categoria_mayor_gasto
)

#  Conectar a la base de datos
conexion = conectar_db()

#  Cargar datos
df = cargar_gastos(conexion)
print("\nDATOS DE GASTOS")
print(df)

#  Resumen general
total, promedio = resumen_general(df)
print("\n--- RESUMEN GENERAL ---")
print(f"Total gastado: ${total:,.0f}")
print(f"Gasto promedio: ${promedio:,.0f}")

#  Gastos por categoría
gastos_categoria = gastos_por_categoria(df)
print("\nGASTOS POR CATEGORÍA")
print(gastos_categoria)

#  Categoría top
categoria_top, monto_top = categoria_mayor_gasto(gastos_categoria)
print("\nCATEGORÍA CON MÁS GASTO")
print(f"{categoria_top}: ${monto_top:,.0f}")

grafico_categoria(gastos_categoria)
grafico_mensual(df)

#  Guardar CSV
gastos_categoria.to_csv("data/resumen_categoria.csv")
print("\nArchivo resumen_categoria.csv guardado")


#  Cerrar conexión
conexion.close()
