import ExecSQL


def CadastrarAcao(papel, descricao, nomepregao,atividade):
    sql = "insert into acoes(papel, descricao, nomepregao,atividade) values" \
          "({},{},{},{});".format(papel, descricao, nomepregao,atividade)
    ExecSQL.exec_comando(sql)

def CadastrarMovtoAcao(notaCorretagem,papel,tipo_movto,valor_unitario,
                      quantidade):
    if tipo_movto == 2:
        quantidade = quantidade * -1
    ''' Cadastramento do Movto da Ação - Memoria de Cálculo'''
    sql = "insert into movtoacoes(notacorretagem,papel,tipo_movto," \
          "valor_unitario,quantidade) values" \
          "({},{},{},{},{});".format(notaCorretagem, 
                                     papel,
                                     tipo_movto,
                                     valor_unitario,
                                     quantidade)
    ExecSQL.exec_comando(sql)

def AtualizarSaldoAcoes(conta, papel, quantidade, valor_total):
    sql = "insert into saldoacoes(conta,papel,quantidade," \
          "valor_total) values ({},{},{},{});".format(papel,                                                     papel, 
                                                      quantidade,
                                                      valor_total)
    ExecSQL.exec_comando(sql)

def ConsultarAcoes(nomepregao):
    sql = "select id, papel, descricao, nomepregao, atividade from acoes " \
          "where nomepregao like '{}';".format(nomepregao.capitalize())
    acoes = ExecSQL.exec_select(sql)
    for acao in acoes:
        print("{:>3} {:>6} {} {} {}".format(acao['id'],
                                            acao['papel'],
                                            acao['descricao'],
                                            acao['nomepregao'],
                                            acao['atividade']))


def ConsultarSaldoAcoes():
    sql = "select c.conta, b.papel, sum(a.quantidade) quantidade," \
          "sum(a.valor_total) total from saldoacoes a, acoes b, " \
          "conta c where a.papel = b.id and a.conta = c.id " \
          "group by c.conta, b.papel order by c.conta, b.papel;"
    consulta = ExecSQL.exec_select(sql)
    print("Conta  Papel Quantidade Valor")
    for linha in consulta:
        if linha['quantidade'] != 0:
            print("{0:>5} {1:>6} {2:>10} {3:>4.2f}".format(linha['conta'], linha['papel'], linha['quantidade'], linha['total']))

def ConsultaValorTotalemAcoes():
    sql = "select round(sum(valor_total),2) 'valor' from saldoacoes where quantidade > 0;"
    TotalEmAcoes = ExecSQL.exec_select(sql)
    print(TotalEmAcoes[0]['valor'])

def ConsultaAcaoPorNotaCorretagem(notacorretagem):
    print("Nota de Corretagem: " + notacorretagem)
    print('Negócios Realizados')
    sql = "select a.data_movto," \
          "d.conta,c.papel,e.tipo_movto,a.quantidade," \
          "a.valor_unitario," \
          "round(a.quantidade * a.valor_unitario,2) total " \
          "from movtoacoes a, notacorretagem b, acoes c, " \
          "conta d, tipomovto e where b.notacorretagem = {} and " \
          "a.notacorretagem = b.id "\
          "and a.papel = c.id and a.conta = d.id " \
          "and a.tipo_movto = e.id" \
          " order by c.papel;".format(notacorretagem)
    acoes = ExecSQL.exec_select(sql)
    print("Conta Papel Trans  Quant Vl Unit Vl Total")
    for acao in acoes:
        print("{:>5} {:>4} {:>6}" \
              "{:>4} {:>9} {:>8}".format(acao['conta'], \
              acao['papel'],acao['tipo_movto'], \
              acao['quantidade'],acao['valor_unitario'], \
              acao['total']))
    ConsultaDespesasFinanceiras(notacorretagem)

def ConsultaDespesasFinanceiras(notacorretagem):
    sql = "select b.despesa, a.valor from movtodespesasfinanceiras a, " \
          "despesasfinanceiras b, notacorretagem c " \
          "where a.despesa = b.id and a.notacorretagem = " \
          "c.id and c.notacorretagem = {};".format(notacorretagem)
    despesas = ExecSQL.exec_select(sql)
    print("Despesa Valor")
    for despesa in despesas:
        print("{} {}".format(despesa['despesa'],despesa['valor']))
