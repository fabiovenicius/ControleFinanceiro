# -*- coding: utf-8 -*-
import TrataDescricao
from TrataDescricao import *
#Funcao para gravar informações em arquivo sql


def gravaLancamentos(data, conta, descricao, categoria, cenario, valor,
parcelas, meuarquivo):
    parcelaAtual = 1
    while (parcelaAtual <= parcelas):
        descricao_completa = TrataDescricao.trataDescricao(data, conta,
descricao, categoria, cenario, valor, parcelas, parcelaAtual)
        meuarquivo.write(descricao_completa)
        parcelaAtual += 1