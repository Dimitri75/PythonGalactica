import pygame
import json
import os, sys
from pygame.locals import *
from card_loading import *
from game_func import *


def deckSelect_main(fenetre, mode):
    pygame.display.set_caption("Galactica - Choix du Deck")
    fond = pygame.image.load("images/background.jpg").convert()
    button_play = pygame.image.load("images/play_no_highlight.jpg").convert()
    button_play_h = pygame.image.load("images/play_highlight.jpg").convert()
    button_back = pygame.image.load("images/back_no_highlight.jpg").convert()
    button_back_h = pygame.image.load("images/back_highlight.jpg").convert()
    title = pygame.image.load("images/title.png").convert()

    fenetre.blit(fond, (0,0))
    fenetre.blit(title, (325,0))
    fenetre.blit(button_play, (700,550))
    fenetre.blit(button_back, (700,600))
    back_r = button_back.get_rect()
    back_r.x, back_r.y = 700,600
    
    play_r = button_play.get_rect()
    play_r.x, play_r.y = 700,550
    
    
    pygame.display.flip()
    continuer = 1
    selectedDeck = 1
    selectedDeckJ2 = 1
    listfile = os.listdir("decks/decklist/")
    while continuer:
        
        for event in pygame.event.get():
            if event.type == pygame.quit:
                continuer = 0
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = event.pos
                #Bouton PLAY
                if ( x in range(700, 825)) and (y in range(550,579)):
                    if mode == 1 :
                        game_main(fenetre, mode, os.path.splitext(listfile[selectedDeck-1])[0], 'deck_1')
                    elif mode == 0 :
                        game_main(fenetre, mode, os.path.splitext(listfile[selectedDeck-1])[0], os.path.splitext(listfile[selectedDeckJ2-1])[0])
                #Bouton BACK
                if ( x in range(700, 825)) and (y in range(600,629)):
                    continuer = 0
                #Si on clique sur un deck
                i = 0
                for file in listfile:
                    i += 1
                    if (x in range (118,243)) and (y in range(30+(i*45)+10,30+(i*45)+50)):
                        selectedDeck = i
                    elif (x in range (418,543)) and (y in range(30+(i*45)+10,30+(i*45)+50)):
                        selectedDeckJ2 = i
        if back_r.collidepoint(pygame.mouse.get_pos()):
            fenetre.blit(button_back_h, (700,600))
            pygame.display.flip()
        elif play_r.collidepoint(pygame.mouse.get_pos()):
            fenetre.blit(button_play_h, (700,550))
            pygame.display.flip()
        else:
            deckSelect_routine(fenetre, selectedDeck, selectedDeckJ2, mode)
            
                
        pygame.display.flip()
       
def deckSelect_routine(fenetre, selectedDeck, selectedDeckJ2, mode):
    pygame.display.set_caption("Galactica - Choix du Deck")
    fond_deckBuilder = pygame.image.load("images/background.jpg").convert()
    button_play = pygame.image.load("images/play_no_highlight.jpg").convert()
    button_play_h = pygame.image.load("images/play_highlight.jpg").convert()
    button_back = pygame.image.load("images/back_no_highlight.jpg").convert()
    button_back_h = pygame.image.load("images/back_highlight.jpg").convert()
    button_deck = pygame.image.load("images/b_no_highlight.jpg").convert()
    title = pygame.image.load("images/title.png").convert()
    fenetre.blit(fond_deckBuilder, (0,0))
    fenetre.blit(title, (325,0))
    fenetre.blit(button_play, (700,550))
    fenetre.blit(button_back, (700,600))

    #Initialisation de la liste des Decks
    listDeck = {}
    cpt = 0
    cpt2 = 0
    # Style des noms de decks
    white = (255, 255, 255)
    red = (255, 0, 0)
    myfont = pygame.font.SysFont("Arial",30)
    # Liste des fichiers dans le dossier decklist
    listfile = os.listdir("decks/decklist/")
    for file in listfile:
        listDeck = {"id": cpt,"name": os.path.splitext(file)[0] }
        cpt += 1
        cpt2 += 1
        if cpt2 == selectedDeckJ2:
            label2 = myfont.render(listDeck["name"], 1, red)
        else:
            label2 = myfont.render(listDeck["name"], 1, white)
        if cpt == selectedDeck:
            label = myfont.render(listDeck["name"], 1, red)
        else:
            label = myfont.render(listDeck["name"], 1, white)
        if mode == 0:
            fenetre.blit(button_deck, (418,45+(cpt*45)))
            fenetre.blit(label2, (418,30+(cpt*45)+10))
            
        fenetre.blit(button_deck, (118,45+(cpt*45)))
        fenetre.blit(label, (118,30+(cpt*45)+10))
    pygame.display.flip()
