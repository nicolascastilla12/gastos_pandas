import sqlite3
import pandas as pd

def conectar_db(ruta_db="data/gastos.db"):
    """
    Crea y devuelve la conexión a la base de datos
    """
    return sqlite3.connect(ruta_db)


def cargar_gastos(conexion):
    """
    Lee la tabla gastos y la convierte en DataFrame
    """
    query = "SELECT * FROM gastos"
    df = pd.read_sql_query(query, conexion)
    return df
