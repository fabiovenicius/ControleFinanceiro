nomeConta = 'teste'
idConta = 1
tipoConta = 1
proprietarioConta = 1
-- Select Contas
select a.id, a.nome Conta, b.id, b.nome Tipo, c.id, c.nome Proprietario from conta a, tipoconta b, proprietario c where a.tipo = b.id and a.proprietario = c.id;
-- Atualiza Descricao
update conta set nome = @nomeConta where id = @idConta;
-- Atualiza Tipo de Conta
update conta set tipo = @tipoConta where id = @idConta;
-- Atualiza Proprietario da Conta
update conta set tipo = @proprietarioConta where id = @idConta;
-- Exclui registro
delete from conta where id = idConta;
-- Insere conta
insert into conta(nome,tipoconta,proprietario) values (nomeConta,tipoConta,proprietarioConta);
