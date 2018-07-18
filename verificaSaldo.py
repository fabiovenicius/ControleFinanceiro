# coding: utf-8
import csv
import ExecSQL
from datetime import date


def maintmp():
    extrato = "set"
    datafinal = informarsaldofinal(extrato)
    ano = datafinal[6:10]
    consultardetalhebd(extrato, 1, ano)


def main():
    extratos = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set",
                "out", "nov", "dez"]

    for extrato in extratos:
        print("Extrato: " + extrato.capitalize() + "/2017")
        datainicial = informarsaldoinicial(extrato)
        consultarsaldodb(datainicial)
        datafinal = informarsaldofinal(extrato)
        ano = datafinal[6:10]
        consultarsaldodb(datafinal)

    opcao = input("Deseja verificar algum extrato detalhadamente (S/N): ")

    if opcao.upper() == "S":
        mes = input(f"Informe o mês desejado  em {extratos}: ")
        if mes in extratos:
            try:
                for dia_extrato in range(1, 32, 1):
                    print("Dia {}:".format(dia_extrato))
                    consultardetalhesextrato(mes, dia_extrato)
                    consultardetalhebd(mes, dia_extrato, ano)
            except ValueError:
                print("Mês de 30 dias.")

        else:
            print(f"Mês informado {mes} não é válido")
    elif opcao.upper() == "N":
        print("Rotina finalizada pelo usuário.")
    else:
        print("Opção não é válida!")
#


def contarlinhas(arquivo):
    """
    Programa verifica e retorna a quantidade de linhas do Extrato
    :param arquivo: Nome do extrato que será pesquisado formato mmm.csv
    :return: Quantidade de linhas do Extrato
    """
    extrato = "sql/" + arquivo + ".csv"
    with open(extrato, newline='', encoding='latin-1') as meuextrato:
        leitorquantidade = csv.reader(meuextrato)

        quantidadelinhastotais = 0

        for linha in leitorquantidade:
            quantidadelinhastotais += 1
    # print(quantidadelinhastotais)
    return quantidadelinhastotais


def informarsaldoinicial(arquivo):
    """
    Programa imprime saldo inicial do extrato e armazena a informação da Data
    Inicial
    :param arquivo: Nome do extrato que será pesquisado formato mmm.csv
    :return: Data inicial do Extrato
    """
    extrato = "sql/" + arquivo + '.csv'
    with open(extrato, newline='', encoding='latin-1') as meuextrato:
        leitorsaldoinicial = csv.reader(meuextrato)

        contadordelinhainicial = 0

        for linha in leitorsaldoinicial:
            contadordelinhainicial += 1
            if contadordelinhainicial == 2:
                data = linha[0]
                descricao = linha[2]
                valor = linha[5]
                print("Origem: Extrato. Data: {0:10}. Descrição: {1:20}\
                        . Valor: {2:7}".format(data, descricao, valor))
                # saldoAnteriorExtrato = float(linha[5])
                datainicialextrato = linha[0]
    return datainicialextrato


def informarsaldofinal(arquivo):
    """
    Programa imprime saldo final do Extrato
    :param arquivo: Nome do extrato que será pesquisado formato mmm.csv
    :return: Data final do Extrato
    """
    extrato = "sql/" + arquivo + '.csv'
    with open(extrato, newline='', encoding='latin-1') as meuextrato:
        leitorSaldoFinal = csv.reader(meuextrato)

        contadordelinhafinal = 0
        ultimaLinha = contarlinhas(arquivo)
        for linha in leitorSaldoFinal:
            contadordelinhafinal += 1
            if contadordelinhafinal < ultimaLinha:
                pass
            else:
                data = linha[0]
                descricao = linha[2]
                valor = linha[5]
                print("Origem: Extrato. Data: {0:10}. Descrição: {1:20}\
                . Valor: {2:7}".format(
                    data, descricao, valor))
                # saldoFinalExtrato = float(linha[5])
                datafinalextrato = linha[0]
    return datafinalextrato


def converterdata(data):
    """
    Programa converte do formato mm/dd/aaaa para aaaa-mm-dd
    :param data: Data no formato mm/dd/aaaa
    :return: Data no formato aaaa-mm-dd
    """
    dataformatada = data[6:11] + "-" + data[0:2] + "-" + data[3:5]
    return dataformatada


def consultarsaldodb(data):
    """
    Programa imprime saldo registrado no Banco de Dados na Data Inicial e Final
    :param data: Data informada
    :return:
    """
    if data == "12/30/2016":
        sql = "select valor saldo from movtoconta where conta = 2 and id =1"
    else:
        sql = "select sum(valor) saldo from movtoconta where conta = 2 and\
         datamovto <= '{}'".format(
            converterdata(data))
    descricao = "Saldo na Data"
    saldo = ExecSQL.exec_select(sql)
    # print(data)
    valor = float(saldo[0]["saldo"])
    # print(type(valor))
    # print(sql)
    print("Origem:Database. Data: {0:10}. Descrição: {1:20}\
    . Valor: {2:7.2f}".format(
        data, descricao, valor))

    # with open(extrato, newline='', encoding='latin-1') as meuextrato:
#
#
#
    #     sql = "select datamovto, descricao, valor " \
    #           "from movtoconta where conta = 2 and " \
    #           "datamovto = '{}'".format(data_extrato)
#
    #     print(sql)
#
    #     dadosdb = ExecSQL.exec_select(sql)
#
    #     for linhadb in dadosdb:
    #             data = linhadb['datamovto']
    #             descricao = linhadb['descricao'] + " - DB"
    #             valor = linhadb['valor']
    #             print("{0:} {1:70} {2:8}".format(data, descricao, valor))


def consultardetalhesextrato(mes, dia_extrato):
    extrato = "sql/" + mes + '.csv'
    limite = contarlinhas(mes)
    # extrato_estruturado = dict()
    with open(extrato, newline='', encoding='latin-1') as meuextrato:
        leitor = csv.reader(meuextrato)
        for num, i in enumerate(leitor, 1):
            if num > 2 and num < limite:
                dia = int(i[0][3:5])
                descricao = i[2] + " - Extrato: " + i[0][3:5] + "/" +\
                    i[0][0:2] + "/" + i[0][6:10]
                valor = float(i[5])
                if dia_extrato == dia:
                    print("{0:90}{1:8.2f}".format(descricao, valor))


def consultardetalhebd(mes, dia_db, ano):
    meses = {"jan": 1, "fev": 2, "mar": 3, "abr": 4, "mai": 5, "jun": 6,
             "jul": 7, "ago": 8, "set": 9, "out": 10, "nov": 11, "dez": 12}
    sql = "select datamovto, descricao, valor from movtoconta where conta = 2\
           and datamovto = '{}'"\
        .format(date(2017,  meses[mes], dia_db))

    dadosdb = ExecSQL.exec_select(sql)

    for i in dadosdb:
        # data = i["datamovto"]
        descricao = i["descricao"] + " - DB"
        valor = i["valor"]
        print("{0:90}{1:8.2f}".format(descricao, valor))


if __name__ == "__main__":
    main()
