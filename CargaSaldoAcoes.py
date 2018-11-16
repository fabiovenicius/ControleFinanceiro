import ExecSQL

def CarregarSaldos():
    sql = "select b.conta,a.papel, a.valor_unitario,a.quantidade " \
          "from movtoacoes a, notacorretagem b where a.notacorretagem = b.id"
    movtos = ExecSQL.exec_select(sql)
    for movto in movtos:        
        conta = movto['conta']
        papel = movto['papel']
        valor_unitario = movto['valor_unitario']
        quantidade = movto['quantidade']
        print(conta,papel,valor_unitario * quantidade)
CarregarSaldos()