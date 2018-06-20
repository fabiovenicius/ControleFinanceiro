# -*- coding: latin-1 -*-
from datetime import date

from GravaLancamentos import gravaLancamentos
import csv
import ExecSQL
# Funcao para alimentar arquivo para sql


meuextrato = open('sql/dez.csv', newline='', encoding='latin-1')
meuarquivo = open('sql/lancamentos.sql', 'w')
leitor = csv.reader(meuextrato)

for cont, linha in enumerate(leitor):
    data = linha[0]
    try:
        ano = int(data[-4:])
    except ValueError:
        continue
    # Converte data em string no formato ‘YYYY-MM-DD’
    mes = int(data[0:2])
    dia = int(data[3:5])
    novadata = date(ano, mes, dia).isoformat()
    descricao = linha[2]
    valor = float(linha[5])
    print(data, descricao, valor)
    sql_categoria = 'select id,categoria from categoria'
    lista_categorias = ExecSQL.exec_select(sql_categoria)
    for lista in lista_categorias:
        print(lista['id'], lista['categoria'])
    categoria = input('Informe a categoria desejada (P-Pular):')
    if categoria == 'P' or categoria == 'p':
        continue
    conta = '2'
    cenario = '2'
    gravaLancamentos(novadata, conta, descricao,
                     categoria, cenario, valor,
                     1, meuarquivo)
meuextrato.close()
meuarquivo.close()
