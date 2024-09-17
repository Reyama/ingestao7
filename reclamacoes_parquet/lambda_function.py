import json
import boto3
import pandas as pd

def lambda_handler(event, context):

    create_parquet()
    return {
        'statusCode': 200,
    }

def create_parquet():
    reclamacoes_dtypes = {
        "Ano": int,
        "Trimestre": str,
        "Categoria": str,
        "Tipo": str,
        "CNPJ IF": str,
        "Instituição financeira": str,
        "Índice": str,
        "Quantidade de reclamações reguladas procedentes": int,
        "Quantidade de reclamações reguladas - outras": int,
        "Quantidade de reclamações não reguladas": int,
        "Quantidade total de reclamações": int,
        "Quantidade total de clientes – CCS e SCR": int,
        "Quantidade de clientes – CCS": int,
        "Quantidade de clientes – SCR": int
    }
    s3_client = boto3.client("s3")
    fileList = s3_client.list_objects_v2(Bucket="atividade8", Prefix="raw/reclamacoes/")

    reclamacoes_list = []

    if 'Contents' in fileList:
        for obj in fileList['Contents']:
            filename = obj['Key']
            if ".csv" in filename:
                try:
                    df = pd.read_csv(f's3://atividade8/{filename}', sep=';', encoding='iso-8859-1', dtype=reclamacoes_dtypes)

                    reclamacoes_list.append(df)
                except Exception as e:
                    print(e)
    
    if reclamacoes_list:
        reclamacoes_df = pd.concat(reclamacoes_list)
        reclamacoes_df = reclamacoes_df.drop('Unnamed: 14', axis=1)
        reclamacoes_df['Quantidade total de clientes \x96 CCS e SCR'] = reclamacoes_df['Quantidade total de clientes \x96 CCS e SCR'].astype(str)
        reclamacoes_df.to_parquet("s3://atividade8/raw/reclamacoes/reclamacoes.parquet")
