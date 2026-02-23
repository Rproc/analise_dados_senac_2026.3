import pandas as pd

vendas = pd.read_csv('01.amazon_sales_dataset.csv')

print(30*'-')
print(vendas.columns)
print(30*'-')
print(vendas.dtypes)
print(30*'-')
print(vendas.info())
print(30*'-')
print(30*'-')

total_vendas = vendas['total_sales'].sum()
media_valor_vendas = vendas['total_sales'].mean()
venda_minima = vendas['total_sales'].min()
venda_maxima = vendas['total_sales'].max()


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
