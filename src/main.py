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
