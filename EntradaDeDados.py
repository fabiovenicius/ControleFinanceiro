# -*- coding: utf-8 -*-
import GravaLancamentos
from GravaLancamentos import *
import ExecSQL
# Funcao para entrada de informações


def entradadedados(meuarquivo):
    opcao = 'S'
    sql_categoria = 'select id,categoria from categoria'	
    while opcao == 'S' or opcao == 's':
        data = input('Informe a data da transação:')
        conta = input('Informe a conta:')
        descricao = input('Informe Descrição do Lançamento:')
        sql_categoria = 'select id,categoria from categoria'
        lista_categorias = ExecSQL.exec_select(sql_categoria)
        for lista in lista_categorias:
            print(lista['id'], lista['categoria'])
        categoria = input('Informe Categoria do Lançamento:')
        cenario = input('Informe o Cenário:')
        valor = float(input('Informe Valor a ser lançado:'))
        parcelas = int(input('Informe a quantidade de parcelas:'))
        GravaLancamentos.gravaLancamentos(data, conta, descricao,
                                          categoria, cenario, valor,
                                          parcelas, meuarquivo)
        opcao = input("Deseja Continuar?[S/N]:")
