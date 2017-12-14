idProprietario = 1
nomeProprietario = 'Teste'
senhaProprietario = 'Senha'
-- Select Proprietario
select a.id, a.nome, senha from proprietario;
-- Atualiza Nome
update proprietario set nome = nomeProprietario where id = idProprietario;
-- Atualiza Senha
update proprietario set senha = senhaProprietario where id = idProprietario;

delete from proprietario where id = idProprietario
-- Insere proprietario
insert into proprietario(nome) values nomeTipoConta
