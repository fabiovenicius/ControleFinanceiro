#!/usr/bin/python
# -*- coding: utf-8 -*-
import pymysql


def conn():

    # Criar um arquivo setup.txt com os parametros de conexao divididos por espaço

    arquivo = open('setup.txt', 'r')
    leitor = arquivo.read()
    parametros = leitor.split()
    db = pymysql.connect(host=parametros[0],
                       user=parametros[1],
                       password=parametros[2],
                       database=parametros[3],
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)
    return db

