# -*- coding: utf-8 -*-
import csv
from csv import *
# Função pra contar a quantidade de linhas em um arquivo


def contaLinhas(arquivo):
    dados = csv.reader(arquivo)
    contador = 0
    for linhas in dados:
        contador += 1
    return (contador)