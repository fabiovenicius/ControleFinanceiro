#!/usr/bin/python
# -*- coding: utf-8 -*-
import GravaLancamentos
import mysql.connector
import ConectaDB
import GravaLancamentos


#Inserir Movimentação Financeira
def exec_comando(sql):
    db = ConectaDB.conn()
    cur = db.cursor()
    try:
        cur.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close

