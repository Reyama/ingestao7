import json
import pandas as pd
import boto3
from read_reclamacoes import read_parquet
import base64


def lambda_handler(event, context):
     # TODO implement
    parquet = read_parquet()
    
    base = base64.b64encode(parquet).decode('utf-8')
    sqs = boto3.client('sqs')
    sqs.send_message(
     QueueUrl = "https://sqs.us-east-1.amazonaws.com/393862075767/atividade7",
     MessageBody = base
    )
    
    return {
     'statusCode': 200,
     #"message": json.dumps(base) 
    }
    
