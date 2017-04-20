#!/usr/bin/python
# -*- coding: utf-8 -*-
import GravaLancamentos
import pymysql
import ConectaDB
import GravaLancamentos


#Inserir, modificar, deletar
def exec_comando(sql):
    db = ConectaDB.conn()
    cur = db.cursor()
    try:
        cur.execute(sql)
        db.commit()
    except:
        print ('Erro: Não foi possível Executar comando sql %s' % (sql))
        db.rollback()
    db.close


def exec_select(sql):
    db = ConectaDB.conn()
    cur = db.cursor()
    cur.execute(sql)
    valores = cur.fetchall()
    return valores
    # for linha in valores:
    #    print(linha)                
    db.close()    