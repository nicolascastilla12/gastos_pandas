import matplotlib.pyplot as plt
import pandas as pd

def grafico_categoria(df):
    gastos = df.groupby("categoria")["monto"].sum()
    gastos.plot(kind="bar")
    plt.title("Gastos por Categoría")
    plt.xlabel("Categoría")
    plt.ylabel("Monto")
    plt.tight_layout()
    plt.show()
