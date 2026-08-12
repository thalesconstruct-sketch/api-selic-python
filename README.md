# API de Consulta da Taxa Selic

API desenvolvida em Python com FastAPI para disponibilizar dados históricos da taxa Selic, armazenados em um banco de dados PostgreSQL.

O projeto possui um processo de atualização dos dados utilizando a API do Banco Central do Brasil (BCB), permitindo consultar os valores da taxa Selic através de endpoints HTTP.

## 🚀 Tecnologias

* Python
* FastAPI
* PostgreSQL
* Docker
* Docker Compose
* Requests
* Pydantic
* Git
* GitHub
* API do Banco Central do Brasil (BCB)

## 📌 Objetivo do Projeto

O objetivo deste projeto é desenvolver uma API capaz de:

* Consultar dados históricos da taxa Selic;
* Armazenar os dados em um banco PostgreSQL;
* Buscar dados atualizados diretamente da API do Banco Central;
* Disponibilizar os dados através de endpoints REST;
* Utilizar Docker para facilitar a configuração do ambiente;
* Praticar conceitos de desenvolvimento de APIs, bancos de dados e integração entre sistemas.

## 🏗️ Arquitetura

O projeto possui a seguinte estrutura:

```text
                    ┌─────────────────────┐
                    │   Banco Central     │
                    │       do Brasil     │
                    └──────────┬──────────┘
                               │
                               │ API
                               ▼
                    ┌─────────────────────┐
                    │       Python        │
                    │      FastAPI        │
                    └──────────┬──────────┘
                               │
                               │ SQL
                               ▼
                    ┌─────────────────────┐
                    │     PostgreSQL      │
                    │      Database       │
                    └─────────────────────┘
```

A aplicação utiliza o FastAPI como camada responsável por receber as requisições e disponibilizar os dados.

O PostgreSQL é utilizado para armazenar os registros da taxa Selic.

A API do Banco Central é utilizada como fonte externa para obtenção dos dados.

## 📂 Estrutura do Projeto

```text
projeto-docker/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   └── schemas.py
│
├── scripts/
│   └── atualizar_selic.py
│
├── .env
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

### Principais arquivos

#### `app/main.py`

Arquivo principal da aplicação FastAPI.

É responsável por inicializar a API e disponibilizar os endpoints.

#### `app/database.py`

Responsável pela configuração da conexão com o PostgreSQL.

#### `app/models.py`

Contém os modelos utilizados para representar as tabelas do banco de dados.

#### `app/schemas.py`

Define os schemas utilizados pela API para validação e estruturação dos dados.

#### `scripts/atualizar_selic.py`

Script responsável por consultar os dados da API do Banco Central e atualizar o banco de dados.

#### `Dockerfile`

Define a imagem utilizada para executar a aplicação Python.

#### `docker-compose.yml`

Responsável por orquestrar os containers da aplicação e do PostgreSQL.

#### `.env`

Arquivo utilizado para armazenar configurações e variáveis de ambiente, como credenciais do banco de dados.

> O arquivo `.env` não deve ser enviado para o GitHub.

## 🐘 Banco de Dados

O projeto utiliza PostgreSQL para armazenamento dos dados.

A tabela principal possui informações relacionadas à taxa Selic.

Exemplo de estrutura:

```sql
CREATE TABLE selic (
    id SERIAL PRIMARY KEY,
    data DATE NOT NULL,
    valor NUMERIC(10, 2) NOT NULL
);
```

### Exemplo de registro

```text
id | data       | valor
---+------------+------
1  | 2026-01-01 | 15.00
```

## 🔌 API

A aplicação é desenvolvida utilizando o FastAPI.

Após iniciar o projeto, a API pode ser acessada localmente através de:

```text
http://localhost:8000
```

### Documentação automática

O FastAPI disponibiliza uma interface interativa para testar os endpoints.

Swagger:

```text
http://localhost:8000/docs
```

Redoc:

```text
http://localhost:8000/redoc
```

## 📡 Endpoints

### Verificar funcionamento da API

```http
GET /
```

Exemplo de resposta:

```json
{
  "mensagem": "API da Taxa Selic funcionando!"
}
```

### Consultar dados da Selic

```http
GET /selic
```

Retorna os registros disponíveis no banco de dados.

Exemplo:

```json
[
  {
    "id": 1,
    "data": "2026-01-01",
    "valor": 15.00
  }
]
```

## 🔄 Atualização dos Dados

O projeto possui um processo de atualização que consulta a API do Banco Central do Brasil.

O fluxo funciona da seguinte maneira:

```text
Banco Central
      │
      ▼
API do BCB
      │
      ▼
Script Python
      │
      ▼
Tratamento dos dados
      │
      ▼
PostgreSQL
      │
      ▼
FastAPI
      │
      ▼
Usuário
```

Dessa forma, os dados externos podem ser coletados e posteriormente disponibilizados pela API desenvolvida no projeto.

## 🐳 Docker

O projeto utiliza Docker para facilitar a configuração do ambiente.

Os principais serviços são:

```text
┌─────────────────────────┐
│       Aplicação         │
│      FastAPI/Python     │
│       Port: 8000        │
└────────────┬────────────┘
             │
             │
┌────────────▼────────────┐
│       PostgreSQL        │
│       Port: 5432        │
└─────────────────────────┘
```

### Subir os containers

Dentro da pasta do projeto:

```bash
docker compose up -d
```

### Verificar os containers

```bash
docker compose ps
```

### Visualizar os logs

```bash
docker compose logs
```

Para visualizar os logs da aplicação:

```bash
docker compose logs app
```

### Parar os containers

```bash
docker compose down
```

## ⚙️ Configuração

Crie um arquivo `.env` na raiz do projeto.

Exemplo:

```env
POSTGRES_DB=minha_api
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

As informações utilizadas devem ser ajustadas de acordo com a configuração do ambiente.

## 📦 Instalação das Dependências

As dependências do projeto estão listadas no arquivo:

```text
requirements.txt
```

Exemplo:

```text
fastapi
uvicorn
psycopg2-binary
requests
python-dotenv
```

Caso esteja executando o projeto fora do Docker, as dependências podem ser instaladas utilizando:

```bash
pip install -r requirements.txt
```

## ▶️ Executando a Aplicação

Com Docker:

```bash
docker compose up -d
```

Depois de iniciar os containers, acesse:

```text
http://localhost:8000
```

Para acessar a documentação:

```text
http://localhost:8000/docs
```

## 🧪 Testando a API

A API pode ser testada diretamente através do Swagger.

Acesse:

```text
http://localhost:8000/docs
```

Depois selecione um endpoint, clique em:

```text
Try it out
```

e execute a requisição.

Também é possível utilizar ferramentas como:

* Postman
* Insomnia
* cURL
* Navegador

## 🔐 Variáveis de Ambiente

As informações sensíveis do projeto devem ser armazenadas através de variáveis de ambiente.

O arquivo `.env` deve estar presente no `.gitignore`.

Exemplo de `.gitignore`:

```text
.env
.venv/
__pycache__/
*.pyc
```

Isso evita que credenciais e arquivos desnecessários sejam enviados para o GitHub.

## 📈 Possíveis Melhorias

O projeto pode ser expandido futuramente com:

* [ ] Endpoint para consultar a Selic por período;
* [ ] Endpoint para consultar um registro específico;
* [ ] Filtros por data;
* [ ] Paginação dos resultados;
* [ ] Melhor tratamento de erros;
* [ ] Testes automatizados;
* [ ] Integração contínua com GitHub Actions;
* [ ] Logs da aplicação;
* [ ] Autenticação da API;
* [ ] Monitoramento;
* [ ] Agendamento automático da atualização dos dados;
* [ ] Deploy em ambiente cloud;
* [ ] Criação de dashboard para visualização dos dados.

## 🎯 Conceitos Praticados

Este projeto foi desenvolvido com foco no aprendizado e aplicação prática de conceitos como:

* Desenvolvimento de APIs REST;
* Python;
* FastAPI;
* PostgreSQL;
* SQL;
* Integração com APIs externas;
* Docker;
* Docker Compose;
* Variáveis de ambiente;
* Git;
* GitHub;
* Estruturação de aplicações;
* Comunicação entre serviços;
* Persistência de dados.

## 💼 Aplicação Profissional

O projeto simula uma situação comum no desenvolvimento de sistemas:

> Uma aplicação precisa consumir dados de uma fonte externa, processar essas informações, armazená-las em um banco de dados e disponibilizá-las através de uma API.

Esse fluxo é encontrado em diversos sistemas corporativos que trabalham com integração entre serviços, APIs e bancos de dados.

## 👨‍💻 Autor

**Thales Lopes Oliveira da Silva**

Estudante de Análise e Desenvolvimento de Sistemas.

Interesses:

* Desenvolvimento de Software
* Backend
* APIs
* Banco de Dados
* Python
* Java
* Cloud
* DevOps

GitHub:

[https://github.com/thalesconstruct-sketch](https://github.com/thalesconstruct-sketch)

## 📄 Licença

Este projeto foi desenvolvido para fins educacionais e de portfólio.
