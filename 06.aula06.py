import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


try:
    # enconding = 'latin1' 
    # enconding = 'IBM860'
    # enconding = 'iso-8859-1' (pega quase sempre)
    df = pd.read_csv('03.BaseDPEvolucaoMensalCisp.csv',
                     encoding='iso-8859-1', sep=';')
    # print(df.head())
    print(df.columns)
except Exception as e:
    print(f'Erro: {e}')
    exit()


# filtrar
df_roubo_veiculos = df[['munic', 'roubo_veiculo']]
# print(df_roubo_veiculos.head())

# agrupar por municipio
df_roubo_veiculos = df_roubo_veiculos.groupby('munic').sum()\
.reset_index().sort_values(by='roubo_veiculo', ascending=False)
df_roubo_veiculos

# transformar dataframe em array
roubo_veiculo_array = np.array(df_roubo_veiculos['roubo_veiculo'])

amplitude = np.max(roubo_veiculo_array) - np.min(roubo_veiculo_array)

media_roubos = np.mean(roubo_veiculo_array)
mediana_roubos = np.median(roubo_veiculo_array)

q1 = np.quantile(roubo_veiculo_array, 0.25)
q2 = np.quantile(roubo_veiculo_array, 0.50)
q3 = np.quantile(roubo_veiculo_array, 0.75)

iqr = q3 - q1
# limite superior -> Identificar outliers acima de q3
limite_superior = q3 + 1.5*iqr
# limite inferior -> Identificar outliers abaixo de q1
limite_inferior = q1 - 1.5*iqr 

desvio = np.std(roubo_veiculo_array)
variancia = np.var(roubo_veiculo_array)
distancia_var_media = abs(variancia/media_roubos**2) # ^
cv = desvio/media_roubos

assimetria = df_roubo_veiculos['roubo_veiculo'].skew()
kurt = df_roubo_veiculos['roubo_veiculo'].kurtosis()


print(f'Média: {media_roubos}')
print(f'Mediana: {mediana_roubos}')
print(f'Min: {np.min(roubo_veiculo_array)}')
print(f'Limite Inferior: {limite_inferior}')
print(f'Q1: {q1}')
print(f'Q3: {q3}')
print(f'Limite Superior: {limite_superior}')
print(f'Max: {np.max(roubo_veiculo_array)}')
print(f'Distancia Variancia-Média:{distancia_var_media}')
print(f'Desvio Padrão: {desvio}')
print(f'Coeficiente de Variação: {cv}')
print(f'Assimetria: {assimetria}')
print(f'Curtose: {kurt}')

df_roubo_outliers_inferiores = df_roubo_veiculos[
    df_roubo_veiculos['roubo_veiculo'] < limite_inferior]

df_roubo_outliers_superiores = df_roubo_veiculos[
    df_roubo_veiculos['roubo_veiculo'] > limite_superior]


# Outliers Inferiores
if df_roubo_outliers_inferiores.empty:
    print('Não há outliers inferiores')
else:
    print(df_roubo_outliers_inferiores.sort_values(by='roubo_veiculo', ascending=True))

# Outliers Superiores
if df_roubo_outliers_superiores.empty:
    print('Não há outliers superiores')
else:
    print(df_roubo_outliers_superiores.sort_values(by='roubo_veiculo', ascending=False))
    

# Histograma
plt.hist(roubo_veiculo_array, bins=50)
plt.axvline(x=media_roubos, color='red')
plt.show()

# x, y
plt.bar(df_roubo_outliers_superiores['munic'],
        df_roubo_outliers_superiores['roubo_veiculo'])
plt.xticks(rotation=90)
plt.title('Ranking das Cidades com Outliers Superiores')
plt.show()


# showmeans (True ou False) -> True marca a media
# showfliers (True ou False) -> True mostra os outliers
# vert (True ou False) -> True = direção na vertical
plt.boxplot(roubo_veiculo_array, vert=True,
            showmeans=True, showfliers=True)
plt.show()

# sem outliers
plt.boxplot(roubo_veiculo_array, vert=True,
            showmeans=True, showfliers=False)
plt.show()