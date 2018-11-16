import ExecSQL


def CadastrarNotaCorretagem(notacorretagem, conta, data):
    sql = "insert into notacorretagem(notacorretagem, conta, data) values" \
          "({},{},{});".format(notacorretagem, conta, data)
    ExecSQL.exec_comando(sql)

def ConsultarNotaCorretagem():
    sql = "select a.id, a.data, b.conta, a.notacorretagem from notacorretagem a," \
          "conta b where a.conta = b.id;"
    notas = ExecSQL.exec_select(sql)
    print(" Id Data       Conta Nota Corretagem")
    for nota in notas:
        print("{:>3} {} {:<5} {}".format(nota['id'],
                                      nota['data'],
                                      nota['conta'],
                                      nota['notacorretagem']))

def ExcluirNotaCorretagem(id):
    sql = "delete from notacorretagem where id = {};".format(id)
    ExecSQL.exec_comando(sql)