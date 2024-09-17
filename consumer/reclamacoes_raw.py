import base64
import io
import pandas as pd

def base64_to_parquet(base64S:str):
    parquet_base64 = base64.b64decode(base64S)
    
    buffer = io.BytesIO(parquet_base64)
    df = pd.read_parquet(buffer)
    return df
    

def save_parquet(df, name):
    df.to_parquet(f"s3://atividade8/messages/raw/{name}.parquet")

def handle_event(message):
    df = base64_to_parquet(message['body'])
    save_parquet(df, message["messageId"])
    return df


