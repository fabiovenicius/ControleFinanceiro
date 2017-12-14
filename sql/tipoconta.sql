idTipoConta = 1
nomeTipoConta = 'Teste'
-- Select Tipo Conta
select a.id, a.nome from tipoconta;
-- Atualiza Nome
update tipoconta set nome = @nomeTipoConta where id = @idTipoConta;
-- Apaga tipoconta
delete from tipoconta where id = idTipoConta;
-- Insere tipo conta
insert into tipoconta(nome) values nomeTipoConta
