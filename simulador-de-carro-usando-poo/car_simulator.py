from playsound import playsound

class Carro:
    def __init__(self):
        self.abrir_porta = None
        self.entrar_carro = None
        self.ligar_carro = None
        self.carro_andar = None
        self.tocar_musica = None
        self.fechar_carro = None


    def abrir(self):
        if self.abrir_porta:
            print('As portas já estão abertas! ')
            return
        print('Portas abertas!')
        self.abrir_porta = True
        self.fechar_carro = False


    def fechar(self):
        if self.fechar_carro:
            print('O carrro já está com as portas fechadas!')
            return

        print('O carro está com as portas fechadas')
        self.fechar_carro = True
        self.abrir_porta = False


    def entrar(self):
        if not self.abrir_porta:
            print('Para entrar você precisa abrir a porta primeiro')
            return

        print('Você entrou no carro e está dentro dele!')
        self.entrar_carro = True


    def ligar(self):
        if not self.entrar_carro:
            print('A porta não está aberta ou você não está dentro do carro para liga-lo')
            return
        if not self.entrar_carro:
            print('Você precisa está dentro do carro para liga-lo')
            return
        print('O Carro esta ligado')
        self.ligar_carro = True

    def andar(self):
        if not self.entrar_carro:
            print('Você precisa entrar no carro e ligar ele primeiro')
            return
        if not self.ligar_carro:
            print('O carro precisa está ligado para andar')
            return


        print('O carro está andando')
        self.carro_andar = True
    def tocarmusica(self, t=''):
        if len(t) == 0:
            print('Você precisa selecionar uma musica!')
        if not self.entrar_carro:
            print('O carro precisa está com a porta aberta para você entrar nele e por a música')
            return

        if not self.entrar_carro:
            print('Você precisa entrar no carro para colocar a música')
            return

        try:
            if len(t.strip()) >= 1:
                print('O som do carro está tocando: \033[32m{}\033[m...'.format(t))
                print('''                 ¬__----___
                ¨O------O--¬''')
                playsound(t)
        except:
            print('Erro ao tocar música')
        finally:
            print('A música parou de tocar!')
    

#Programa principal
c = Carro()
while True:
    print('\033[1;35m='*38)
    print('{:^38}'.format('Opções do que fazer com seu carro'))
    print('='*38)
    try:
        op = int(input('''        1 - Abrir porta
        2 - Entrar
        3 - Fechar portas
        4 - Ligar
        5 - Andar
        6 - Tocar música
    (digite 000 para sair )\033[1;34m=>>\033[m'''))
        print('\033[1;35m~\033[m'*38)

    except ValueError:
        print('\033[1;33mErro!\033[m Por favor digite um número correto!')
        
    else:
        if op == 1:
            c.abrir()
        elif op == 2:
            c.entrar()
        elif op == 3:
            c.fechar()
        elif op == 4:
            c.ligar()
        elif op == 5:
            c.andar()
        elif op == 6:
            c.tocarmusica('DEAF KEV - Invincible[NCS].mp3')  # Coloque a música na pasta junto com o programa e coloque o nome dela entre aspas alterando a musica atual, ex: 'musica.mp3'
            continue
        elif op > 5 or op != 000:
            print('\033[1;31mErro!\033[m Digite uma opção válida!')
        if op == 000:
            break
print('Até logo!')
