import pandas as pd
import boto3
import io


def read_parquet():
    s3_client = boto3.client("s3")
    
    df = pd.read_parquet("s3://atividade8/raw/reclamacoes/reclamacoes.parquet")
    buffer = io.BytesIO()
    df.to_parquet(buffer, index=False)
    return buffer.getvalue()
    
