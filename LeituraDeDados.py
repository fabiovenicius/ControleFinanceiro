# -*- coding: utf-8 -*-
import csv
from csv import *
import ContaLinhas
from ContaLinhas import *
# Programa para verificar linhas que deverão ser importadas


extrato = open('c:\\dados\\extrato.csv', 'r')
totalLinhas = ContaLinhas.contaLinhas(extrato)
extrato = open('c:\\dados\\extrato.csv', 'r')
meuarquivo = open('c:\\dados\\LinhasExtrato.txt', 'w')
ultimalinha = open('c:\\dados\\ultimoExtrato.txt', 'w')
dados = csv.reader(extrato)
qtdLinhas = 0
for linhas in dados:
    qtdLinhas += 1
#Iniciar após a linha de Saldo Anterior e percorrer até a penultima linha
    if qtdLinhas == totalLinhas - 1:
        data = linhas[0]
        dependenciaOrigem = linhas[1]
        historico = linhas[2]
        dataDoBalancete = linhas[3]
        numeroDoDocumento = linhas[4]
        valor = linhas[5]
        linha = data + ' ' + historico + '\n'
        ultimalinha.write(linha)
    if 2 < qtdLinhas < totalLinhas:
        data = linhas[0]
        dependenciaOrigem = linhas[1]
        historico = linhas[2]
        dataDoBalancete = linhas[3]
        numeroDoDocumento = linhas[4]
        valor = linhas[5]
        linha = data + ' ' + historico + '\n'
        meuarquivo.write(linha)
