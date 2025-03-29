def create_tables(conn):
    """
    Cria as tabelas company e user (com os campos de endereço) se elas não existirem.
    """
    create_company_table = """
    CREATE TABLE IF NOT EXISTS company (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        catchPhrase VARCHAR(255),
        bs VARCHAR(255)
    );
    """

    create_user_table = """
    CREATE TABLE IF NOT EXISTS user (
        id INT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        username VARCHAR(255),
        email VARCHAR(255),
        phone VARCHAR(255),
        website VARCHAR(255),
        street VARCHAR(255),
        suite VARCHAR(255),
        city VARCHAR(255),
        zipcode VARCHAR(20),
        lat VARCHAR(20),
        lng VARCHAR(20),
        company_id INT,
        FOREIGN KEY (company_id) REFERENCES company(id)
    );
    """

    cursor = conn.cursor()
    cursor.execute(create_company_table)
    cursor.execute(create_user_table)
    conn.commit()
    cursor.close()
   