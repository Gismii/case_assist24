def insert_company(conn, company):
    """
    Insere um registro na tabela company e retorna o id.
    Se a empresa já existir (baseado no nome), retorna o id existente.
    """
    cursor = conn.cursor()
    query_select = "SELECT id FROM company WHERE name = %s"
    cursor.execute(query_select, (company.get("name"),))
    result = cursor.fetchone()
    if result:
        company_id = result[0]
    else:
        query_insert = "INSERT INTO company (name, catchPhrase, bs) VALUES (%s, %s, %s)"
        values = (company.get("name"), company.get("catchPhrase"), company.get("bs"))
        cursor.execute(query_insert, values)
        conn.commit()
        company_id = cursor.lastrowid
    cursor.close()
    return company_id