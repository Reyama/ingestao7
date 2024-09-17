def create_bancos_trusted(df_bancos_raw):
    bancos_trusted_df = df_bancos_raw.rename(columns={'Nome': 'nome', 'Segmento': 'segmento', 'CNPJ': 'cnpj'})
    bancos_trusted_df['nome'] = bancos_trusted_df['nome'].str.replace(' - PRUDENCIAL','')
    return bancos_trusted_df