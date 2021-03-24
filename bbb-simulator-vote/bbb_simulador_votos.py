from random import choice

participantes = ['Carla', 'Gil', 'Juliete', 'Projota', 'Rodolfo', 'Sara']
na_reta = ['Carla', 'Gil', 'Juliete', 'Rodolfo', 'Sara']
print('Todos os participantes')
print('-'*25)
print('cod.| Part.')
for i, p in enumerate(participantes):
    print(i, p)
liderescolhe_p = choice(na_reta)
liderescolhe_a = choice(na_reta)
print('OBS: Projota é o líder')
print('Projota indica {} direto para o paredão e {} para ser o anjo'.format(liderescolhe_p, liderescolhe_a))
paredao = []
maisvotado = []
for c in range(0, len(na_reta)):
    vota = int(input('Em quem {} deve votar?(digite o codigo do participante): '.format(na_reta[c])))
    while vota > len(participantes):
        print('digite uma opção valida !!!')
        vota = int(input('Em quem {} deve votar?(digite o codigo do participante): '.format(na_reta[c])))
    while participantes[vota] == liderescolhe_a or participantes[vota] == participantes[3]:
        print('Atenção! {} não pode ser indicado ao paredão, pois é anjo ou líder!'.format(participantes[vota]))
        vota = int(input('Em quem {} deve votar?(digite o codigo do participante): '.format(na_reta[c])))
        while vota > len(participantes[-1]):
            print('digite uma opção valida!!!')
            vota = int(input('Em quem {} deve votar?(digite o codigo do participante): '.format(na_reta[c])))
    paredao.append(participantes[vota])
    maisvotado.append(str(vota))
    print('-'*50)

print('O mais votado para o paredão foi ')
if maisvotado.count('0') > maisvotado.count('1') and maisvotado.count('2') and maisvotado.count('3'):
    print(paredao[0])
elif maisvotado.count('1') > maisvotado.count('0') and maisvotado.count('2') or maisvotado.count('3'):
    print(paredao[1])
elif maisvotado.count('2') > maisvotado.count('0') and maisvotado.count('1') and maisvotado.count('3'):
    print(paredao[2])
else:
    print(paredao[3])