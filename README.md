# 🚀 Integração API, MySQL e Flyway com Python

[![Python 3.x](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![MySQL 8.0](https://img.shields.io/badge/MySQL-8.0-blue.svg)](https://www.mysql.com/)
[![Docker](https://img.shields.io/badge/Docker-Compose-blue.svg)](https://www.docker.com/)
[![Flyway](https://img.shields.io/badge/Flyway-Migrations-orange.svg)](https://flywaydb.org/)

Projeto que integra uma API pública de usuários com MySQL utilizando migrações controladas pelo Flyway e Docker para orquestração de serviços.

##  Funcionalidades

- Consumo de API REST pública ([JSONPlaceholder](https://jsonplaceholder.typicode.com/users))
- Persistência em banco MySQL com relacionamento user-company
- Versionamento de banco usando Flyway
- Stored procedures para consultas comuns
- Ambiente isolado com Docker Compose

---

## 🛠 Tecnologias

- **Python 3.x** - Lógica de integração
- **MySQL 8.0** - Armazenamento relacional
- **Flyway** - Migrações e versionamento de schema
- **Docker** - Containerização dos serviços
- **python-dotenv** - Gestão de variáveis de ambiente
---

## 📋 Pré-requisitos

- Python 3.x instalado
- Docker e Docker Compose instalados
- Acesso à internet para consumo da API

---

## 🚀 Começando

### 1. Clone o repositório
```bash
git clone git@github.com:Gismii/case_assist24.git
cd case_assist24

## Estrutura do Projeto

.
├── db/
│   ├── create_connection.py    # Gerenciador de conexões MySQL
│   ├── insert_company.py       # Inserção de dados na tabela company
│   └── insert_user.py          # Inserção de dados na tabela user
├── fetch_users/
│   └── fetch_users.py          # Cliente da API de usuários
├── migrations/
│   ├── V1__create_tables.sql       # DDL inicial
│   └── V2__create_procedures.sql   # Stored procedures
├── .env.example                # Template de variáveis
├── docker-compose.yml          # Definição de serviços
├── main.py                     # Script principal
└── requirements.txt            # Dependências Python


---

## Tecnologias Utilizadas

- **Python 3.x:** Linguagem de programação.
- **MySQL 8.0:** Banco de dados relacional.
- **Flyway:** Ferramenta de versionamento e migração de banco de dados.
- **Docker & Docker Compose:** Para levantar os containers do MySQL e do Flyway.
- **Ambiente Virtual Python:** Para isolamento das dependências.

---

## Pré-requisitos

- **Python 3.x** instalado.
- **Docker** e **Docker Compose** instalados.
- **Git** (opcional, para clonar o repositório).

---
```
```bash
## Instalação e Configuração

### 1. Clone o Repositório

git clone git@github.com:Gismii/case_assist24.git
cd case_assist24

### Crie e Ative o Ambiente Virtual

No Linux/Mac:

python3 -m venv venv
source venv/bin/activate

No Windows:

python -m venv venv
venv\Scripts\activate

```

```bash

###Instale as Dependências

pip install -r requirements.txt

```

```bash

### Configure as Variáveis de Ambiente

Crie um arquivo .env na raiz do projeto com o seguinte conteúdo:
DB_HOST=localhost
DB_PORT=3306
DB_USER=user
DB_PASSWORD=root
DB_NAME=test_db

```

```bash

### Levante os Containers com Docker Compose
Execute o comando abaixo para iniciar os serviços do MySQL e do Flyway:

docker-compose up -d

Isso fará com que:

O MySQL seja iniciado com as credenciais definidas.

O Flyway aplique as migrations presentes na pasta migrations, criando as tabelas e as stored procedures.

```

```bash
### Dica: Verifique se os containers estão rodando com:

docker ps

```

```bash

### Execução da Aplicação
Com o ambiente configurado e os containers em execução, execute a aplicação Python para consumir a API e persistir os dados:

python main.py

```

```bash

### Conecte ao MySQL via terminal:

docker exec -it mysql-container mysql -u user -p test_db

```

```bash
### Execute as procedures:

CALL list_all_users();
CALL get_user_by_email('Sincere@april.biz');



```
## 🚨 Solução de Problemas

### Erros de Conexão com MySQL

🔍 **Containers Ativos?**  
Verifique se os serviços estão rodando:
```bash
docker ps