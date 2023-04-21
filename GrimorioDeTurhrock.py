from trello import TrelloClient
from dotenv import load_dotenv
import re
import os
import sqlite3

# carrega as variáveis de ambiente do arquivo .env
load_dotenv('/home/ricardo_piero/Documentos/PROJETOS/TURHROCK/Fichas/keys/turhrock.env')


# Crie um cliente do Trello
client = TrelloClient(
    api_key=os.getenv("apiKey"),
    api_secret=os.getenv("apiSecret"),
)

# Obtenha o quadro desejado
id_acess = os.getenv("idQuadro")
board = client.get_board(id_acess)

# adiciona os dados do trello na db
def grimorioTotal():
    magia_inicial = board.get_list('63f2c1f51747292eb0a8d350')
    magia_primeiro = board.get_list('63f2c207bb3985fa7cfb89aa')
    magia_segundo = board.get_list('6414cee970fc506e434c0365')
    magia_terceiro = board.get_list('6414d071ac7895ccdd803322')

    conn = sqlite3.connect('bin/magias.db')
    cursor = conn.cursor()

    for lista in [magia_inicial, magia_primeiro, magia_segundo, magia_terceiro]:
        cards = lista.list_cards()
        for card in cards:
            nome = card.name

            description_lines = [re.sub('<[^<]+?>', '', line.strip().replace("Elemento:", "").replace("Custo:", "").replace("Tempo de Execução:", "").replace("Alcance:", "").replace("Alvo:", "").replace("Duração:", "").replace("Teste de Resistência:", "").replace("Melhoria:", "").replace("Descrição:", "")) for line in card.desc.splitlines() if line.strip()]
            description_lines = [re.sub(r'\*\*([^\*]+)\*\*', r'\1', line).strip() for line in description_lines]
            
            values = tuple(val if val is not None else "" for val in [nome] + description_lines) + ("",) * (9 - len(description_lines))

            values = values[:10]

            cursor.execute("INSERT INTO magias (nome, elemento, custo, tempo, alcance, alvo, duracao, resistencia, melhoria, descricao) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", values)

    conn.commit()

    conn.close()