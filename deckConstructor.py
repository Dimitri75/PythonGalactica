import pygame
from card_loading import *
from pygame.locals import *
import json
#import nomDuFichier import *

def deckModify(deck_name):
    W=960
    H=720
    pygame.init()

    #Ouverture de la fenêtre Pygame
    fenetre = pygame.display.set_mode((W, H))

    #Chargement et collage du fond
    fond = pygame.image.load("images/background.jpg").convert()
    fenetre.blit(fond, (0,0))

    #AFFICHAGE DECK
    deck = print_deck(fenetre, deck_name)

    #DEBUT AFFICHAGE CARDLIST
    
    #CHOIX FONT POUR TITRE
    myfont = pygame.font.Font(None, 35)

    #AFFICHAGE TITRE
    text = [myfont.render("Liste des cartes", True, [185,169,255], None)]
    my_image = text[0]
    rect = my_image.get_rect()
    rect.center = [(W-(W/5)), 13]
    fenetre.blit(my_image, rect)

    #CHANGEMENT FONT POUR LISTE
    myfont = pygame.font.SysFont("Consolas", 20)

    #Chargement liste des cartes
    json_data = open('decks/card_list.json')
    data = json.load(json_data)
    json_data.close()

    for i in range(0,len(data)):
        fond_carte = pygame.image.load("images/bg_cardList.png").convert_alpha()
        fenetre.blit(fond_carte, ((W-(W/5)-105), (40+i*23)-11))

        #COST
        text = [myfont.render(str(data[i]["Cost"]), True, [0,0,0], None)]
        my_image = text[0]
        rect = my_image.get_rect()
        rect.center = [(W-(W/5)-95), (40+i*23)]
        fenetre.blit(my_image, rect)

        #NAME
        text = [myfont.render(data[i]["name"], True, [255,255,255], None)]
        my_image = text[0]
        rect = my_image.get_rect()
        rect.center = [(W-(W/5)), (40+i*23)]
        fenetre.blit(my_image, rect)
    
    #Rafraîchissement de l'écran
    pygame.display.flip()

    #BOUCLE INFINIE
    continuer = 1

    while continuer:
        #reload(fenetre,x)
        for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
            if event.type == QUIT:     #Si un de ces événements est de type QUIT
                continuer = 0      #On arrête la boucle
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    x,y = event.pos
                    for i in range(0,len(deck)):
                        if (x in range(int((W/5)-104),int((W/5)+104))) and (y in range (40+(i*23-10),40+(i*23+10))):
                            print("\nLa carte "+deck[i]["name"]+" doit être retirée du deck.")

                    for i in range(0,len(data)):
                        if (x in range(int(W-(W/5)-104),int(W-(W/5)+104))) and (y in range (40+(i*23-10),40+(i*23+10))):
                            print("\nS'il y a moins de 30 cartes dans le deck: ")
                            print("La carte "+data[i]["name"]+" doit être ajoutée au deck.")
                        

    pygame.quit()

def reload(fenetre, x):
    pygame.display.flip()

def print_deck(fenetre, deck_name):
    W=fenetre.get_width()
    H=fenetre.get_height()
    
    #Choix police
    myfont = pygame.font.SysFont(None, 35)

    #Affichage nom du deck
    text = [myfont.render(deck_name, True, [185,169,255], None)]
    my_image = text[0]
    rect = my_image.get_rect()
    rect.center = [W/5, 13]
    fenetre.blit(my_image, rect)

    #Changement font pour liste
    myfont = pygame.font.SysFont("Consolas", 20)
    
    deck = load_deck(deck_name)

    
    for i in range(0,len(deck)):
        fond_carte = pygame.image.load("images/bg_cardList.png").convert_alpha()
        fenetre.blit(fond_carte, (W/5-105, (40+i*23)-11))

        #COST
        text = [myfont.render(str(deck[i]["Cost"]), True, [0,0,0], None)]
        my_image = text[0]
        rect = my_image.get_rect()
        rect.center = [((W/5)-95), (40+i*23)]
        fenetre.blit(my_image, rect)
        
        #NAME
        text = [myfont.render(deck[i]["name"], True, [255,255,255], None)]
        my_image = text[0]
        rect = my_image.get_rect()
        rect.center = [W/5, (40+i*23)]
        fenetre.blit(my_image, rect)

    return deck