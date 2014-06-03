import pygame
from pygame.locals import *


def options_print(fenetre):
    
    pygame.display.set_caption("Galactica - Options")
    
    fond_credits = pygame.image.load("images/background.jpg").convert()
    title = pygame.image.load("images/title.png").convert()
    button_back = pygame.image.load("images/back_no_highlight.jpg").convert()
    button_back_h = pygame.image.load("images/back_highlight.jpg").convert()
    fullscreen_off = pygame.image.load("images/off_no_highlight.jpg").convert()
    fullscreen_on = pygame.image.load("images/on_highlight.jpg").convert()
    
    fenetre.blit(fond_credits, (0,0))
    fenetre.blit(title, (325,0))
    fenetre.blit(button_back, (700,600))
    
    back_r = button_back.get_rect()
    back_r.x, back_r.y = 700,600

    with open("options.txt") as f:
        options_list = f.readlines()
    if (options_list[0] == "fullscreen_off\n"):
        fenetre.blit(fullscreen_off, (225, 100))
    else:
        fenetre.blit(fullscreen_on, (225,100))
    font = pygame.font.Font(None, 36)
    text = font.render("Full screen :", 1, (255, 255, 255))
    fenetre.blit(text, (75,100))
    
    pygame.display.flip()
    continuer = 1
    while continuer:
        options_routine(fenetre)
        for event in pygame.event.get():
            if event.type == pygame.quit:
                continuer = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                #Bouton BACK
                if ( x in range(700, 925)) and (y in range(600,625)):
                    continuer = 0
                #Bouton Fullscreen ON/OFF
                if ( x in range(225, 350)) and (y in range(100,125)):
                    if (options_list[0] == "fullscreen_off\n"):
                        fenetre = pygame.display.set_mode((960, 720), FULLSCREEN)
                        options_routine(fenetre)
                        options_list[0] = "fullscreen_on"
                    else:
                        fenetre = pygame.display.set_mode((960, 720))
                        options_routine(fenetre)
                        options_list[0] = "fullscreen_off"
                    with open("options.txt", 'w') as f:
                        for s in options_list:
                            f.write(s + '\n')
        if back_r.collidepoint(pygame.mouse.get_pos()):
            fenetre.blit(button_back_h, (700,600))
            pygame.display.flip()



def options_routine(fenetre):
    fond_credits = pygame.image.load("images/background.jpg").convert()
    title = pygame.image.load("images/title.png").convert()
    button_back = pygame.image.load("images/back_no_highlight.jpg").convert()
    button_back_h = pygame.image.load("images/back_highlight.jpg").convert()
    fullscreen_off = pygame.image.load("images/off_no_highlight.jpg").convert()
    fullscreen_on = pygame.image.load("images/on_highlight.jpg").convert()
    fenetre.blit(fond_credits, (0,0))
    fenetre.blit(title, (325,0))
    fenetre.blit(button_back, (700,600))
    font = pygame.font.Font(None, 36)
    text = font.render("Full screen :", 1, (255, 255, 255))
    fenetre.blit(text, (75,100))
    with open("options.txt") as f:
        options_list = f.readlines()
    if (options_list[0] == "fullscreen_off\n"):
        fenetre.blit(fullscreen_off, (225, 100))
    else:
        fenetre.blit(fullscreen_on, (225,100))
    pygame.display.flip()


    
