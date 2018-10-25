import ExecSQL


def CadastraDespesasFinanceira(despesa):
    sql = "insert into acoes(despesa) values" \
          "({});".format(despesa)
    ExecSQL.exec_comando(sql)

def ConsultaDespesasFinanceiras():
    sql = "select id,despesa from despesasfinanceiras;"
    despesas = ExecSQL.exec_select(sql)
    print(" Id Despesa")
    for despesa in despesas:
        print("{:>3} {}".format(despesa['id'],despesa['despesa']))