# -*- coding: utf-8 -*-
import EntradaDeDados
# from EntradaDeDados import *
# Funcao para alimentar arquivo para sql


meuarquivo = open('sql/lancamentos.sql', 'w')
EntradaDeDados.entradadedados(meuarquivo)
meuarquivo.close()
