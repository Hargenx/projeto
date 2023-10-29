import tkinter as tk
from tkinter import ttk
from controller import JogoController


class JogoView:
    def __init__(self, root):
        self.root = root
        self.root.title("CRUD de Jogos")

        # Widgets
        self.nome_label = ttk.Label(root, text="Nome:")
        self.genero_label = ttk.Label(root, text="Gênero:")
        self.plataforma_label = ttk.Label(root, text="Plataforma:")
        self.lancamento_label = ttk.Label(root, text="Ano de Lançamento:")

        self.nome_entry = ttk.Entry(root)
        self.genero_entry = ttk.Entry(root)
        self.plataforma_entry = ttk.Entry(root)
        self.lancamento_entry = ttk.Entry(root)

        self.salvar_button = ttk.Button(root, text="Salvar", command=self.salvar_jogo)
        self.atualizar_button = ttk.Button(
            root, text="Atualizar", command=self.atualizar_jogo
        )
        self.deletar_button = ttk.Button(
            root, text="Deletar", command=self.deletar_jogo
        )

        self.jogos_listbox = tk.Listbox(root)
        self.jogos_listbox.bind("<<ListboxSelect>>", self.selecionar_jogo)

        # Posicionamento dos widgets
        self.nome_label.grid(row=0, column=0)
        self.genero_label.grid(row=1, column=0)
        self.plataforma_label.grid(row=2, column=0)
        self.lancamento_label.grid(row=3, column=0)

        self.nome_entry.grid(row=0, column=1)
        self.genero_entry.grid(row=1, column=1)
        self.plataforma_entry.grid(row=2, column=1)
        self.lancamento_entry.grid(row=3, column=1)

        self.salvar_button.grid(row=4, column=0)
        self.atualizar_button.grid(row=4, column=1)
        self.deletar_button.grid(row=4, column=2)

        self.jogos_listbox.grid(row=5, column=0, columnspan=3)

        # Inicializar o controlador e a lista de jogos
        self.controller = JogoController()
        self.atualizar_lista_jogos()

    def salvar_jogo(self):
        nome = self.nome_entry.get()
        genero = self.genero_entry.get()
        plataforma = self.plataforma_entry.get()
        lancamento = int(self.lancamento_entry.get())
        self.controller.criar_jogo(nome, genero, plataforma, lancamento)
        self.atualizar_lista_jogos()
        self.limpar_campos()

    def atualizar_lista_jogos(self):
        self.jogos_listbox.delete(0, tk.END)
        jogos = self.controller.listar_jogos()
        for jogo in jogos:
            self.jogos_listbox.insert(tk.END, f"{jogo.id}: {jogo.nome}")

    def selecionar_jogo(self, event):
        selected_index = self.jogos_listbox.curselection()
        if selected_index:
            jogo_id = int(self.jogos_listbox.get(selected_index[0]).split(':')[0])
            jogos = self.controller.listar_jogos()
            
            if 0 <= jogo_id - 1 < len(jogos):
                jogo = jogos[jogo_id - 1]
                self.preencher_campos(jogo)
            else:
                self.limpar_campos()
        else:
            self.limpar_campos()


    def preencher_campos(self, jogo):
        self.nome_entry.delete(0, tk.END)
        self.genero_entry.delete(0, tk.END)
        self.plataforma_entry.delete(0, tk.END)
        self.lancamento_entry.delete(0, tk.END)

        self.nome_entry.insert(0, jogo.nome)
        self.genero_entry.insert(0, jogo.genero)
        self.plataforma_entry.insert(0, jogo.plataforma)
        self.lancamento_entry.insert(0, jogo.lancamento)

    def atualizar_jogo(self):
        selected_index = self.jogos_listbox.curselection()
        if selected_index:
            jogo_id = int(self.jogos_listbox.get(selected_index[0]).split(":")[0])
            jogo = self.controller.listar_jogos()[jogo_id - 1]

            jogo.nome = self.nome_entry.get()
            jogo.genero = self.genero_entry.get()
            jogo.plataforma = self.plataforma_entry.get()
            jogo.lancamento = int(self.lancamento_entry.get())

            self.controller.atualizar_jogo(jogo)
            self.atualizar_lista_jogos()
            self.limpar_campos()

    def deletar_jogo(self):
        selected_index = self.jogos_listbox.curselection()
        if selected_index:
            jogo_id = int(self.jogos_listbox.get(selected_index[0]).split(":")[0])
            self.controller.deletar_jogo(jogo_id)
            self.atualizar_lista_jogos()
            self.limpar_campos()

    def limpar_campos(self):
        self.nome_entry.delete(0, tk.END)
        self.genero_entry.delete(0, tk.END)
        self.plataforma_entry.delete(0, tk.END)
        self.lancamento_entry.delete(0, tk.END)
