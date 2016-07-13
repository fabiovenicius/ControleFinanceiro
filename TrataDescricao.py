# -*- coding: utf-8 -*-
import TrataData
from TrataData import *
#Funcao para FORMATAR informações que serão gravadas no arquivo e acumular em
#descricao_completa


def trataDescricao(data, conta, descricao, categoria, cenario, valor,
parcelas, parcelaAtual):
    inicio = "insert into movtofinanc(datamovto,conta,descricao,categoria,\
cenario, valor) values (\'"
    caracter_virgula = "',"
    virgula = ","
    virgula_caracter = ",'"
    fim = ");\n"
# Unica Parcela
    if parcelas == 1:
        descricao_completa = inicio + data + caracter_virgula + conta + \
virgula_caracter + descricao + caracter_virgula + categoria + virgula + \
cenario + virgula + str(valor) + fim
        return descricao_completa
# Menos de 10 parcelas
    elif parcelas < 10:
        parcelamentoMenorQueDez = 1
        while(parcelamentoMenorQueDez <= parcelas):
            novaData = str(TrataData.trataData(data, parcelaAtual))
            novaDescricao = descricao + ' PARC 0' + str(parcelaAtual) + '/0' \
+ str(parcelas)
            descricao_completa = inicio + novaData + caracter_virgula + \
conta + virgula_caracter + novaDescricao + caracter_virgula + categoria + \
virgula + cenario + virgula + str(valor) + fim
            novaDescricao = ''
            novaData = ''
            parcelamentoMenorQueDez += 1
        return descricao_completa
# Mais de 10 parcelas
    elif parcelas >= 10:
        parcelamentoMaiorQueDez = 1
        while (parcelamentoMaiorQueDez <= parcelas):
# Tratamento para as parcelas menores que 10
            if (parcelaAtual < 10):
                novaDescricao = descricao + ' PARC 0' + str(parcelaAtual) + \
'/' + str(parcelas)
                novaData = str(TrataData.trataData(data, parcelaAtual))
                descricaoCompleta = inicio + novaData + caracter_virgula + \
conta + virgula_caracter + novaDescricao + caracter_virgula + categoria + \
virgula + cenario + virgula + str(valor) + fim
                novaDescricao = ''
                novaData = ''
# Tratamento para parcelas maiores que 10
            elif(parcelaAtual >= 10):
                novaDescricao = descricao + ' PARC ' + str(parcelaAtual) + \
'/' + str(parcelas)
                novaData = str(TrataData.trataData(data, parcelaAtual))
                descricaoCompleta = inicio + novaData + caracter_virgula + \
conta + virgula_caracter + novaDescricao + caracter_virgula + categoria + \
virgula + cenario + virgula + str(valor) + fim
                novaDescricao = ''
                novaData = ''
                parcelamentoMaiorQueDez += 1
            return descricaoCompleta