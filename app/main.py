from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel, EmailStr
import psycopg2
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

app = FastAPI()


class UsuarioCreate(BaseModel):
    nome: str
    email: EmailStr


def conectar_banco():
    return psycopg2.connect(
        host=os.getenv("POSTGRES_HOST"),
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        port=os.getenv("POSTGRES_PORT")
    )


@app.get("/")
def home():
    return {"mensagem": "Olá! Minha API está funcionando!"}


@app.get("/ola")
def ola():
    return {"mensagem": "Olá!"}


@app.get("/selic")
def listar_selic(
    pagina: int = Query(1, ge=1),
    limite: int = Query(10, ge=1, le=100)
):
    conn = conectar_banco()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM selic;")
    total = cursor.fetchone()[0]

    offset = (pagina - 1) * limite

    cursor.execute(
        """
        SELECT data, valor
        FROM selic
        ORDER BY data DESC
        LIMIT %s OFFSET %s;
        """,
        (limite, offset)
    )

    registros = cursor.fetchall()

    cursor.close()
    conn.close()

    dados = [
        {
            "data": str(data),
            "valor": float(valor)
        }
        for data, valor in registros
    ]

    total_paginas = (total + limite - 1) // limite

    return {
        "pagina": pagina,
        "limite": limite,
        "total": total,
        "total_paginas": total_paginas,
        "dados": dados
    }


@app.get("/selic/{data}")
def buscar_selic(data: str):

    try:
        if "/" in data:
            data_convertida = datetime.strptime(
                data,
                "%d/%m/%Y"
            ).date()
        else:
            data_convertida = datetime.strptime(
                data,
                "%Y-%m-%d"
            ).date()

    except ValueError:
        raise HTTPException(
            status_code=400,
            detail="Data inválida. Use DD/MM/YYYY ou YYYY-MM-DD"
        )

    conn = conectar_banco()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "SELECT data, valor FROM selic WHERE data = %s;",
            (data_convertida,)
        )

        registro = cursor.fetchone()

    finally:
        cursor.close()
        conn.close()

    if registro is None:
        return {"erro": "Data não encontrada"}

    return {
        "data": str(registro[0]),
        "valor": float(registro[1])
    }


@app.post("/usuarios")
def criar_usuario(usuario: UsuarioCreate):
    conn = conectar_banco()
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO usuarios (nome, email)
            VALUES (%s, %s)
            RETURNING id;
            """,
            (usuario.nome, usuario.email)
        )

        usuario_id = cursor.fetchone()[0]

        conn.commit()

        return {
            "id": usuario_id,
            "nome": usuario.nome,
            "email": usuario.email
        }

    except psycopg2.errors.UniqueViolation:
        conn.rollback()

        raise HTTPException(
            status_code=409,
            detail="Email já cadastrado"
        )

    finally:
        cursor.close()
        conn.close()
