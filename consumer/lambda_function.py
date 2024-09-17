import json
from reclamacoes_raw import handle_event
from bancos_raw import get_bancos_raw
from bancos_trusted import create_bancos_trusted
from reclamacoes_trusted import create_reclamacoes_trusted
from enrich import create_enriched


def lambda_handler(event, context):
    # TODO implement
    
    for record in event['Records']:
        handle_record(record)

    

    return {
        'statusCode': 200,
        'body': "worked!!"
    }


def handle_record(record):
    df_reclamacoes_raw = handle_event(record)
    df_bancos_raw = get_bancos_raw()
        
    df_bancos_trusted = create_bancos_trusted(df_bancos_raw)
    df_reclamacoes_trusted = create_reclamacoes_trusted(df_reclamacoes_raw)
    create_enriched(df_bancos_trusted, df_reclamacoes_trusted, record['messageId'])
    