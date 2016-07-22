#!/usr/bin/python
# -*- coding: utf-8 -*-
import mysql.connector

def conn():
    # Criar um arquivo setup.txt com os parametros de conexao divididos por espaço
    arquivo = open('setup.txt','r')
    leitor = arquivo.read()
    parametros = leitor.split()

    db = mysql.connector.connect(host = parametros[0],    # your host, usually localhost
                     user = parametros[1],         # your username
                     passwd = parametros[2],  # your password
                     db = parametros[3])        # name of the data base
    # you must create a Cursor object. It will let
    #  you execute all the queries you need
    return db

# Use all the SQL you like
#cur.execute("SELECT * FROM movtofinanc where conta = 2 order by datamovto")

# print all the first cell of all the rows
#for row in cur.fetchall():
#    print row[0], row[1], row[3], row[6]

