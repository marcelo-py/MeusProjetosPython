#para praticar mais não irei nem olhar no codigo que eu fiz para gerar nesse repositorio
import random

cpf = ''
digito1 = 0
digito2 = 0

full_cpf = ''

soma = 0

cont = 10
for n in range(9):
    gerados = random.choice('01021324354657687989')
    cpf += gerados
    soma += int(gerados)*cont
    cont -= 1


if 11 - (soma % 11) < 9:
    digito1 = 11 - (soma % 11)

soma = 0
cont = 11

for n in range(10):
    if cont == 2:
        soma += digito1 * cont
        break
    soma += int(cpf[n]) * cont
    cont -= 1

if 11 - (soma % 11) < 9:
    digito2 = 11 - (soma % 11)


cont = 0

for c in cpf:
    if cont == 3:
        full_cpf += '.'
        cont -= 3
    full_cpf += c
    cont += 1
full_cpf = full_cpf+'-'+str(digito1)+str(digito2)
print(full_cpf)

