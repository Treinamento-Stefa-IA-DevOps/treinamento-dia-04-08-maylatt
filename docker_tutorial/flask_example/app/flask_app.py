from flask import Flask

import os  # vamos pegar nossas credenciais de conexão como variaveis de ambiente!!
import psycopg2  # lib que vai nos conectar ao postgres!

app = Flask(__name__)


@app.route('/')
def hello_world():
    with psycopg2.connect(f"host={os.getenv('DB_HOST')} dbname={os.getenv('DB_NAME')} user={os.getenv('DB_USER')} password={os.getenv('DB_PASS')}") as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM hello_world;")
        rows = cur.fetchall()  # retorna o resultado como tuplas, onde cada item dentro da tupla [e o valor de uma coluna]
        message = ''
        for row in rows:
            message = message + row[1] # seleciona primeiro elemento da tupla retornada
    return message + " Direto de meu belo database!!"