import sqlite3
import os
from pylatex import Document, Section, Subsection, Command
import tkinter as tk

class MagiasApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Magias App")
        self.geometry("400x200")

        self.frame = tk.Frame(self)
        self.frame.grid()

        self.welcome_label = tk.Label(self.frame, text="Bem-vindo ao Magias App!")
        self.welcome_label.grid(row=0, column=0, padx=10, pady=10)

        self.add_magia_button = tk.Button(self.frame, text="Adicionar nova magia", command=self.add_magia_button_click)
        self.add_magia_button.grid(row=1, column=0, padx=10, pady=10)

        self.view_magias_button = tk.Button(self.frame, text="Visualizar todas as magias", command=self.view_magias_button_click)
        self.view_magias_button.grid(row=2, column=0, padx=10, pady=10)

        # Conecta ao banco de dados
        self.conn = sqlite3.connect('magias.db')

        # Cria a tabela "magias" se ela ainda não existir
        self.conn.execute('''CREATE TABLE IF NOT EXISTS magias
                            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                             nome TEXT NOT NULL,
                             elemento TEXT NOT NULL,
                             custo TEXT NOT NULL,
                             tempo TEXT NOT NULL,
                             alcance TEXT NOT NULL,
                             alvo TEXT NOT NULL,
                             duracao TEXT NOT NULL,
                             resistencia TEXT NOT NULL,
                             melhoria TEXT NOT NULL,
                             descricao TEXT NOT NULL);''')

        # cria cursor
        self.cursor = self.conn.cursor()

    def add_magia_button_click(self):
        # solicita ao usuário o nome e a descrição da magia
        nome = input("Digite o nome da magia: ")
        elemento = input("Digite o elemento da magia: ")
        custo = input("Digite o custo da magia: ")
        tempo = input("Digite o tempo de conjuração da magia: ")
        alcance = input("Digite o alcance da magia: ")
        alvo = input("Digite o alvo da magia: ")
        duracao = input("Digite a duração da magia: ")
        resistencia = input("Digite a resistência da magia: ")
        melhoria = input("Digite a melhoria da magia: ")
        descricao = input("Digite a descrição da magia: ")

        # insere a nova magia no banco de dados
        self.cursor.execute('''INSERT INTO magias (nome, elemento, custo, tempo, alcance, alvo, duracao, resistencia, melhoria, descricao)
                           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);''', (nome, elemento, custo, tempo, alcance, alvo, duracao, resistencia, melhoria, descricao))
        self.conn.commit()

        # confirmação de que a magia foi adicionada com sucesso
        print("Magia adicionada com sucesso!")

    def view_magias_button_click(self):
        # obtém todas as magias do banco de dados e exibe na saída padrão
        self.cursor.execute("SELECT * FROM magias")
        magias = self.cursor.fetchall()
        for magia in magias:
            print(f"{magia[0]} - {magia[1]} - {magia[2]} - {magia[3]} - {magia[4]} - {magia[5]} - {magia[6]} - {magia[7]} - {magia[8]} - {magia[9]} - {magia[10]}")

if __name__ == "__main__":
    app = MagiasApp()
    app.mainloop()
