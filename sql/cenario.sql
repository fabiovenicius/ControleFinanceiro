nomeCenario = 'teste'
idCenario = 1

-- Select Contas
select a.id, a.cenario from cenario;
-- Atualiza Descricao
update cenario set cenario = nomeCenario where id = @idConta;
-- Atualiza Tipo de Conta
update cenario set cenario = nomeCenario where id = idCenario;
-- Exclui registro
delete from cenario where id = idCenario;
-- Insere conta
insert into cenario(cenario) values (nomeCenario);
