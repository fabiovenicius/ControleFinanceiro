Programa desenvolvido em Python para Criação de Instrução Insert a partir de dados informados pelo Usuário
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