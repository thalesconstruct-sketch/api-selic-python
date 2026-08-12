import csv
import psycopg2
from datetime import datetime

ARQUIVO = "selic.csv"

conn = psycopg2.connect(
    host="localhost",
    database="minha_api",
    user="postgres",
    password="postgres"
)

cursor = conn.cursor()

with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        data = datetime.strptime(
            linha["data"],
            "%d/%m/%Y"
        ).date()

        valor = float(linha["valor"])

        cursor.execute(
            """
            INSERT INTO selic (data, valor)
            VALUES (%s, %s)
            ON CONFLICT (data)
            DO UPDATE SET valor = EXCLUDED.valor
            """,
            (data, valor)
        )

conn.commit()

cursor.close()
conn.close()

print("Dados importados/atualizados com sucesso!")
