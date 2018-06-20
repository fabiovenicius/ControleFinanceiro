import ExecSQL


def listar_tabelas():
    tabelas = "show tables"
    lista_tabelas = ExecSQL.exec_select(tabelas)
    print("Lista de Tabelas: ")
    for lt in lista_tabelas:
        print("# Tabela:")
        tabela = lt['Tables_in_venic708_financapessoal']
        print(tabela)
        campos = "show columns in {}".format(tabela)
        lista_campos = ExecSQL.exec_select(campos)
        print("   Campos:")
        for lc in lista_campos:
            print("   {0:20}{1:25}".format(lc['Field'], lc['Type']))


if __name__ == "__main__":
    listar_tabelas()
