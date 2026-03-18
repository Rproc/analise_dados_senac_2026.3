import pandas as pd
import polars as pl
import time

arquivo = '03.BaseDPEvolucaoMensalCisp.csv'

print('---------- Teste Pandas -------------')
inicio = time.time()

df_pandas = pd.read_csv(arquivo, sep=';',
                encoding='iso-8859-1')
media = df_pandas['roubo_veiculo'].mean()
filtro = (
    df_pandas[df_pandas['roubo_veiculo'] > 50])
agrupado = (df_pandas. 
    groupby('regiao')['roubo_veiculo'].mean())

fim = time.time()
tempo_pandas = fim - inicio
print(f'Tempo do Pandas: {tempo_pandas}')

print('----------- Polars ------------')
inicio_polars = time.time()
df_polars = pl.read_csv(arquivo, separator=';',
                        encoding='iso-8859-1')
media = df_polars.select(
    pl.col('roubo_veiculo').mean()
)
filtro = df_polars.filter(
    pl.col('roubo_veiculo') > 50
)
agrupado = df_polars.group_by('regiao').agg(
    pl.col('roubo_veiculo').mean()
)
fim_polars = time.time()
tempo_polars = fim_polars - inicio_polars
print(f'Tempo Polars: {tempo_polars}')

div = tempo_pandas/tempo_polars
print(f'Polars é {div} vezes mais rapido que o \
      Pandas')