#para praticar mais não irei nem olhar no codigo nesse repositório que eu fiz para gerar
import random

def gerar_cpf(quant=1, ncpf='', add_arq=False):
    arq = open('./cpfsgerados.txt', 'wt+')
    for _ in range(int(quant)):
        cpf = ''
        digito1 = 0
        digito2 = 0

        full_cpf = ''

        soma = 0
        cont = 10

        if len(ncpf) > 1:
            cpf = ncpf.replace('.', '')[:-3:]
            for n in range(9):
                soma += int(cpf[n]) * cont
                cont -= 1
        
        #gerando um CPF aleatorio
        else:
            for n in range(9):
                gerados = random.choice('01021324354657687989')
                cpf += gerados
                soma += int(gerados)*cont
                cont -= 1

        #definindo o primeiro digito
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

        #definindo o segundo digito
        if 11 - (soma % 11) < 9:
            digito2 = 11 - (soma % 11)

        
        if len(ncpf) > 1:
            if digito1 == int(ncpf[-2]) and digito2 == int(ncpf[-1]):
                return 'O CPF é Valido!'
            else:
                return 'O CPF não é Valido!'

        cont = 0
        #deixando em formado de CPF
        for c in cpf:
            if cont == 3:
                full_cpf += '.'
                cont -= 3
            full_cpf += c
            cont += 1
        full_cpf = full_cpf+'-'+str(digito1)+str(digito2)
        if add_arq:
            arq.write(f'{full_cpf}\n')
        
        yield full_cpf
    arq.close()

