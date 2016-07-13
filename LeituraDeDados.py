# -*- coding: utf-8 -*-
import csv
from csv import *

from datetime import date

import ContaLinhas
from ContaLinhas import *
# Programa para verificar linhas que deverão ser importadas


#Somente contagem de linhas do arquivo
extrato = open('extrato.csv', 'r')
totalLinhas = ContaLinhas.contaLinhas(extrato)
extrato.close()

#Abertura do arquivo para extração de dados
extrato = open('extrato.csv', 'r')
meuarquivo = open('LinhasExtrato.txt', 'w')
dados = csv.reader(extrato)
qtdLinhas = 0
for linhas in dados:
    qtdLinhas += 1
#Iniciar após a linha de Saldo Anterior e percorrer até a penultima linha, antes da linha com Saldo final
    if 2 < qtdLinhas < totalLinhas:
        data = linhas[0]
        dependenciaOrigem = linhas[1]
        historico = linhas[2]
        dataDoBalancete = linhas[3]
        numeroDoDocumento = linhas[4]
        valor = linhas[5]
        linha = data + ' ' + historico + ' ' + valor + '\n'
        meuarquivo.write(linha)
