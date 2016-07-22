# -*- coding: utf-8 -*-
import EntradaDeDados
from EntradaDeDados import *
#Funcao para alimentar arquivo para sql


meuarquivo = open('lancamentos.sql', 'w')
EntradaDeDados.entradaDeDados(meuarquivo)
meuarquivo.close()