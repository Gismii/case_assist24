def insert_user(conn, user, company_id):
    """
    Insere um registro na tabela user utilizando o company_id recebido.
    Se o usuário já existir (id duplicado), atualiza os dados.
    """
    cursor = conn.cursor()
    # Extraindo os dados de endereço e geo do usuário
    address = user.get("address", {})
    geo = address.get("geo", {}) if address else {}

    query_insert = """
    INSERT INTO user (id, name, username, email, phone, website, street, suite, city, zipcode, lat, lng, company_id)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
        name = VALUES(name),
        username = VALUES(username),
        email = VALUES(email),
        phone = VALUES(phone),
        website = VALUES(website),
        street = VALUES(street),
        suite = VALUES(suite),
        city = VALUES(city),
        zipcode = VALUES(zipcode),
        lat = VALUES(lat),
        lng = VALUES(lng),
        company_id = VALUES(company_id)
    """
    values = (
        user.get("id"),
        user.get("name"),
        user.get("username"),
        user.get("email"),
        user.get("phone"),
        user.get("website"),
        address.get("street"),
        address.get("suite"),
        address.get("city"),
        address.get("zipcode"),
        geo.get("lat"),
        geo.get("lng"),
        company_id
    )
    cursor.execute(query_insert, values)
    conn.commit()
    cursor.close()