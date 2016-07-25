#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Tkinter
from Tkinter import *
import ExecSQL


class Principal(Frame):
    def __init__(self, master=None):
        principal = Tk()
        principal.title("Controle Financeiro")
        principal.geometry("800x400+100+100")
        fmContaBB = LabelFrame(principal,borderwidth=2, text="Banco do Brasil")
        fmContaBB.grid(row=0, column=0)

        lstLancamentos = Listbox(fmContaBB)
        valores = ExecSQL.exec_select("select id, nome, tipo from conta")
        contador = 1
        for conta in valores:
            lstLancamentos.insert(contador, (conta[0], conta[1], conta[2]))
            lstLancamentos.insert(contador, (conta[0], conta[1], conta[2]))
            contador += 1
            lstLancamentos.grid(row=0, column=0)


        btSair = Button(fmContaBB, text="Sair", command=self.sair)
        btSair.grid(row=1, column=0)

        fmContaBradesco = LabelFrame(principal, borderwidth=2, text="Bradesco")
        fmContaBradesco.grid(row=0, column=1)
        btFicar = Button(fmContaBradesco, text="Ficar", command=self.sair)
        btFicar.grid(row=0, column=1)

        fmDiversos = LabelFrame(principal, borderwidth=2, text="Informações Diversas")
        fmDiversos.grid(row=1, column=0)



    def sair(self):
        import sys
        sys.exit()
Principal()
mainloop()


