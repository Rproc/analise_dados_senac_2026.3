import pandas as pd
import numpy as np
# 1. Criar dados ficticios
# media = 33 // mediana = 21
dados = \
    np.array([10, 25, 56, 8, 17, 12, 85, 49, 72, 1])

q1 = np.percentile(dados, 25) # 25% do todo
q2 = np.percentile(dados, 50) # 50% (Mediana)
q3 = np.percentile(dados, 75) # 75% do todo

print(f'Primeiro Quartil (Q1 - mais rapidos): {q1}')
print(f'Segundo Quartil (Q2 - Mediana/Padrão): {q2}')
print(f'Terceiro Quartil (Q3 - mais lentos): {q3}')

media = np.mean(dados)
delta_media_mediana = media - q2
print(f'Média: {media}')
print(f'Diferença entre média e mediana: \
      {delta_media_mediana:,.2f}')


