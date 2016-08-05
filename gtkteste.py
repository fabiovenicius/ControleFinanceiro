#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygtk
pygtk.require("2.0")  # Essa linha define a versão do pygtk a ser importado
import gtk


# Criando a Classe do Programa
class InverterApp(object):
    def __init__(self):
        # Agora como eu havia dito vamos utilizar uma função da classe gtk.Builder
        # para carregar o arquivo XML gerado pelo Glade.

        builder = gtk.Builder()  # Primeiramente criamos uma instância da classe
        builder.add_from_file("inverter.glade")  # Função para carregar o arquivo

        # Agora nós podemos acessar os widgets do arquivo XML, caso você tenha
        # alterado o nome de algum widget e não seguiu o tutorial exatamente como
        # eu fiz, preste atenção e utilize o nome que você definiu.
        # Caso não se lembre os nomes abra o arquivo XML no glade novamente e veja
        # os nomes na ávore de widgets do lado direito.
        # Utilizaremos a função get_object passando como parâmetro o nome do widget.

        # Obtendo o widget window1 nossa janela principal
        self.window = builder.get_object("window1")

        # Obtendo o widget text_entry (a área de texto do nosso programa) pois
        # iremos utiliza-la nas funções de inversão da URL e para adicionar o a
        # URL já invertida
        self.text_area = builder.get_object("text_entry")

        # Obtendo o widget about_dialog (janelinha com as informações do programa)
        self.about = builder.get_object("about_dialog")

        # Exibindo a janela do programa
        self.window.show()

        # Agora nós iremos conectar os sinais que definimos para cada widget no
        # Glade Para isso usamos a função connect_signals(). Se você definiu o nome
        # de algum sinal de um modo diferente dos que eu utilizei preste atenção
        # nessa parte e substitua pelo nome que você definiu.

        builder.connect_signals({"gtk_main_quit": gtk.main_quit,
                                 # Sinal da janela principal, conectada a função
                                 # do gtk que fecha o nosso programa
                                 "on_button_invert_clicked": self.invert_url,
                                 # Sinal do botão ao ser clicado, o valor é uma
                                 # função que vamos criar mais a frente no código.
                                 "on_text_entry_activate": self.invert_url,
                                 # Sinal da área de texto ao ser pressionado a tecla
                                 # enter, perceba que utilizamos a mesma função que
                                 # utilizamos no valor do botão, ou seja se o usuário
                                 # clicar no botao ou apertar enter a URL será
                                 # invertida pois os sinais chamam a mesma função de
                                 # inversão.
                                 "on_copy_activate": self.copy_text,
                                 # Sinal do item Copiar do Menu Editar, onde chamamos
                                 # a função que copia o texto para o clipboard do
                                 # sistema. Essa função nós iremos cria-la ainda.
                                 "on_paste_activate": self.paste_text,
                                 # Sinal do item Colar do Menu Editar, com a função
                                 # paste_text que definiremos mais a frente
                                 "on_delete_activate": self.delete_text,
                                 # Sinal do item Excluir do Menu Editar, a função
                                 # delete_text será definida mais a frente.
                                 "on_about_activate": self.about_window,
                                 # Sinal do Item Sobre do Menu Ajuda, a função será
                                 # criado ainda.
                                 })

    # Criando as funções que eu especifiquei como valor no dicionário dos Sinais
    def invert_url(self, widget):
        """Função Principal do programa, irá armazenar a URL que o usuário
        digitar na área de texto e inverte-la"""

        # Usando a variável text_area que contém o widget da área de texto
        # usamos a função get_text() para pegar o texto que o usuário digitar
        # essa é uma função de qualquer instância de um objeto gtk.Entry
        # Veja mais a respeito sobre na documentação oficial no final do Post.
        url = self.text_area.get_text()

        # Invertendo a URL que foi armazenada na variável text
        url = url[::-1]

        # Adicionando a URL já invertida na área de texto, para isso usamos a
        # função set_text() também disponível em objetos do tipo gtk.Entry
        self.text_area.set_text(url)

    def copy_text(self, widget):
        """Função para copiar o valor digitado na área de texto para o
        clipboard do sistema"""

        # Obtendo o acesso ao clipboard do sistema
        clipboard = gtk.clipboard_get()

        # Obtendo a URL digitada na área de texto para que possamos copia-la
        url = self.text_area.get_text()

        # Copiando a URL para o clipboard do sistema
        clipboard.set_text(url)

        # Para que a URL permanceça amazenada no clipboard mesmo depois do
        # programa ser encerrado utilizamos a função store() do gtk.clipboard
        clipboard.store()

    def paste_text(self, widget):
        """Função para colar o texto armazenado no clipboard na área de texto
        do programa"""

        # Obtendo o acesso ao clipboard do sistema
        clipboard = gtk.clipboard_get()

        # Obtendo o texto armazenado no clipboard
        url = clipboard.wait_for_text()

        # Inserindo o texto obtido do clipboard na área de texto do programa
        self.text_area.set_text(url)

    def delete_text(self, widget):
        """Função para apagar qualquer texto que esteja inserido na
        área de texto"""

        # Como queremos apagar qualquer texto que se encontra na área de texto
        # apenas inserimos uma stirng vazia na área de texto
        self.text_area.set_text("")

    def about_window(self, widget):
        """Função para exibir a Janela Sobre do programa"""

        # Executando a Janela Sobre
        self.about.run()

        # Ativando a opção fechar da Janela Sobre
        self.about.hide()


if __name__ == "__main__":
    # Criando uma instância do Programa
    app = InverterApp()

    # Função do GTK que deixa a janela principal do nosso programa em loop para
    # que ela permanceça em execução, sendo encerrada apenas ao chamar a função
    # gtk.main_quit que está configurado no sinal gtk_main_quit, referente ao
    # botão fechar do programa
    gtk.main()