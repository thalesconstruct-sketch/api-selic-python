# API de Consulta da Taxa Selic

API REST desenvolvida em Python com FastAPI para consulta de dados históricos da taxa Selic, armazenados em PostgreSQL.

O projeto utiliza Docker para facilitar a configuração e execução dos serviços e possui integração com a API do Banco Central do Brasil para obtenção dos dados da Selic.

## Tecnologias

* Python
* FastAPI
* PostgreSQL
* Docker
* Docker Compose
* psycopg2
* Pydantic
* Git
* GitHub
* API do Banco Central do Brasil

## Funcionalidades

* Consulta da taxa Selic
* Consulta de dados históricos
* Consulta da Selic por data
* Suporte a diferentes formatos de data
* Paginação dos resultados
* Cadastro de usuários
* Validação de e-mail
* Tratamento de e-mails duplicados
* Documentação automática com Swagger/OpenAPI
* Banco de dados PostgreSQL
* Ambiente containerizado com Docker

## Estrutura do projeto

```text
projeto-docker/
│
├── app/
│   └── main.py
│
├── .env
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── README.md
└── requirements.txt
```

## Como executar

### 1. Clonar o repositório

```bash
git clone https://github.com/thalesconstruct-sketch/api-selic-python.git
```

### 2. Entrar no projeto

```bash
cd api-selic-python
```

### 3. Subir os containers

```bash
docker compose up -d --build
```

A aplicação será executada na porta:

```text
http://localhost:8000
```

## Documentação da API

A API possui documentação automática através do Swagger.

Acesse:

```text
http://localhost:8000/docs
```

Também é possível acessar o schema OpenAPI:

```text
http://localhost:8000/openapi.json
```

## Endpoints

### GET /

Verifica se a API está funcionando.

Exemplo:

```http
GET /
```

Resposta:

```json
{
  "mensagem": "Olá! Minha API está funcionando!"
}
```

---

### GET /ola

Endpoint simples de teste.

Exemplo:

```http
GET /ola
```

Resposta:

```json
{
  "mensagem": "Olá!"
}
```

---

### GET /selic

Lista os registros históricos da taxa Selic.

Exemplo:

```http
GET /selic
```

Resposta:

```json
{
  "pagina": 1,
  "limite": 10,
  "total": 6683,
  "total_paginas": 669,
  "dados": [
    {
      "data": "2026-08-11",
      "valor": 13.9
    },
    {
      "data": "2026-08-10",
      "valor": 13.9
    }
  ]
}
```

### Paginação

É possível controlar a página e a quantidade de registros retornados.

Exemplo:

```http
GET /selic?pagina=2&limite=20
```

Parâmetros:

| Parâmetro | Tipo    | Descrição                          | Valor padrão |
| --------- | ------- | ---------------------------------- | ------------ |
| pagina    | integer | Número da página                   | 1            |
| limite    | integer | Quantidade de registros por página | 10           |
| data      | string  | Data específica para consulta      | opcional     |

O limite máximo permitido é de 100 registros por página.

---

### GET /selic?data=

Permite consultar a taxa Selic utilizando uma data específica.

A API aceita os formatos:

```text
DD/MM/YYYY
```

ou:

```text
YYYY-MM-DD
```

#### Formato brasileiro

```http
GET /selic?data=11/08/2026
```

Resposta:

```json
{
  "data": "2026-08-11",
  "valor": 13.9
}
```

#### Formato ISO

```http
GET /selic?data=2026-08-11
```

Resposta:

```json
{
  "data": "2026-08-11",
  "valor": 13.9
}
```

Caso a data não exista:

```json
{
  "erro": "Data não encontrada"
}
```

---

### GET /selic/{data}

Também é possível consultar uma data diretamente pela URL.

Exemplo:

```http
GET /selic/2026-08-11
```

Resposta:

```json
{
  "data": "2026-08-11",
  "valor": 13.9
}
```

> Para datas no formato `DD/MM/YYYY`, recomenda-se utilizar o parâmetro `?data=`, pois o caractere `/` possui função especial na estrutura da URL.

---

### POST /usuarios

Cria um novo usuário no banco de dados.

Exemplo:

```http
POST /usuarios
```

Body:

```json
{
  "nome": "Thales",
  "email": "thales@email.com"
}
```

Resposta:

```json
{
  "id": 1,
  "nome": "Thales",
  "email": "thales@email.com"
}
```

O campo `email` é validado utilizando Pydantic.

Caso o e-mail já esteja cadastrado, a API retorna:

```text
409 Conflict
```

Com a mensagem:

```json
{
  "detail": "Email já cadastrado"
}
```

## Banco de dados

O projeto utiliza PostgreSQL para armazenamento dos dados.

A tabela principal utilizada para consulta da Selic possui informações como:

```text
data
valor
```

Os dados são organizados por data em ordem decrescente nas consultas paginadas.

## Docker

O projeto utiliza Docker Compose para executar os serviços da aplicação.

Serviços principais:

```text
API
PostgreSQL
```

Para verificar os containers em execução:

```bash
docker ps
```

Para parar os containers:

```bash
docker compose down
```

Para iniciar novamente:

```bash
docker compose up -d
```

Para reconstruir a aplicação após alterações no código:

```bash
docker compose up -d --build
```

## Variáveis de ambiente

As configurações de conexão com o PostgreSQL são armazenadas através de variáveis de ambiente.

Exemplo:

```env
POSTGRES_HOST=banco
POSTGRES_DB=nome_do_banco
POSTGRES_USER=usuario
POSTGRES_PASSWORD=senha
POSTGRES_PORT=5432
```

As credenciais reais não devem ser versionadas no GitHub.

## Testando a API

Exemplo utilizando cURL:

### Consultar Selic

```bash
curl http://localhost:8000/selic
```

### Consultar por data

```bash
curl "http://localhost:8000/selic?data=11/08/2026"
```

### Consultar utilizando formato ISO

```bash
curl "http://localhost:8000/selic?data=2026-08-11"
```

### Consultar diretamente pela rota

```bash
curl http://localhost:8000/selic/2026-08-11
```

## Git e GitHub

O projeto utiliza Git para controle de versão e está hospedado no GitHub.

Repositório:

[https://github.com/thalesconstruct-sketch/api-selic-python](https://github.com/thalesconstruct-sketch/api-selic-python)

Principais conceitos utilizados:

* Git
* Branch `main`
* Commits
* GitHub
* Git push
* Git pull
* Versionamento de código

## Objetivo do projeto

Este projeto foi desenvolvido com o objetivo de praticar e demonstrar conhecimentos em:

* Desenvolvimento de APIs REST
* Python
* FastAPI
* Bancos de dados relacionais
* PostgreSQL
* Docker
* Integração com APIs externas
* Tratamento e validação de dados
* Paginação
* Git e GitHub
* Documentação de APIs

O projeto também serve como base para estudos de desenvolvimento backend e práticas relacionadas a DevOps.
