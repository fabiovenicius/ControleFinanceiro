# -*- coding: utf-8 -*-
import GravaLancamentos
from GravaLancamentos import *
#Funcao para entrada de informações


def entradaDeDados(meuarquivo):
    opcao = 'S'
    while(opcao == 'S' or opcao == 's'):
        data = raw_input('Informe a data da transação:')
#        data = '2016-08-03'
        conta = raw_input('Informe a conta:')
#        conta = '6'
        descricao = raw_input('Informe Descrição do Lançamento:')
        categoria = raw_input('Informe Categoria do Lançamento:')
#        categoria = '55'
        cenario = raw_input('Informe o Cenário:')
#        cenario = '1'
        valor = float(input('Informe Valor a ser lançado:'))
        parcelas = input('Informe a quantidade de parcelas:')
#        parcelas = 1
        GravaLancamentos.gravaLancamentos(data, conta, descricao, categoria,
cenario, valor, parcelas, meuarquivo)
        opcao = raw_input("Deseja Continuar?[S/N]:")