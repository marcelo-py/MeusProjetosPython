#É apenas um movimento, mas da para ir mais adiante
xadrez = [[['TB'], ['CB'], ['BB'], ['KB'], ['RB'], ['BB'], ['CB'], ['TB']],
          [['PB'], ['PB'], ['PB'], ['PB'], ['PB'], ['PB'], ['PB'], ['PB']],
          [['  '], ['  '], ['  '], ['  '], ['  '], ['  '], ['  '], ['  ']],
          [['  '], ['  '], ['  '], ['  '], ['  '], ['  '], ['  '], ['  ']],
          [['  '], ['  '], ['  '], ['  '], ['  '], ['  '], ['  '], ['  ']],
          [['  '], ['  '], ['  '], ['  '], ['  '], ['  '], ['  '], ['  ']],
          [['PP'], ['PP'], ['PP'], ['PP'], ['PP'], ['PP'], ['PP'], ['PP']],
          [['TP'], ['CP'], ['BP'], ['KP'], ['RP'], ['BP'], ['CP'], ['TP']]]


jogador1 = input('Nome do jogador: ')
print('Jogada de {}'.center(50).format(jogador1))
print('-'*50)
print('     0     1     2     3     4     5     6     7') #representa as colunas
for n, linha in enumerate(xadrez):
    print(n, end=' ')
    for q in linha:
        print(q, end='')
    print()

jogada1_l = int(input('Selecione a linha que está a peça: '))
jogada1_c = int(input('Qual coluna? '))
print('Peça {} selecionada'.format(xadrez[jogada1_l][jogada1_c]))
mover_l = int(input('escolha a linha para onde quer mover a peça '))
mover_c = int(input('escolha a coluna para onde quer mover '))

xadrez[jogada1_l][jogada1_c].append(xadrez[mover_l][mover_c][0]) #adicionando a peça do destino da que sera movida no mesmo lugar da mesma

xadrez[mover_l][mover_c][0] = xadrez[jogada1_l][jogada1_c][0] #fiz com que o conteudo da lista, ou seja o valor, se tornasse a peça que seria movida

#até então a peça que seria movida esta junto com a que deveria ficar no lugar dela então a peça que deve ser movida deve ser apagada
del xadrez[jogada1_l][jogada1_c][0]#apagando a peça que deveria ter sido movida

xadrez[mover_l][mover_c] = '\033[1;32m{}\033[m'.format(xadrez[mover_l][mover_c]) #a peça que sera mexida será representada pela cor amarela
xadrez[jogada1_l][jogada1_c] = '\033[1;35m{}\033[m'.format(xadrez[jogada1_l][jogada1_c])# a peça que foi pro lugar da outra sera a roxa

print('='*50)
print('     0     1     2     3     4     5     6     7')#representa as colunas
for n, linha in enumerate(xadrez):
    print(n, end=' ')
    for q in linha:
        print(q, end='')
    print()
