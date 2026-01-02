def resumen_general(df):
    total = df["monto"].sum()
    promedio = df["monto"].mean()

    return total, promedio


def gastos_por_categoria(df):
    return df.groupby("categoria")["monto"].sum()


def categoria_mayor_gasto(gastos_categoria):
    categoria = gastos_categoria.idxmax()
    monto = gastos_categoria.max()

    return categoria, monto
