import pandas as pd

#cargar un archivo

df = pd.read_csv("ventas.csv")

df.head()

df['total'] = df['precio'] * df['unidades']
df.head()

df.groupby('producto')['total'].sum()
df.head()

#filtro por unidades

df[df['unidades'] > 3]

#fecha

df['fecha'] = pd.to_datetime(df['fecha'])

df['mes'] = df['fecha'].dt.month

df.head()

#agrupar por mes

df.groupby('mes')['total'].sum()

