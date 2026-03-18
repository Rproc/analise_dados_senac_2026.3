import polars as pl

arquivo_info = 'Music Info.csv'
arquivo_user = 'User Listening History.csv'

try:
    df_musica = pl.read_csv(arquivo_info)
    df_execucao = pl.read_csv(arquivo_user)

    # print(df_info.glimpse())
    # print(df_user.glimpse())
    df_execucao_agrupado = df_execucao.group_by('track_id').agg(
        pl.col('playcount').sum().alias('plays')
    )
    print(df_execucao_agrupado.head())

    df_merge = df_musica.join(
        df_execucao_agrupado,
        left_on='track_id',
        right_on='track_id',
        how='left'
    )
    # print(df_merge.head())
    print(df_merge.columns)

except Exception as e:
    print(f'Erro ao ler arquivos: {e}')

# Top 10 de músicas mais tocadas

top10_musicas = df_merge.group_by(['name', 'artist']).agg(
    pl.col('plays').sum()
).sort(by='plays', descending=True)
top10_musicas.head(10)

# Quantas musicas não foram tocadas?
df_sem_execucao = df_merge.group_by('plays').agg(
    pl.len()
).sort(by='plays', descending=False)
print(df_sem_execucao.head(1))

sem_execucao = df_merge.filter(
    pl.col('plays').is_null()
).height
print(sem_execucao)

# Qual genero tem mais musicas não tocadas?
