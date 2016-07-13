opcao = 'Y'
x = 1
while(opcao == 'Y' or opcao == 'y'):
    print 'O while rodou', x, 'vezes'
    x += 1
    opcao = raw_input('Deseja continuar?')
print 'Acabou o while'
