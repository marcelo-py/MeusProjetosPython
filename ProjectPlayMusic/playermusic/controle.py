import pygame
import save_config

pygame.init()


def carregar_musica(m):
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(m)
        pygame.mixer.music.play()
        conf_volume(save_config.consult_config()['volume'])
        print('Tocando', m)

    except Exception as ex:
        print('Erro ao tentar carregar a musica!', ex)


def pause():
    try:
        pygame.mixer.music.pause()
    except pygame.error as erro:
        print('pause erro: ', erro)


def play(m=save_config.consult_config()['musica_e_diretorio']):
    try:
        pygame.mixer.music.unpause()
    except pygame.error:
        carregar_musica(m)


def proxima(m):
    carregar_musica(m)


def anterior(m):
    carregar_musica(m)


def musica_tocando():
    try:
        if pygame.mixer.music.get_busy():
            return True
        else:
            return False
    except pygame.error:
        return 'musica_nao_carregada'


def avancar(t):
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.set_pos(t)


def conf_volume(v=save_config.consult_config()['volume']):
    try:
        pygame.mixer.music.set_volume(v/100)
    except:
        pass


pygame.quit()
