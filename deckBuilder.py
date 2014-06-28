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
    while continuer:
        deckBuilder_routine(fenetre)
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
                    deckModify(fenetre, "dim_deck")

                #BOUTON DELETE
                if (x in range (700, 825)) and (y in range(550, 579)):
                    print('DELETE')    

        #Initialisation de la liste des Decks
        listDeck = {}
        cpt = 0
        # Style des noms de decks
        red = (255, 255, 255)
        myfont = pygame.font.SysFont("Arial",30)
        # Liste des fichiers dans le dossier decklist
        listfile = os.listdir("decks/decklist/")
        for file in listfile:
            listDeck = {"id": cpt,"name": os.path.splitext(file)[0] }
            cpt += 1
            label = myfont.render(listDeck["name"], 1, red)
            fenetre.blit(label, (40,30+(cpt*45)+10))
            # Si l'on passe la souris sur le label alors ...
            #if listDeck.get_rect().collipoint(pygame.mouse.get_pos()):
                
            #print(listDeck)
            pygame.display.flip()
            #print(os.path.splitext(file)[0])
        #Recuperation des donnees Json des fichier
        with open("decks/decklist/deck_base.json") as json_file:
            json_data = json.load(json_file)
            pygame.display.flip()
            #Affiche le tableau de valeurs
            #print(json_data)
def deckBuilder_routine(fenetre):
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
