from trello import TrelloClient
from dotenv import load_dotenv
import os
import sqlite3

# carrega as variáveis de ambiente do arquivo .env
load_dotenv('turhrock.env')

# Crie um cliente do Trello
client = TrelloClient(
    api_key=os.getenv("apiKey"),
    api_secret=os.getenv("apiSecret"),
)

# Obtenha o quadro desejado
id_acess = os.getenv("idQuadro")
board = client.get_board(id_acess)

# Obtenha todas as listas do quadro
lists = board.all_lists()

# Conecte-se ao banco de dados SQLite
conn = sqlite3.connect('magias.db')
cursor = conn.cursor()

# Para cada lista, obtenha todos os cartões e insira suas informações na tabela
for lista in lists:
    cards = lista.list_cards()
    for card in cards:
        # Divida a descrição em linhas
        description_lines = card.desc.splitlines() if card.desc else []

        # Crie uma tupla com os valores para cada coluna
        values = (card.name,) + tuple(description_lines) + (None,) * (9 - len(description_lines))

        # Remova o valor extra da tupla
        values = values[:10]

        # Insira a tupla na tabela
        cursor.execute("INSERT INTO magias (nome, elemento, custo, tempo, alcance, alvo, duracao, resistencia, melhoria, descricao) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", values)

# Salve as alterações no banco de dados
conn.commit()

# Feche a conexão com o banco de dados
conn.close()
