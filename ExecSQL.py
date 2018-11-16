#!/usr/bin/python
# -*- coding: utf-8 -*-
import ConectaDB
import pymysql


# Inserir, modificar, deletar
def exec_comando(sql):
    db = ConectaDB.conn()
    cur = db.cursor()
    try:
        cur.execute(sql)
        db.commit()
    except(pymysql.err.OperationalError):
        print('Erro: Não foi possível Executar comando sql %s' % (sql))
        db.rollback()
    db.close


def exec_select(sql):
    db = ConectaDB.conn()
    cur = db.cursor()
    cur.execute(sql)
    valores = cur.fetchall()
    return valores
    db.close()
