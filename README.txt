Programa desenvolvido em Python para Criação de Instrução Insert a partir de dados informados pelo Usuário

Requisitos do Projeto
1. Identificação do Proprietario
2. Menu de Cadastros
	- Conta, Tipo de Conta e Proprietario
	- Categoria e Grupo Categoria
	- Cenario
3. Visualização Detalhada dos lançamentos de 3 contas (ultimos lançamentos)
	- Incluir novos Lançamentos em qualquer conta cadastras
		- Com parcelas
		- Sem parcelas
	- Apagar Lançamentos de quaisquer contas
	- Editar Lançamentos de quaisquer contas
4. Cosulta de Saldos de todas as contas cadastradas (em ordem descrescente)
5. Consulta de gastos por Categoria ( todas as categoria em ordem descrescente)

Cadastros:
	- Conta
	- Tipo Conta
	- Proprietário
	- Categoria
	- GrupoCategoria
	- Cenário
	- MovtoFinanc
	- SubMovtoFinanc
	- Ativos
	- TipoAtivos
	- TipoLancamento
	- PainelControle (Melhorias Futuras)
	
Informações Principais:
	- Em Conta Corrente
		-Saldo Final
		-Movimentação
		-Gastos por Categoria
	- Em Investimentos
		-Valor Investido
		-Valor Atual
		-Percentual de Perda ou Ganho

Sequencia de Execução
1. CadastraLancamentos
2. EntradaDeDados
3. GravaLancamentos
4. TrataDescricao
5. TrataData

#CadastraLancamentos
Serve somente para abrir e fechar o arquivo onde será gravada a instrucao
#EntradaDeDados
Serve para o usuário cadastrar as informações
#GravaLancamentos
Serve para gravar as informações do usuário no arquivo, sendo tratadas as informações de descrição e data
quando o usuário informa que tem mais de uma parcela
ex.: Descricao -> 'COMPRA DE BIKE PARC 01/02', 'COMPRA DE BIKE PARC 02/02'
	 Data -> '2016-02-01' para Parcela 1 e '2016-03-01' para Parcela 2 (diferença de 1 mês, util para cartão de crédito ou empréstimo com parcelas fixas)
#TrataDescricao
Cria informações a respeito da parcela
#TrataData
Cria parcelamento de datas