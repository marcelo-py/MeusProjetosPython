from func import *

while True:
    op = int(input(''' \033[1;34m              Opções:
    1 - gerar um CPF aleátorio
    2 - gerar varios CPF's aleátorios
    3 - apagar os CPF's do arquivo de texto
    0 - Sair \033[m'''))

    if op == 1:
        print(cpf_generator())

    elif op == 2:
        quant = int(input("Quantos CPF's aleátorios deseja imprimir? "))
        sn = input('Deseja adciona-los em um arquivo de texto? [S/N]sim/não ')[0].lower()
        resp = False

        if sn == 's':
            resp = True

        cpf_generator(quant, sn=resp)
    elif op == 3:
        apagar_dados()
    elif op == 0:
        break