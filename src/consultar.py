import pandas as pd
from db import conectar

def ver_gastos():
    conexion = conectar()
    df = pd.read_sql_query("SELECT * FROM gastos", conexion)
    conexion.close()

    print("\n📋 LISTA DE GASTOS")
    print(df)
