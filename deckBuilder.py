import pygame
import json
import os, sys
from pygame.locals import *
from card_loading import *
from deckConstructor import *

def deckBuilder_main(fenetre):
    pygame.display.set_caption("Galactica - Deck Builder")
    fond_deckBuilder = pygame.image.load("images/background.jpg").convert()
    button_modify = pygame.image.load("images/modify_no_highlight.jpg").convert()
    button_modify_h = pygame.image.load("images/modify_highlight.jpg").convert()
    button_delete = pygame.image.load("images/delete_no_highlight.jpg").convert()
    button_delete_h = pygame.image.load("images/delete_highlight.jpg").convert()
    button_create = pygame.image.load("images/create_no_highlight.jpg").convert()
    button_create_h = pygame.image.load("images/create_highlight.jpg").convert()
    button_back = pygame.image.load("images/back_no_highlight.jpg").convert()
    button_back_h = pygame.image.load("images/back_highlight.jpg").convert()
    title = pygame.image.load("images/title.png").convert()

    fenetre.blit(fond_deckBuilder, (0,0))
    fenetre.blit(title, (325,0))
    fenetre.blit(button_create, (700,450))
    fenetre.blit(button_modify, (700,500))
    fenetre.blit(button_delete, (700,550))
    fenetre.blit(button_back, (700,600))
    back_r = button_back.get_rect()
    back_r.x, back_r.y = 700,600
    
    create_r = button_create.get_rect()
    create_r.x, create_r.y = 700,450
    
    modify_r = button_modify.get_rect()
    modify_r.x, modify_r.y = 700,500
    
    delete_r = button_delete.get_rect()
    delete_r.x, delete_r.y = 700,550
    
    pygame.display.flip()
    continuer = 1
    selectedDeck = 1
    listfile = os.listdir("decks/decklist/")
    while continuer:
        
        for event in pygame.event.get():
            if event.type == pygame.quit:
                continuer = 0
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = event.pos
                #Bouton BACK
                if ( x in range(700, 825)) and (y in range(600,629)):
                    continuer = 0

                #BOUTON CREATE
                if (x in range (700, 825)) and (y in range(450, 479)):
                    print('CREATE')

                #BOUTON MODIFY
                if (x in range (700, 825)) and (y in range(500, 529)):
                    deckModify(fenetre, os.path.splitext(listfile[selectedDeck-1])[0])

                #BOUTON DELETE
                if (x in range (700, 825)) and (y in range(550, 579)):
                    print('DELETE')
                #Si on clique sur un deck
                i = 0
                for file in listfile:
                    i += 1
                    if (x in range (40,150)) and (y in range(30+(i*45)+10,30+(i*45)+70)):
                        selectedDeck = i
        if back_r.collidepoint(pygame.mouse.get_pos()):
            fenetre.blit(button_back_h, (700,600))
            pygame.display.flip()
        elif create_r.collidepoint(pygame.mouse.get_pos()):
            fenetre.blit(button_create_h, (700,450))
            pygame.display.flip()
        elif modify_r.collidepoint(pygame.mouse.get_pos()):
            fenetre.blit(button_modify_h, (700,500))
            pygame.display.flip()
        elif delete_r.collidepoint(pygame.mouse.get_pos()):
            fenetre.blit(button_delete_h, (700,550))
            pygame.display.flip()
        else:
            deckBuilder_routine(fenetre, selectedDeck)
            
                
        pygame.display.flip()
       
def deckBuilder_routine(fenetre, selectedDeck):
    pygame.display.set_caption("Galactica - Deck Builder")
    fond_deckBuilder = pygame.image.load("images/background.jpg").convert()
    button_modify = pygame.image.load("images/modify_no_highlight.jpg").convert()
    button_modify_h = pygame.image.load("images/modify_highlight.jpg").convert()
    button_delete = pygame.image.load("images/delete_no_highlight.jpg").convert()
    button_delete_h = pygame.image.load("images/delete_highlight.jpg").convert()
    button_create = pygame.image.load("images/create_no_highlight.jpg").convert()
    button_create_h = pygame.image.load("images/create_highlight.jpg").convert()
    button_back = pygame.image.load("images/back_no_highlight.jpg").convert()
    button_back_h = pygame.image.load("images/back_highlight.jpg").convert()
    button_deck = pygame.image.load("images/b_no_highlight.jpg").convert()
    title = pygame.image.load("images/title.png").convert()
    fenetre.blit(fond_deckBuilder, (0,0))
    fenetre.blit(title, (325,0))
    fenetre.blit(button_create, (700,450))
    fenetre.blit(button_modify, (700,500))
    fenetre.blit(button_delete, (700,550))
    fenetre.blit(button_back, (700,600))

    #Initialisation de la liste des Decks
    listDeck = {}
    cpt = 0
    # Style des noms de decks
    white = (255, 255, 255)
    red = (255, 0, 0)
    myfont = pygame.font.SysFont("Arial",30)
    # Liste des fichiers dans le dossier decklist
    listfile = os.listdir("decks/decklist/")
    for file in listfile:
        listDeck = {"id": cpt,"name": os.path.splitext(file)[0] }
        cpt += 1
        fenetre.blit(button_deck, (40,45+(cpt*45)))
        if cpt == selectedDeck:
            label = myfont.render(listDeck["name"], 1, red)
        else:
            label = myfont.render(listDeck["name"], 1, white)
        fenetre.blit(label, (40,30+(cpt*45)+10))
    pygame.display.flip()
