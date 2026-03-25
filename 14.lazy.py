import polars as pl
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

ENDERECO_DADOS = \
r'C:/Users/renan.duarte/Documents/analise_dados_senac_2026.3/dados_bronze/'


try:
    print('Lendo arquivo parquet')

    hora_inicio = dt.datetime.now()
    # cria um plano de execução sobre o futuro df
    df_bf_exec_plan = pl.scan_parquet(
        ENDERECO_DADOS + 'bf.parquet'
    )
    # vira um dataframe quando eu coleto
    df_bf = df_bf_exec_plan.collect()
    hora_fim = dt.datetime.now()
    print(df_bf.columns)
    print(df_bf.head())
    print(f'Tempo de Execução: {hora_fim-hora_inicio}')
except Exception as e:
    print(f'Erro ao obter dados parquet: {e}')
