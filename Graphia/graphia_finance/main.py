import tkinter
from tkinter import *
from tkinter import ttk

from importer import importar_csv_nubank

caminho = ""

movimentacoes = importar_csv_nubank(caminho)

"""
Exigir no terminal
for movimentacao in movimentacoes:
    print(
        f"{movimentacao['data']} "
        f"{movimentacao['descricao']} "
        f"R$ {movimentacao['valor']}"
    )
"""

##desktop

#config
root = Tk()
root.title("My Application")
root.geometry("640x480")
root.minsize(320, 240)

#Elementos
ttk.Label(root, text="Hello").pack(padx=20, pady=20)

root.mainloop()
