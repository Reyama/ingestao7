from database import get_connection
import pandas as pd

def get_bancos_raw():
    conn = get_connection()
    bancos_dtypes = {
        "Segmento": str,
        "CNPJ": str,
        "Nome": str
    }

    df = pd.read_sql_query('''SELECT * FROM bancos_raw''',conn, dtype=bancos_dtypes)
    return df