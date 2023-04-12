from trello import TrelloClient
from dotenv import load_dotenv
import re
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

def grimorioTotal():
    # Obtenha todas as listas do quadro
    lists = board.all_lists()

    # Conecte-se ao banco de dados SQLite
    conn = sqlite3.connect('magias.db')
    cursor = conn.cursor()

    # Para cada lista, obtenha todos os cartões e insira suas informações na tabela
    for lista in lists:
        cards = lista.list_cards()
        for card in cards:
            # Use o nome do cartão como valor para a coluna 'nome'
            nome = card.name

            # Divida a descrição em linhas e filtre as palavras "fora" e "dentro"
            description_lines = [re.sub('<[^<]+?>', '', line.strip().replace("Elemento:", "").replace("Custo:", "").replace("Tempo de Execução:", "").replace("Alcance:", "").replace("Alvo:", "").replace("Duração:", "").replace("Teste de Resistência:", "").replace("Melhoria:", "").replace("Descrição:", "")) for line in card.desc.splitlines() if line.strip()]
            description_lines = [re.sub(r'\*\*([^\*]+)\*\*', r'\1', line).strip() for line in description_lines]
            
            # Crie uma tupla com os valores para cada coluna, substituindo None por ""
            values = tuple(val if val is not None else "" for val in [nome] + description_lines) + ("",) * (9 - len(description_lines))

            # Ajuste a tupla para ter 10 valores
            values = values[:10]

            # Insira a tupla na tabela
            cursor.execute("INSERT INTO magias (nome, elemento, custo, tempo, alcance, alvo, duracao, resistencia, melhoria, descricao) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", values)

    # Salve as alterações no banco de dados
    conn.commit()

    # Feche a conexão com o banco de dados
    conn.close()