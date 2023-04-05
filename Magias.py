import sqlite3
from pylatex import Document, Section, Subsection, Command

# Conecta ao banco de dados
conn = sqlite3.connect('magias.db')

# Cria a tabela "magias" se ela ainda não existir
conn.execute('''CREATE TABLE IF NOT EXISTS magias
                (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                 nome TEXT NOT NULL,
                 descricao TEXT NOT NULL);''')

# cria cursor
cursor = conn.cursor()

# método para adicionar uma nova magia
def add_magia():
    # solicita ao usuário o nome e a descrição da magia
    nome = input("Digite o nome da magia: ")
    descricao = input("Digite a descrição da magia: ")

    # insere a nova magia no banco de dados
    cursor.execute("INSERT INTO magias (nome, descricao) VALUES (?, ?)", (nome, descricao))
    conn.commit()

    print("Magia adicionada com sucesso!")
# método criar documento
def documento(magia, magiaDes):
    texto_Tit = magia
    texto_Des = magiaDes

    # Cria um novo documento
    doc = Document()
    # Adiciona uma seção e uma subseção
    with doc.create(Section(texto_Tit)):
        doc.append(texto_Des)
    # with doc.create(Subsection('Uma subseção')):
    #     doc.append('Mais texto.')

    # Adiciona um comando LaTeX personalizado
    doc.append(Command('vspace', '1cm'))

    # Gera o PDF com o nome "PDFLaTeX.pdf"
    doc.generate_pdf('Magias', clean_tex=False)

# método para visualizar todas as magias
def view_magias():
    cursor.execute("SELECT * FROM magias")
    magias = cursor.fetchall()

    if not magias:
        print("Nenhuma magia encontrada!")
    else:
        for magia in magias:
            print(f"Nome: {magia[1]}")
            print(f"Descrição: {magia[2]}")
            print()

            documento(magia[1], magia[2])


# método para buscar magias por nome
def search_magia():
    nome = input("Digite o nome da magia: ")

    cursor.execute("SELECT * FROM magias WHERE nome LIKE ?", ('%' + nome + '%',))
    magias = cursor.fetchall()

    if not magias:
        print("Nenhuma magia encontrada!")
    else:
        for magia in magias:
            print(f"Nome: {magia[1]}")
            print(f"Descrição: {magia[2]}")
            print()

def limpar_banco_de_dados():
    cursor = conn.cursor()

    cursor.execute("DELETE FROM magias")

    print(f"Magias Destruidas")
    print()

    # Confirma a operação e fecha a conexão com o banco de dados
    conn.commit()

# menu principal
while True:
    print("Selecione uma opção:")
    print("1. Adicionar magia")
    print("2. Visualizar magias")
    print("3. Buscar magias por nome")
    print("4. Sair")

    opcao = input()

    if opcao == '1':
        add_magia()
    elif opcao == '2':
        view_magias()
    elif opcao == '3':
        search_magia()
    elif opcao == '4':
        conn.close()
        break
    elif opcao == '666':
        limpar_banco_de_dados()
    else:
        print("Opção inválida!")
