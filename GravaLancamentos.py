# -*- coding: utf-8 -*-
import TrataDescricao
from TrataDescricao import *
import ExecSQL
#Funcao para gravar informações em arquivo sql


def gravaLancamentos(data, conta, descricao, categoria, cenario, valor,
parcelas, meuarquivo):
    parcelaAtual = 1
    while (parcelaAtual <= parcelas):
        descricao_completa = TrataDescricao.trataDescricao(data, conta,
descricao, categoria, cenario, valor, parcelas, parcelaAtual)
        #Gravação dos lançamentos no arquivo
        meuarquivo.write(descricao_completa)
        ExecSQL.exec_comando(descricao_completa)
        parcelaAtual += 1