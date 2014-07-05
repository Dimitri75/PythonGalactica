import pygame

from pygame.locals import *
from deckSelect import *


#Choix du Mode:
def mode_choice(fenetre):
    pygame.display.set_caption("Galactica - Choix du mode de jeu")

    fond = pygame.image.load("images/background.jpg").convert()
    title = pygame.image.load("images/title.png").convert()
    button_1j = pygame.image.load("images/mode1j_no_highlight.jpg").convert()
    button_1j_h = pygame.image.load("images/mode1j_highlight.jpg").convert()
    button_2j = pygame.image.load("images/mode2j_no_highlight.jpg").convert()
    button_2j_h = pygame.image.load("images/mode2j_highlight.jpg").convert()
    button_back = pygame.image.load("images/back_no_highlight.jpg").convert()
    button_back_h = pygame.image.load("images/back_highlight.jpg").convert()
    
    mode1j = button_1j.get_rect()
    mode1j.x, mode1j.y = 418, 173
    mode2j = button_2j.get_rect()
    mode2j.x, mode2j.y = 418, 222
    back_r = button_back.get_rect()
    back_r.x, back_r.y = 700,600
    
    fenetre.blit(fond, (0,0))
    fenetre.blit(title, (325,0))
    fenetre.blit(button_1j, (418,173))
    fenetre.blit(button_2j, (418,222))
    fenetre.blit(button_back, (700,600))
    pygame.display.flip()

    continuer = 1

    while continuer:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                continuer = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                #Bouton MODE 1 JOUEUR
                if ( x in range(418,543)) and (y in range (173,202)):
                    deckSelect_main(fenetre, 1)
                #Bouton MODE 2 JOUEURS
                elif ( x in range(418,543)) and (y in range (222,251)):
                    deckSelect_main(fenetre, 0)
                #Bouton BACK
                elif ( x in range(700, 825)) and (y in range(600,625)):
                    continuer = 0

        if mode1j.collidepoint(pygame.mouse.get_pos()):
            fenetre.blit(button_1j_h, (418,173))
            pygame.display.flip()
        elif back_r.collidepoint(pygame.mouse.get_pos()):
            fenetre.blit(button_back_h, (700,600))
            pygame.display.flip()
        elif mode2j.collidepoint(pygame.mouse.get_pos()):
            fenetre.blit(button_2j_h, (418,222))
            pygame.display.flip()
        else:
            mode_choice_routine(fenetre)

def mode_choice_routine(fenetre):
    fond = pygame.image.load("images/background.jpg").convert()
    title = pygame.image.load("images/title.png").convert()
    button_1j = pygame.image.load("images/mode1j_no_highlight.jpg").convert()
    button_2j = pygame.image.load("images/mode2j_no_highlight.jpg").convert()
    button_back = pygame.image.load("images/back_no_highlight.jpg").convert()
    fenetre.blit(fond, (0,0))
    fenetre.blit(title, (325,0))
    fenetre.blit(button_1j, (418,173))
    fenetre.blit(button_2j, (418,222))
    fenetre.blit(button_back, (700,600))
    pygame.display.flip()
