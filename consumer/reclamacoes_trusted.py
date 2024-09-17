def create_reclamacoes_trusted(df_reclamacoes_raw):
    reclamacoes_trusted_df = df_reclamacoes_raw.rename(columns={
        "Ano": "ano",
        "Trimestre": "trimestre",
        "Categoria": "categoria",
        "Tipo": "tipo",
        "CNPJ IF": "cnpj",
        "Instituição financeira": "nome",
        "Índice": "indice",
        "Quantidade de reclamações reguladas procedentes": "quantidade_de_reclamacoes_reguladas_procedentes",
        "Quantidade de reclamações reguladas - outras": "quantidade_de_reclamacoes_reguladas_outras",
        "Quantidade de reclamações não reguladas": "quantidade_de_reclamacoes_nao_reguladas",
        "Quantidade total de reclamações": "quantidade_total_de_reclamacoes",
        "Quantidade total de clientes – CCS e SCR": "quantidade_total_de_clientes_CCS_SCR",
        "Quantidade de clientes – CCS": "quantidade_de_clientes_CCS",
        "Quantidade de clientes – SCR": "quantidade_de_clientes_SCR"   
    })
    return reclamacoes_trusted_df