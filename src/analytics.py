import pandas as pd
import sqlite3

def cargar_dataframe():
    conn = sqlite3.connect("data/gastos.db")
    df = pd.read_sql("SELECT * FROM gastos", conn)
    conn.close()
    return df

def resumen(df):
    return {
        "total": df["monto"].sum(),
        "promedio": df["monto"].mean(),
        "por_categoria": df.groupby("categoria")["monto"].sum()
    }
