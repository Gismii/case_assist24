DROP TABLE IF EXISTS user, company;

CREATE TABLE IF NOT EXISTS company (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    catchPhrase VARCHAR(255),
    bs VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    username VARCHAR(255) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    street VARCHAR(255),
    suite VARCHAR(255),
    city VARCHAR(255),
    zipcode VARCHAR(20),
    lat DECIMAL(10,8),
    lng DECIMAL(11,8),
    phone VARCHAR(50),
    website VARCHAR(100),
    company_id INT,
    FOREIGN KEY (company_id) REFERENCES company(id) ON DELETE SET NULL
);
