import tkinter as tk

class MyGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Minha GUI")
        
        # Criando um menu
        self.menu_bar = tk.Menu(self.master)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Abrir", command=self.open_file)
        self.file_menu.add_command(label="Salvar", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Sair", command=self.master.quit)
        self.menu_bar.add_cascade(label="Arquivo", menu=self.file_menu)
        self.master.config(menu=self.menu_bar)
        
        # Criando uma barra de ferramentas
        self.tool_bar = tk.Frame(self.master)
        self.tool_bar.pack(side="top", fill="x")
        self.open_button = tk.Button(self.tool_bar, text="Abrir", command=self.open_file)
        self.open_button.pack(side="left", padx=2, pady=2)
        self.save_button = tk.Button(self.tool_bar, text="Salvar", command=self.save_file)
        self.save_button.pack(side="left", padx=2, pady=2)
        
        # Criando uma área de texto
        self.text_area = tk.Text(self.master, wrap="word")
        self.text_area.pack(side="top", fill="both", expand=True)
        
        # Criando um botão
        self.quit_button = tk.Button(self.master, text="Sair", command=self.master.quit)
        self.quit_button.pack(side="bottom")
    
    def open_file(self):
        # Implementação para abrir um arquivo
        pass
    
    def save_file(self):
        # Implementação para salvar um arquivo
        pass

root = tk.Tk()
app = MyGUI(root)
root.mainloop()
