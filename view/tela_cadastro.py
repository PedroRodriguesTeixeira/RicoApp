from ctypes import c_ushort
import customtkinter as ctk
import tkinter as tk
from PIL.ImageChops import darker
from view.tela_inicial import COR_FUNDO

class TelaCadastro(ctk.CTkFrame):
    def __init__(self, master, **kwargs):  # Corrigido kwargs
        super().__init__(master, **kwargs)  # Passando kwargs para super

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=0)

        self.frame_cadastro = ctk.CTkFrame(self, width=400)
        self.frame_cadastro.grid(row=0, column=0, padx=20, pady=20, sticky='nsew')

        self.frame_explicativo = ctk.CTkFrame(self, width=400)
        self.frame_explicativo.grid(row=0, column=1, padx=20, pady=20, sticky='nsew')

        self.criar_componentes_cadastro()
        self.criar_componentes_explicativos()  # Corrigido nome do método


    def criar_componentes_cadastro(self):
        self.titulo_cadastro = ctk.CTkLabel(
            self.frame_cadastro,
            text="Cadastro",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        self.titulo_cadastro.grid(row=0, column=0, padx=20, pady=10)


    def criar_componentes_explicativos(self):
        self.titulo_explicativo = ctk.CTkLabel(
            self.frame_explicativo,
            text="Como Funciona",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        self.titulo_explicativo.grid(row=0, column=0, padx=20, pady=10)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Cadastro")
        self.geometry("1920x1080")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.tela_cadastro = TelaCadastro(self)
        self.tela_cadastro.grid(row=0, column=0, sticky="nsew")

# Precisa criar um método main para executar essas funções
#if __name__ == "__main__":
#    app = App()
#    app.mainloop()
