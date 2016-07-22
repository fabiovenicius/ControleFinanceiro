#!/usr/bin/env python
import Tkinter
from Tkinter import *

class Principal(Frame):
    def __init__(self, master=None):
        principal = Tk()
        principal.title("Controle Financeiro")
        principal.geometry("800x400+100+100")
        fmContaBB = LabelFrame(principal,borderwidth=2, text="Banco do Brasil")
        fmContaBB.grid(row=0, column=0)


        btSair = Button(fmContaBB, text="Sair", command=self.sair)
        btSair.grid(row=1, column=0)


        fmContaBradesco = LabelFrame(principal, borderwidth=2, text="Bradesco")
        fmContaBradesco.grid(row=0, column=1)
        btFicar = Button(fmContaBradesco, text="Ficar", command=self.sair)
        btFicar.grid(row=0, column=1)

    def sair(self):
        import sys
        sys.exit()
Principal()
mainloop()


