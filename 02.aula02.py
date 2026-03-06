import pandas as pd
import numpy as np
df_vendas = pd.read_csv('01.amazon_sales_dataset.csv')

print(30*'-')
print(df_vendas.columns)
print(30*'-')
print(df_vendas.dtypes)
print(30*'-')
print(df_vendas.info())
print(30*'-')
print(30*'-')

coluna_alvo = 'total_sales'

# Medidas de Tendencia Centrais
total_vendas = df_vendas[coluna_alvo].sum()
media_valor_vendas = df_vendas[coluna_alvo].mean()
venda_minima = df_vendas[coluna_alvo].min()
venda_maxima = df_vendas[coluna_alvo].max()

# Medidas de Posição
q1 = np.percentile(df_vendas[coluna_alvo], 25)
# q2 = Mediana
q2 = np.percentile(df_vendas[coluna_alvo], 50)
q3 = np.percentile(df_vendas[coluna_alvo], 75)

# avaliar a 'confiabilidade' da média
delta_media_mediana = media_valor_vendas - q2
distancia_percentual = media_valor_vendas/q2
# Caso 1. Distancia <= 10% (0.9 ~ 1.1)
# R = Média é altamente confiavel
# Caso 2. Distancia entre 10% e 25% 
# (0.75~0.9 / 1.10~1.25)
# R = Média sofre influencia moderada de extremos
# Caso 3. Distancia > 25% (< 0.75 / > 1.25)
# R = NÃO confie na média, ela é distorcida 
# pelos extremos


# Assimetria (Skewness)
assimetria = df_vendas[coluna_alvo].skew()

# Caso 1. Assimetria entre -0.5 e 0.5
# R = Dados Equilibrados
# Caso 2. Assimetria > 0.5 (Positiva)
# R = Valores altos são raros, porém são tão
# grandes que distorcem o calculo
# Caso 3. Assimetria < - 0.5 (Negativa)
# R = Menos valores distorcem o calculo para baixo


print('\n--- Resumo Executivo de Vendas ---')
print(f'1. Volume Total (Soma das Vendas): \
      $ {total_vendas:,.2f}')
# Representa o tamanho total da nossa operação no periodo
print(f'2. Gasto Médio: $ {media_valor_vendas:,.2f}')
# Valor esperado que um cliente gaste em média conosco
print(f'3. Maior Venda: $ {venda_maxima:,.2f}')
# Nosso recorde. Investigar o perfil do cliente
print(f'4. Menor Venda: $ {venda_minima:,.2f}')
# Menor valor registrado. Investigar se há anomalias ou fraude


print('--- Relatorio Estatísticos de Negócio ---')

print(f'A média de vendas é \
      $ {media_valor_vendas:,.2f}')
print(f'A mediana (valor central) das vendas é \
      $ {q2:,.2f}')
print(f'O Delta (Diferença Financeira) entre \
      elas é: $ {delta_media_mediana:,.2f}')

print('\n--- Analise Comportamental ---\n')
print(f'Distância Relativa entre elas: \
      {distancia_percentual:.2f}')
print(f'Grau de Assimetria (Skewness): \
      {assimetria:.4f}')


print('--- Relatorio Estatísticos de Negócio ---')

print(f'A média de vendas é \
      $ {media_valor_vendas:,.2f}')
print(f'A mediana (valor central) das vendas é \
      $ {q2:,.2f}')
print(f'O Delta (Diferença Financeira) entre \
      elas é: $ {delta_media_mediana:,.2f}')

print('\n--- Analise Comportamental ---\n')
print(f'Distância Relativa entre elas: \
      {distancia_percentual:.2f}')


if abs(distancia_percentual-1) < 0.10:
      print(f'INFERÊNCIA: Baixa Dispersão. \
            A média é confiável para representar a coluna.')

elif abs(distancia_percentual-1) < 0.25:
      print(f'INFERÊNCIA: Dispersão Moderada. \
            Fique atento aos extremos, média começa a mentir.')
      
else:
      print(f'INFERÊNCIA: Alta Dispersão. \
            A média NÃO é confiável, foque na mediana.')

print(f'Grau de Assimetria (Skewness): \
      {assimetria:.4f}')

if assimetria > 0.5:
    print(f'INFERÊNCIA (Assimetria Positiva): \
            Nossas vendas tem uma cauda longa para a direita.\
            Os grandes clientes são minoria, todavia eles \
            faturam valores expressivos \
            puxando a venda média para cima')
elif assimetria < -0.5:
    print(f'INFERÊNCIA (Assimetria Negativa): \
            Nossa vendas tem uma cauda longa para a esquerda.\
            O valor médio está sendo puxado para baixo por um \
            grande volume de vendas baratas, \
            talvez pela liquidação')
else:
    print(f'INFERÊNCIA (Simétrica): Distribuição Equilibrada.\
          Média e mediana estão bem próximas.')




# Navegação e Filtros Avançados

# iloc -> pega 'n' linhas -> indice
amostra = df_vendas.iloc[0:10]
print(amostra)


# loc -> usa o nome da coluna e filtra com base em algo

# Quem são os melhores clientes?
clientes_vip = df_vendas.loc[df_vendas['total_sales'] > q3]
print(clientes_vip.head())

clientes_vip2 = df_vendas.loc[df_vendas['total_sales'] > q3,
    ['order_id', 'customer_name', 'category', 'total_sales']]
print(clientes_vip2.head())

# query (consulta)

# O gerente quer saber quais pedidos da categoria Eletronico
# ficaram acima da média geral
filtro = \
f"category == 'Electronics' and total_sales > {media_valor_vendas}"
eletronicos = df_vendas.query(filtro)
print(eletronicos.head())