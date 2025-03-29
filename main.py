import os
from dotenv import load_dotenv
from db.create_connection import create_connection
from db.create_tables import create_tables
from db.insert_company import insert_company
from db.insert_user import insert_user
from fetch_users.fetch_users import fetch_users


def main():
    # Configurações de conexão com o MySQL (conforme definido no docker-compose)
    load_dotenv()
    
    db_config = {
        'host': os.getenv('DB_HOST', 'localhost'),
        'port': int(os.getenv('DB_PORT', 3306)),
        'user': os.getenv('DB_USER', 'user'),
        'password': os.getenv('DB_PASSWORD', 'root'),
        'database': os.getenv('DB_NAME', 'test_db'),
    }
    
    conn = create_connection(**db_config)
    if conn is None:
        print("Falha na conexão com o banco de dados.")
        return


    # Busca os usuários na API
    users = fetch_users()
    if users is None:
        print("Nenhum usuário encontrado.")
        return

    # Processa cada usuário: insere a empresa e depois o usuário com os dados de endereço
    for user in users:
        company = user.get("company")
        if company:
            company_id = insert_company(conn, company)
        else:
            company_id = None
        insert_user(conn, user, company_id)
        print(f"Usuário {user.get('name')} inserido com sucesso.")

    conn.close()

if __name__ == "__main__":
    main()
