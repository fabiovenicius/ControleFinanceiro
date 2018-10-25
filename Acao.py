import ExecSQL


def CadastraAcao(papel, descricao):
    sql = "insert into acoes(papel,descricao) values" \
          "({},{});".format(papel,descricao)
    ExecSQL.exec_comando(sql)

def CadastraMovtoAcao(dataMovto,conta,papel,valor_unitario,tipo_movto,
                      quantidade,notaCorretagem):
    ''' Cadastramento do Movto da Ação - Memoria de Cálculo'''
    cadastramovto = "insert into movtoacoes(datamovto,conta,papel," \
          "valor_unitario,tipo_movo,quantidade,notacorretagem) values" \
          "('{}',{},{},{},{},{},'{}');".format(dataMovto, conta, papel, valor_unitario,
                                    tipo_movto, quantidade, notaCorretagem)
    ExecSQL.exec_comando(cadastramovto)
    '''Atualização dos Saldos das ações em carteira'''
    if tipo_movto == 1:
        valor_total = quantidade * valor_unitario
    else:
        quantidade = quantidade * -1
        valor_total = quantidade * valor_unitario
    AtualizarSaldoAcoes(conta,papel,quantidade,valor_total)

def AtualizarSaldoAcoes(conta, papel, quantidade, valor_total):
    sql = "insert into saldoacoes(conta,papel,quantidade," \
          "valor_total) values ({},{},{},{});".format(conta,
                                                      papel, 
                                                      quantidade,
                                                      valor_total)
    ExecSQL.exec_comando(sql)

def ConsultaAcoes():
    sql = "select id, papel, descricao from acoes;"
    acoes = ExecSQL.exec_select(sql)
    print(" Id  Ação  Descrição")
    for acao in acoes:
        print("{:>3} {:>6} {}".format(acao['id'],acao['papel'],acao['descricao']))


def ConsultaSaldoAcoes():
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
