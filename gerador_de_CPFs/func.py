from random import randint

def arquivo_existe(arq):
    try:
        a = open(arq, 'rt')
        a.close()

    except FileNotFoundError:
        return False

    else:
        return True

def cpf_generator(q=1, sn=False):
    nome_arquivo = 'cpfsgerados.txt'

    if not arquivo_existe(nome_arquivo):
        a = open(nome_arquivo, 'wt+')
        a.close()
        print(nome_arquivo, 'criado com sucesso!')

    l = open(nome_arquivo, 'at')

    for p in range(q):

        numeros = []
        for c in range(1, 10):
            random = randint(0, 9)
            numeros.append(random)

        cpf = ''

        soma = 0
        soma2 = 0
        for c, i in zip(numeros, [n for n in range(10, 1, -1)]):
            soma += c * i

        primeiro_digito = soma % 11
        primeiro_digito = 11 - primeiro_digito

        if primeiro_digito > 9:
            primeiro_digito = 0

        numeros.append(primeiro_digito)

        for c, i in zip(numeros, [n for n in range(11, 1, -1)]):
            soma2 += c * i

        segundo_digito = soma2 % 11
        segundo_digito = 11 - segundo_digito

        if segundo_digito > 9:
            segundo_digito = 0

        numeros.append(segundo_digito)

        cont = 0
        contd = 0

        for n in numeros:
            cpf += str(n)
            cont += 1

            if cpf.count('.') == 2:
                contd += 1
                if contd == 3:
                    cpf += '-'

            if cont == 3 and cpf.count('.') < 2:
                cpf += '.'
                cont -= 3
        print(cpf)

        if sn:
            l.write('{}\n'.format(cpf))

    if sn:
        print("CPF's adicionados ao arquivo de texto(ou não kk)")

    l.close()

def apagar_dados():
    try:
        with open('cpfsgerados.txt', 'w') as f:
            f.truncate()
            pass
    except FileNotFoundError:
        print('Erro! o Aquivo de texto ainda não existe!')
    else:
        print('Dados apagados')