# Integração API, MySQL e Flyway com Python

Este projeto é uma aplicação Python simples cujo objetivo é consumir uma API pública, extrair dados de usuários e persistir essas informações em um banco de dados MySQL. Os dados do usuário são divididos em duas tabelas:
- **user:** Dados do usuário.
- **company:** Dados da empresa associada ao usuário.

A gestão do banco (criação de tabelas, procedures e demais alterações) é realizada com o Flyway. O serviço do MySQL e o Flyway são levantados via Docker Compose. A aplicação Python, por sua vez, é executada localmente em um ambiente virtual.

---

## Estrutura do Projeto

<raiz-do-projeto>/ ├── db/ │ ├── create_connection.py # Módulo para conectar ao MySQL. │ ├── create_tables.py # (Opcional) Módulo para criar tabelas (já substituído pelas migrations). │ ├── insert_company.py # Módulo para inserir dados na tabela company. │ └── insert_user.py # Módulo para inserir dados na tabela user. ├── fetch_users/ │ └── fetch_users.py # Módulo que consome a API e extrai os dados dos usuários. ├── migrations/ │ ├── V1__create_tables.sql # Cria as tabelas (drop, create, constraints). │ └── V2__create_stored_procedures.sql # Cria as stored procedures para busca de usuário por email e listagem. ├── .env # Arquivo de variáveis de ambiente. ├── docker-compose.yml # Configuração do Docker Compose para MySQL e Flyway. ├── requirements.txt # Dependências do Python. └── main.py # Script principal que integra as funcionalidades.


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

## Instalação e Configuração

### 1. Clone o Repositório

```bash
git clone <URL-do-repositório>
cd <nome-do-repositório>

### Crie e Ative o Ambiente Virtual

No Linux/Mac:

python3 -m venv venv
source venv/bin/activate

No Windows:

python -m venv venv
venv\Scripts\activate

###Instale as Dependências


pip install -r requirements.txt

### Configure as Variáveis de Ambiente

Crie um arquivo .env na raiz do projeto com o seguinte conteúdo:
DB_HOST=localhost
DB_PORT=3306
DB_USER=user
DB_PASSWORD=root
DB_NAME=test_db

### Levante os Containers com Docker Compose
Execute o comando abaixo para iniciar os serviços do MySQL e do Flyway:

docker-compose up -d

Isso fará com que:

O MySQL seja iniciado com as credenciais definidas.

O Flyway aplique as migrations presentes na pasta migrations, criando as tabelas e as stored procedures.

### Dica: Verifique se os containers estão rodando com:

docker ps

### Execução da Aplicação
Com o ambiente configurado e os containers em execução, execute a aplicação Python para consumir a API e persistir os dados:

python main.py
