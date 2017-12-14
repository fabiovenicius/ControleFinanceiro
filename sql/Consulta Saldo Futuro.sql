-- update movtofinanc set valor=-198.11 where id=225;

/*insert into movtofinanc(datamovto,conta,descricao,categoria,cenario,valor) values
('2016-05-03',2,'PARQUE SHOPPING',55,2,-5);*/

-- EXCLUIR PROVIS�O DE DESPESAS COM CART�O
delete from movtofinanc where categoria = 56;
-- INSERIR PROVIS�O DESPESAS COM CART�O
insert into movtofinanc(datamovto,conta,descricao,categoria,cenario,valor) 
select datamovto,2,'PROV DESPESA OUROCARD',56,1,round(sum(valor),2) from movtofinanc where conta = 6 and datamovto > now() group by datamovto;

select id, a.datamovto,a.descricao,a.valor,(select round(sum(b.valor),2) from movtofinanc b where b.datamovto <= a.datamovto and a.conta = b.conta) Saldo from movtofinanc a
where a.conta = 2 and a.datamovto between adddate(now(),-5) and adddate(now(),20) order by a.datamovto, a.valor DESC;

select 'Ourocard', date_format(datamovto,'%Y-%m') Per�odo,round(sum(valor),2) Valor from movtofinanc where conta=6
group by date_format(datamovto,'%YYYY-%mm')
order by date_format(datamovto,'%YYYY-%mm')