# -*- coding: utf-8 -*-
from TrataDescricao import trataDescricao
from ExecSQL import exec_comando
#Funcao para gravar informações em arquivo sql


def gravaLancamentos(data, conta, descricao, categoria, cenario, valor,
parcelas, meuarquivo):
    parcelaAtual = 1
    while (parcelaAtual <= parcelas):
        descricao_completa = trataDescricao(data, conta,
descricao, categoria, cenario, valor, parcelas, parcelaAtual)
        #Gravação dos lançamentos no arquivo
        meuarquivo.write(descricao_completa)
        exec_comando(descricao_completa)
        parcelaAtual += 1