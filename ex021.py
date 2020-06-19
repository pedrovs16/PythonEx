import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('musicex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
print('Feito')
