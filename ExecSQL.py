#!/usr/bin/python
# -*- coding: utf-8 -*-
import GravaLancamentos
import mysql.connector
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
        print 'Erro: Não foi possível Executar comando sql %s' %(sql)
        db.rollback()
    db.close

def exec_select(sql, qtdcampos):
    db = ConectaDB.conn()
    cur = db.cursor()
    cur.execute(sql)
    valores = cur.fetchall()

    try:
        for linha in valores:
            contador = 0
            while(contador < qtdcampos):
                print linha[contador]
                contador += 1
        db.close()
    except:
        print 'Erro ao processar comando: \n %s \n Quantidade de elementos informados: %s' %(sql,qtdcampos)