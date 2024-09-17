from pymysql import connect

def get_connection():
    conn = connect(user='root', password='atividade8', database='atividade8', host='atividade8.cxpksz8athek.us-east-1.rds.amazonaws.com')
    return conn