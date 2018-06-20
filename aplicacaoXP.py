# coding: utf-8
import ExecSQL


def principal():

    listaopcoes = ["1", "2", "3", "4", "5"]

    executa = True
    while executa:
        opcao = input("Informe o movimento desejado \n"
                      "1. Inserir \n"
                      "2. Excluir \n"
                      "3. Alterar \n"
                      "4. Relatório \n"
                      "5. Sair \n"
                      "Opçao Desejada: ")

        if opcao in listaopcoes:
            if opcao == "1":
                menu("inserir")
            elif opcao == "2":
                menu("excluir")
            elif opcao == "3":
                menu("alterar")
            elif opcao == "4":
                imprimir_relatorio()
            else:
                print("Programa finalizado pelo usuário!")
                executa = False

        else:
            print("Valor inválido!")


def menu(opcao):
    lista_opcoes = ["1", "2", "3", "4", "5", "6", "7", "8", "S", "s"]
    validaopcao = True
    while validaopcao:
        if opcao == "alterar":
            opcao_menu = input("Informe o que deseja {}: \n"
                               "1. Ações \n"
                               "2. Fundos Imobiliários \n"
                               "3. Fundos de Investimentos \n"
                               "4. Renda Fixa \n"
                               "5. COE \n"
                               "6. Tesouro Direto \n"
                               "7. Proventos \n"
                               "8. Saldo em Conta Corrente \n"
                               "S. Retornar ao menu anterior \n"
                               "Opção Desejada: ".format(opcao))
        else:
            opcao_menu = input("Informe o que deseja {}: \n"
                               "1. Ações \n"
                               "2. Fundos Imobiliários \n"
                               "3. Fundos de Investimentos \n"
                               "4. Renda Fixa \n"
                               "5. COE \n"
                               "6. Tesouro Direto \n"
                               "7. Proventos \n"
                               "S. Retornar ao menu anterior \n"
                               "Opção Desejada: ".format(opcao))

        if opcao_menu in lista_opcoes:
            if opcao_menu == "S" or opcao_menu == "s":
                validaopcao = False
            elif opcao != "alterar" and opcao_menu == "8":
                print("Valor Inválido!")
            else:
                if opcao == "inserir":
                    inserir_valores(opcao_menu)
                elif opcao == "alterar":
                    alterar_valores(opcao_menu)
                else:
                    excluir_valores(opcao_menu)

        else:
            print("Valor Inválido!")


def listarvalores(opcao):
    if opcao == "1":
        tabela = "select * from acao where tipoacao = 1"
        relatorio = ExecSQL.exec_select(tabela)
        print("Id Papel          TA Data        Qtd   Vlr")
        for i in relatorio:
            print("{0:2} {1:20} {2:2} {3:11} {4:6} {5:8}"
                  .format(i['id'], i['papel'], i['tipoacao'], i['datamovto'],
                          i['quantidade'], i['valor'])
                  )
    elif opcao == "2":
        tabela = "select * from acao where tipoacao = 2"
        relatorio = ExecSQL.exec_select(tabela)
        print("Id Papel          TA Data        Qtd   Vlr")
        for i in relatorio:
            print("{0:2} {1:20} {2:2} {3:11} {4:6} {5:8}"
                  .format(i['id'],
                          i['papel'], i['tipoacao'], i['datamovto'],
                          i['quantidade'], i['valor'])
                  )
    elif opcao == "3":
        tabela = "select * from fundos"
        relatorio = ExecSQL.exec_select(tabela)
        for i in relatorio:
            print(i)
    elif opcao == "4":
        tabela = "select * from rendafixa where tipo != 'COE'"
        relatorio = ExecSQL.exec_select(tabela)
        for i in relatorio:
            print(i)
    elif opcao == "5":
        tabela = "select * from rendafixa where tipo = 'COE'"
        relatorio = ExecSQL.exec_select(tabela)
        for i in relatorio:
            print(i)
    elif opcao == "6":
        tabela = "select * from tesourodireto"
        relatorio = ExecSQL.exec_select(tabela)
        for i in relatorio:
            print(i)
    elif opcao == "7":
        tabela = "select * from proventos"
        relatorio = ExecSQL.exec_select(tabela)
        for i in relatorio:
            print(i)
    else:
        tabela = "select contacorrente from saldocontainvestimento"
        relatorio = ExecSQL.exec_select(tabela)
        for i in relatorio:
            print(i)


def imprimir_relatorio():
    print("Ações: \n")
    listarvalores("1")
    print("Fundos Imobiliários: \n")
    listarvalores("2")
    print("Fundos de Investimentos: \n")
    listarvalores("3")
    print("Renda Fixa: \n")
    listarvalores("4")
    print("COE: \n")
    listarvalores("5")
    print("Tesouro Direto: \n")
    listarvalores("6")
    print("Proventos: \n")
    listarvalores("7")
    print("Conta Corrente: \n")
    listarvalores("8")


def inserir_valores(opcao_menu):
    valores_validos = {"1": ["acao", "papel,tipoacao,datamovto,quantidade,\
                        valor"],
                       "2": ["acao", "papel,tipoacao,datamovto,quantidade,\
                       valor"],
                       "3": ["fundos", "nome,data,quantidade,valorcota,\
                       valorliquido,valorbruto,IR,IOF"],
                       "4": ["rendafixa", "tipo,papel,emissor,datavencimento,\
                       valorpu,datapu,valorbruto,IR,IOF"],
                       "5": ["rendafixa", "nome,data,quantidade,valorcota,\
                       valorliquido,valorbruto,IR,IOF"],
                       "6": ["teourodireto", "tipo,papel,datavencimento,\
                       quantidade,valorpu,valorbruto"],
                       "7": ["proventos", "papel,datamovto,valor"]}
    listarvalores(opcao_menu)
    campo_comando = ""
    if opcao_menu in valores_validos.keys():
        campos = "show columns in {}".format(valores_validos[opcao_menu][0])
        lista_campos = ExecSQL.exec_select(campos)
        for campo in lista_campos:
            if campo["Field"] != "id":
                displaycampo = campo["Field"]
                comando = input("Informe o valor de {}: "
                                .format(displaycampo.upper()))
                try:
                    if comando[4] == "-":
                        comando = "'" + comando + "'"
                    elif comando[0].isalpha():
                        comando = "'" + comando + "'"
                    else:
                        pass
                except IndexError:
                    if comando[0].isnumeric():
                        pass
                    else:
                        comando = "'" + comando + "'"

                campo_comando = campo_comando + comando + ","

        sql = "insert into {}({}) values ({})"\
            .format(valores_validos[opcao_menu][0],
                    valores_validos[opcao_menu][1],
                    campo_comando[0:-1])
        ExecSQL.exec_comando(sql)
    else:
        print("Alguma coisa saiu Errada")


def alterar_valores(opcao_menu):
    print("Alterar valor em {}".format(opcao_menu))
    listarvalores(opcao_menu)
    # TODO


def excluir_valores(opcao_menu):
    valores_validos = {"1": ["acao", "acao where tipoacao = 1", "papel,\
    tipoacao,datamovto,quantidade,valor"],
                       "2": ["acao", "acao where tipoacao = 2", "papel,\
    tipoacao,datamovto,quantidade,valor"],
                       "3": ["fundos", "fundos", "nome,data,quantidade,\
                       valorcota,valorliquido,valorbruto,IR,IOF"],
                       "4": ["rendafixa", "rendafixa where tipo != 'COE'",
                             "tipo,papel,emissor,datavencimento,valorpu,datapu,\
                             valorbruto,IR,IOF"],
                       "5": ["rendafixa", "rendafixa where tipo == 'COE'",
                             "nome,data,quantidade,valorcota,valorliquido,\
                             valorbruto,IR,IOF"],
                       "6": ["teourodireto", "tesourodireto",
                             "tipo,papel,datavencimento,quantidade,valorpu,\
                             valorbruto"],
                       "7": ["proventos", "proventos", "papel,datamovto,\
                       valor"]}

    valida = True
    while valida:
        listarvalores(opcao_menu)
        opcao = input("Informe o Id do valor que deseja Excluir (S-Sair): ")
        if opcao == "S" or opcao == "s":
            valida = False
        else:
            sql = "delete from {} where id = {}"\
                .format(valores_validos[opcao_menu][0], opcao)
            ExecSQL.exec_comando(sql)


if __name__ == "__main__":
    principal()
