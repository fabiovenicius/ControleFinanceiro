import ExecSQL


def CadastraNotaCorretagem(notacorretagem):
    sql = "insert into notacorretagem(notacorretagem) values" \
          "({});".format(notacorretagem)
    ExecSQL.exec_comando(sql)

def ConsultaNotaCorretagem():
    sql = "select id, notacorretagem from notacorretagem;"
    notas = ExecSQL.exec_select(sql)
    print(" Id  Nota Corretagem")
    for nota in notas:
        print("{:>3} {}".format(nota['id'],nota['notacorretagem']))
