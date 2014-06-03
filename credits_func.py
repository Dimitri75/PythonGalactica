import pygame
from pygame.locals import *

def credits_print(fenetre):
    pygame.display.set_caption("Galactica - Credits")
    fond_credits = pygame.image.load("images/background.jpg").convert()
    title = pygame.image.load("images/title.png").convert()
    button_back = pygame.image.load("images/back_no_highlight.jpg").convert()
    button_back_h = pygame.image.load("images/back_highlight.jpg").convert()
    fenetre.blit(fond_credits, (0,0))
    fenetre.blit(title, (325,0))
    fenetre.blit(button_back, (700,600))
    back_r = button_back.get_rect()
    back_r.x, back_r.y = 700,600
    pygame.display.flip()
    continuer = 1
    while continuer:
        credits_routine(fenetre)
        for event in pygame.event.get():
            if event.type == pygame.quit:
                continuer = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                #Bouton BACK
                if ( x in range(700, 825)) and (y in range(600,625)):
                    continuer = 0
        if back_r.collidepoint(pygame.mouse.get_pos()):
            fenetre.blit(button_back_h, (700,600))
            pygame.display.flip()



def credits_routine(fenetre):
    fond_credits = pygame.image.load("images/background.jpg").convert()
    title = pygame.image.load("images/title.png").convert()
    button_back = pygame.image.load("images/back_no_highlight.jpg").convert()
    button_back_h = pygame.image.load("images/back_highlight.jpg").convert()
    fenetre.blit(fond_credits, (0,0))
    fenetre.blit(title, (325,0))
    fenetre.blit(button_back, (700,600))
    pygame.display.flip()


    
