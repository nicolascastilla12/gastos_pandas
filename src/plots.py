import matplotlib.pyplot as plt
import pandas as pd


def grafico_categoria(gastos_categoria):
    gastos_categoria.plot(kind="bar")
    plt.title("Gastos por Categoría")
    plt.xlabel("Categoría")
    plt.ylabel("Monto")
    plt.tight_layout()
    plt.show()


def grafico_mensual(df):
    df["fecha"] = pd.to_datetime(df["fecha"])
    df["mes"] = df["fecha"].dt.to_period("M")

    gastos_mes = df.groupby("mes")["monto"].sum()

    gastos_mes.plot(marker="o")
    plt.title("Tendencia de Gastos Mensual")
    plt.xlabel("Mes")
    plt.ylabel("Monto")
    plt.tight_layout()
    plt.show()
