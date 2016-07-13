# -*- coding: utf-8 -*-


def trataDescricao(data, conta, descricao, categoria, cenario, valor,
parcelas, parcelaAtual):
    descricao_completa = 'Parcela 0' + str(parcelaAtual) + '\n'
    parcelas += 1
    return descricao_completa