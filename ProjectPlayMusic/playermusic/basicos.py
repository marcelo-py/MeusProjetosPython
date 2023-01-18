import PySimpleGUI as sg
import os
import controle
import save_config
from pygame.mixer import music
from threading import Thread
from time import sleep


class PlayMusic:
    path = []
    musicas = []

    def diretorio_musica(self, nome):
        return self.path[self.musicas.index(nome)]+'/'+nome

    def somentemusica(self, musica, v=0):  # v -> -1 volta uma musica, 0 apenas reproduz a atual, 1/+1 pula uma musica
        return self.musicas[self.musicas.index(musica)+v]


class ListMusics(PlayMusic):
    def buscar_musicas(self):
        for r, p, a in os.walk('/home/marcelo'):
            for musica in a:
                if musica[-4:] in '.mp3':
                    self.path.append(r)
                    self.musicas.append(musica)


volume_set = save_config.consult_config()['volume']
musica_selecionada = save_config.consult_config()['ultima_musica']
state_icon = '▶'
list_music = ListMusics()
list_music.buscar_musicas()


time = 0

tela_fechou = False
play = False


def time_music():
    while True:
        try:
            while music.get_busy():
                global time
                time += 1

                if tela_fechou:
                    break
                sleep(1)
            if play:
                time = 0
        except Exception:
            pass

        if tela_fechou:
            break


def layout1():
    layout = [
        [sg.Button('<Musicas'), sg.Push()],
        [sg.Text(musica_selecionada, key='musicaatual')],
        [sg.Image('arquivos/imagens/logo.png', size=(250, 250))],
        [
            sg.Text('00:00', key='progresstime'),
            sg.Text('lllı.'), sg.Slider((0, 100), size=(20, 10), key='volume',
                                        enable_events=True, disable_number_display=True,
                                        orientation='h', default_value=volume_set)],
        [
            sg.Button('<<'), sg.Button('<-', key='anterior'),
            sg.Button('▶', key='playpause'),
            sg.Button('->', key='proximo'), sg.Button('>>', key='avancar'),
        ],
    ]
    return sg.Window('Music Player', layout, element_justification='center', finalize=True)


def layout2(musicas):
    layout = [
        [sg.Listbox(musicas, size=(40, 15), enable_events=True, key='-MUSICLIST-')],
        [sg.Button(musica_selecionada, key='musicaatual')],
        [
            sg.Text('00:00', key='progresstime'),
            sg.Button('<<'), sg.Button('<-', key='anterior'),
            sg.Button(state_icon, key='playpause'),
            sg.Button('->', key='proximo'), sg.Button('>>', key='avancar'),
        ],
    ]
    return sg.Window('Music Player', layout, element_justification='center', finalize=True)


janela1, janela2 = layout1(), None


Thread(target=time_music).start()

while True:
    window, event, value = sg.read_all_windows(timeout=500)
    if event == sg.WINDOW_CLOSED:
        tela_fechou = True
        break

    if window == janela1 and event == '<Musicas':
        janela2 = layout2(list_music.musicas)
        janela1.hide()

    if window == janela2 and event == 'musicaatual':
        janela2.hide()
        janela1.un_hide()

    if event == '-MUSICLIST-':
        musica_selecionada = value['-MUSICLIST-'][0]
        controle.carregar_musica(list_music.diretorio_musica(musica_selecionada))
        janela1['playpause'].update('||')
        janela2['playpause'].update('||')
        time = 0

        play = True

    if window == janela2 and event == '-MUSICLIST-':
        janela1['musicaatual'].update(musica_selecionada)
        janela2['musicaatual'].update(musica_selecionada)

    if event == 'playpause':
        if play:
            controle.pause()
            state_icon = '▶'
            janela1['playpause'].update(state_icon)
            try:
                janela2['playpause'].update(state_icon)
            except TypeError:
                pass
            play = False
        else:
            state_icon = '||'
            controle.play()
            janela1['playpause'].update(state_icon)
            try:
                janela2['playpause'].update(state_icon)
            except TypeError as erro:
                print(erro)

            play = True
    if event == 'proximo':
        musica_selecionada = list_music.somentemusica(musica_selecionada, +1)
        controle.carregar_musica(list_music.diretorio_musica(musica_selecionada))

        state_icon = '||'
        controle.play()
        janela1['playpause'].update(state_icon)
        janela1['musicaatual'].update(musica_selecionada)
        controle.conf_volume(volume_set)
        time = 0
        try:
            janela2['playpause'].update(state_icon)
            janela2['musicaatual'].update(musica_selecionada)
        except TypeError:
            pass
    if event == 'avancar':
        time += 10
        controle.avancar(time)

    if event == 'volume':
        volume_set = value['volume']
        controle.conf_volume(volume_set)

    if controle.musica_tocando() != 'musica_nao_carregada' and not controle.musica_tocando() and play:
        musica_selecionada = list_music.somentemusica(musica_selecionada, +1)
        controle.carregar_musica(list_music.diretorio_musica(musica_selecionada))
        janela1['musicaatual'].update(musica_selecionada)
        try:
            janela2['musicaatual'].update(musica_selecionada)
        except TypeError:
            pass

    if time > 0:
        janela1['progresstime'].update(f'{int(time//60):0>2}:{int(time%60):0>2}')
        try:
            janela2['progresstime'].update(f'{int(time//60):0>2}:{int(time%60):0>2}')
        except Exception as erro:
            print(erro)
            
save_config.save_config(musica_selecionada, volume_set, list_music.diretorio_musica(musica_selecionada))
