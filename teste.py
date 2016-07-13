# -*- coding: utf-8 -*-
import TrataData
from TrataData import *


parcelaAtual = 1
data = '2016-07-03'
parcelas = 10

while (parcelaAtual <= parcelas):
    novaData = str(TrataData.trataData(data, parcelaAtual))
    print 'Passado:' + data + ' Retornado:' + novaData + ' Loop:' + \
str(parcelaAtual)
    parcelaAtual += 1
    novaData = ''