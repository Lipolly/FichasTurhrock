import sqlite3
import os
import shutil
from pylatex import Document, Section, Subsection, Command
from init import initGrimorio

# Conecta ao banco de dados
conn = sqlite3.connect('bin/magias.db')

# Cria a tabela "magias" se ela ainda não existir
conn.execute('''CREATE TABLE IF NOT EXISTS magias
                (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                 nome TEXT,
                 elemento TEXT,
                 custo TEXT,
                 tempo TEXT,
                 alcance TEXT,
                 alvo TEXT,
                 duracao TEXT,
                 resistencia TEXT,
                 melhoria TEXT,
                 descricao TEXT);''')

initGrimorio()

# cria cursor
cursor = conn.cursor()

# método para adicionar uma nova magia
def add_magia():
    # solicita ao usuário o nome e a descrição da magia
    nome = input("Digite o nome da magia: ")
    elemento = input("Digite o elemento da magia: ")
    custo = input("Digite o custo da magia: ")
    tempo = input("Digite o tempo de 'cast' da magia: ")
    alcance = input("Digite o alcance maximo da magia: ")
    alvo = input("Digite a quantidade de alvos da magia: ")
    duracao = input("Digite a duracao de efeito da magia: ")
    resistencia = input("Digite qual teste de resistencia da magia: ")
    melhoria = input("Digite a melhoria da magia, junto ao seu aumento de valor: ")
    descricao = input("Digite a descrição da magia: ")

    # insere a nova magia no banco de dados
    cursor.execute("INSERT INTO magias (nome, elemento, custo, tempo, alcance, alvo, duracao, resistencia, melhoria, descricao) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (nome, elemento, custo, tempo, alcance, alvo, duracao, resistencia, melhoria, descricao))
    conn.commit()

    print()
    print("Magia adicionada com sucesso!")
    print()

# método criar documento
def documento():
    cursor.execute("SELECT * FROM magias")
    magias = cursor.fetchall()

    if not magias:
        print("\nNenhuma magia encontrada!")
        grimorio = "Grimorio.pdf"
        if os.path.exists(grimorio):
            resposta = input("\nDeseja destruir o grimorio existente? \n1 -> Sim \n2 -> Não")
            if resposta == "1":
                # exclui o arquivo PDF existente
                os.remove(grimorio)
                print("Grimorio destruido.")
        else: print("Nenhum grimorio encontrado")
    else:
        # Cria um novo documento
        doc = Document()

        for magia in magias:
            texto_Tit = magia[1]
            texto_Ele = magia[2]
            texto_Cus = magia[3]
            texto_Tem = magia[4]
            texto_Alc = magia[5]
            texto_Alv = magia[6]
            texto_Dur = magia[7]
            texto_Res = magia[8]
            texto_Mel = magia[9]
            texto_Des = magia[10]
            # Adiciona uma seção e uma subseção
            with doc.create(Section(texto_Tit)):
                doc.append("Elemento " + texto_Ele + "\n" + "Custo " + texto_Cus + "\n" + "Tempo de Cast " + texto_Tem + "\n" + "Alcance " + texto_Alc + "\n" + "Quantidade de alvos atingidos " + texto_Alv + "\n" + "Duração da magia " + texto_Dur + "\n" + "Teste de resistencia " + texto_Res + "\n" + "Melhoria " + texto_Mel + "\n" + "Descrição " + texto_Des + '\n')
        
        # Gera o arquivo .tex dentro da pasta arquivos
        doc.generate_pdf(os.path.join('bin', 'Grimorio'), clean_tex=False)
        
        # Compila o arquivo .tex para gerar o PDF
        os.chdir('bin')
        os.system('pdflatex Grimorio.tex')
        shutil.move('Grimorio.pdf', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Grimorio.pdf'))

# printar dados
def printMagia(magias):
    if not magias:
        print("Nenhuma magia encontrada!")
        print()
    else:
        for magia in magias:
            print(f"Nome: {magia[1]}")
            print(f"Elemento: {magia[2]}")
            print(f"Custo: {magia[3]} PS")
            print(f"Tempo de Cast: {magia[4]}")
            print(f"Alcance: {magia[5]}")
            print(f"Quantidade de Alvos: {magia[6]}")
            print(f"Duração de Efeito: {magia[7]} turnos")
            print(f"Teste de Resistencia: {magia[8]}")
            print(f"Melhoria: {magia[9]}")
            print(f"Descrição: {magia[10]}")
            print()

# método para visualizar todas as magias
def view_magias():
    cursor.execute("SELECT * FROM magias")
    magias = cursor.fetchall()

    printMagia(magias)


# método para buscar magias por nome
def search_magia():
    nome = input("Digite o nome da magia: ")

    cursor.execute("SELECT * FROM magias WHERE nome LIKE ?", ('%' + nome + '%',))
    magias = cursor.fetchall()

    printMagia(magias)

def limpar_banco_de_dados():
    cursor = conn.cursor()

    cursor.execute("DELETE FROM magias")

    print("Magias Destruidas")
    print()

    # Confirma a operação e fecha a conexão com o banco de dados
    conn.commit()

# menu principal
while True:
    print("Selecione uma opção:")
    print("1. Adicionar uma nova magia")
    print("2. Visualizar todas as magias")
    print("3. Buscar magias por nome")
    print("4. Atualizar Grimorio")
    print("5. Sair")

    opcao = input()

    if opcao == '1':
        add_magia()
    elif opcao == '2':
        view_magias()
    elif opcao == '3':
        search_magia()
    elif opcao == '4':
        documento()
    elif opcao == '5':
        conn.close()
        break
    elif opcao == '666':
        limpar_banco_de_dados()
    else:
        print("Opção inválida!")
