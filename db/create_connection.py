import mysql.connector
from mysql.connector import Error

def create_connection(host, user, password, database, port):
    """
    Cria e retorna uma conexão com o MySQL.
    """
    try:
        conn = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )
        if conn.is_connected():
            print("Conexão bem-sucedida ao MySQL")
            return conn
    except Error as e:
        print("Erro ao conectar ao MySQL:", e)
    return None