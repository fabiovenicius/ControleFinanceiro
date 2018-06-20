# -*- coding: utf-8 -*-
from datetime import date


def trataData(data, parcela):
    ano = int(data[0:4])
    mes = int(data[5:7])
    dia = int(data[8:10])
    dataInformada = date(ano, mes, dia)
    if (parcela == 1):
        novaData = dataInformada
    else:
        qtdDiasAcrescentados = (parcela - 1) * 30
        novaDataIntermediaria = \
            date.fromordinal(date.toordinal(dataInformada) +
                             qtdDiasAcrescentados)
        if (novaDataIntermediaria.day == 28):
            novaDataIntermediaria = \
                date.fromordinal(date.toordinal(dataInformada) +
                                 qtdDiasAcrescentados + 3)
            novaData = date(novaDataIntermediaria.year,
                            novaDataIntermediaria.month, dia)
        elif (novaDataIntermediaria.day == 29):
            novaDataIntermediaria = \
                date.fromordinal(date.toordinal(dataInformada) +
                                 qtdDiasAcrescentados + 3)
            novaData = date(novaDataIntermediaria.year,
                            novaDataIntermediaria.month, dia)
        elif (novaDataIntermediaria.day == 30):
            novaDataIntermediaria = \
                date.fromordinal(date.toordinal(dataInformada) +
                                 qtdDiasAcrescentados + 2)
            novaData = date(novaDataIntermediaria.year,
                            novaDataIntermediaria.month, dia)
        elif (novaDataIntermediaria.day == 31):
            novaDataIntermediaria = \
                date.fromordinal(date.toordinal(dataInformada) +
                                 qtdDiasAcrescentados + 1)
            novaData = date(novaDataIntermediaria.year,
                            novaDataIntermediaria.month, dia)
        else:
            novaData = date(novaDataIntermediaria.year,
                            novaDataIntermediaria.month, dia)
        qtdDiasAcrescentados = 0
    return novaData
