def create_enriched(df_bancos_trusted, df_reclamacoes_trusted, message_id:str):
    df_merged = df_bancos_trusted.merge(df_reclamacoes_trusted, on=["cnpj", "nome"], how="inner")
    df_merged.to_parquet(f"s3://atividade8/messages/enriched/{message_id}_enriched.parquet")
