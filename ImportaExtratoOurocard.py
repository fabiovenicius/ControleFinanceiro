# -*- coding: utf-8 -*-
import GravaLancamentos
from GravaLancamentos import *
#import csv
#Funcao para alimentar arquivo para sql


meuextrato=open(r'C:\Users\M050183\Downloads\OUROCARD_PLATINUM_VISA-Próxima_Fatura.txt','r')
meuarquivo = open(r'c:\temp\lancamentos.sql', 'w')
#leitor=csv.reader(meuextrato,delimiter=',',quotechar='"')
data_lancamento=input('Informe a Data para lançamento:')

for linha in meuextrato:
    try:
        data = int(linha[0])
    except(ValueError):
        continue
    if linha[33:37] == 'Auto':
        continue
    else:
        if linha[76:77]=='0':
            data = linha[0:5]
            '''Tratamento deslocamento na linha de descricao'''
            try:
                descricao = int(linha[32:33])
            except(ValueError):
                descricao = linha[9:32]+' '
            else:
                descricao = linha[9:33]
            ''' Tratamento do deslocamento na linha de cidade'''
            try:
                cidade=int(linha[32:33])
            except(ValueError):		
                cidade=linha[32:48]
            else:
                cidade=linha[34:48]
            if linha[32:33] == '0':
                continue
            '''Tratamento valor decimal'''
            valortemp=linha[51:69]
            #print(linha[34:38])
            inteiro=float(valortemp.split(',')[0])
            decimal=float(valortemp.split(',')[1]) / 100
            valor=(inteiro+decimal) * -1
            conta = '6'
            cenario='1'
            descricao_completa = descricao+'-'+'Data:'+data+'-Local:'+cidade
            print(descricao_completa,valor)
            sql_categoria = 'select id,categoria from categoria'
            lista_categorias = ExecSQL.exec_select(sql_categoria)
            for lista in lista_categorias:
                print(lista['id'],lista['categoria'])
            categoria=input('Informe a categoria desejada (P-Pular):')
            if (categoria=='P' or categoria=='p'):
                continue
            parcelas=int(input('Informe a quantidade de parcelas:'))
            GravaLancamentos.gravaLancamentos(data_lancamento, conta, descricao_completa, categoria,		
        cenario, valor, parcelas, meuarquivo)
meuextrato.close()
meuarquivo.close()