import pygame
import json
import os, sys
from pygame.locals import *
from card_loading import *

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
    pygame.display.flip()
    listDeck = {}
    cpt = 0
    yellow = (255, 255, 0)
    myfont = pygame.font.SysFont("Comic Sans MS", 30)
    listfile = os.listdir("decks/decklist/")
    for file in listfile:
        listDeck = {"id": cpt,"name": os.path.splitext(file)[0] }
        cpt += 1
        label = myfont.render(listDeck["name"], 1, yellow)
        fenetre.blit(label, (400,300+(cpt*45)+10))
        pygame.display.flip()
        print(listDeck)
        #print(os.path.splitext(file)[0])
    with open("decks/decklist/deck_base.json") as json_file:
        json_data = json.load(json_file)
        #Affiche le tableau de valeurs
        #print(json_data)
    
    continuer = 1
    while continuer:
        continuer +=1
        if continuer > 500:
            continuer = 0