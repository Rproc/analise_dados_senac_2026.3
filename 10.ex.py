import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# OBTER DADOS
try:
    dados = pd.read_csv(
        '03.BaseDPEvolucaoMensalCisp.csv',
        sep=';', encoding='iso-8859-1')
    dp = pd.read_csv('08.DP.csv', sep=',', 
                     encoding='utf-8')
    # juntar com codDP
    df_comDP = dados.merge(dp, left_on='cisp',
                           right_on='codDP', how='left')
    
    # df_comDP.info()
    df_roubos = df_comDP[['cisp', 'nome', 'roubo_celular', 
                             'roubo_transeunte', 'ano', 'regiao']]
    
    df_roubos.fillna('Delegacia não informada', inplace=True)
    df_roubos.info()
except Exception as e:
    print(f'Erro ao obter dados: {e}')
    exit(1)




    