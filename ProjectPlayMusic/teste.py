'''import os
import pygame

pygame.init()

path = []
musicas = []

for root, pasta, arq in os.walk('/'):
    for musica in arq:
        if musica[-4:] == '.mp3':
            path.append(root)
            musicas.append(musica)

"""pygame.mixer.init()
pygame.mixer.music.load(path[20]+'/'+musicas[20])
pygame.mixer.music.play()
input()"""
print(path)
print(musicas)
'''
