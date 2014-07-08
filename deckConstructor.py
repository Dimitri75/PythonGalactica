import pygame
from card_loading import *
from pygame.locals import *
import json
#from nomDuFichier import *

def deckModify(fenetre, deck_name):
    W=960
    H=720
    
    deck = reload(fenetre, deck_name)
    data = load_card_list()
    
    #BOUCLE INFINIE
    continuer = 1

    while continuer:
        for event in pygame.event.get():   #On parcours la liste de tous les evenements recus
            if event.type == QUIT:     #Si un de ces evenements est de type QUIT
                continuer = 0      #On arrete la boucle
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    x,y = event.pos
                    if (x in range(int((W/2)-100),int((W/2)+100))) and (y in range (int(H - (H/8)-61), int(H - (H/8))+61)):
                        continuer = 0
                    for i in range(0,len(deck)):
                        if (x in range(int((W/5)-104),int((W/5)+104))) and (y in range (40+(i*23-10),40+(i*23+10))):
                            print("\nLa carte "+deck[i]["name"]+" vient d'etre retiree du deck.")
                            deck.remove(deck[i])
                            with open ("decks/decklist/"+deck_name+".json", "w") as f:
                                json.dump(deck, f)
                                f.close()
                            deck = reload(fenetre, deck_name)

                    for i in range(0,len(data)):
                        if (x in range(int(W-(W/5)-104),int(W-(W/5)+104))) and (y in range (40+(i*23-10),40+(i*23+10))):
                            if(len(deck)<30) and not(is_rarityMax_in_deck(deck, data[i]["name"])):
                                deck.append(data[i])
                                with open ("decks/decklist/"+deck_name+".json", "w") as f:
                                    json.dump(deck, f)
                                    f.close()
                                print("\nLa carte "+data[i]["name"]+" vient d'etre ajoutee au deck.")
                                deck = reload(fenetre, deck_name)
                                

def reload(fenetre, deck_name):
    W=960
    H=720

    #Chargement et collage du fond
    fond = pygame.image.load("images/background.jpg").convert()
    fenetre.blit(fond, (0,0))

    #AFFICHAGE DECK
    deck = print_deck(fenetre, deck_name)

    #DEBUT AFFICHAGE CARDLIST
    
    #CHOIX FONT POUR TITRE
    myfont = pygame.font.Font(None, 35)

    #AFFICHAGE TITRE
    text = [myfont.render("Liste des cartes", True, [185,169,255])]
    my_image = text[0]
    rect = my_image.get_rect()
    rect.center = [(W-(W/5)), 13]
    fenetre.blit(my_image, rect)

    #AFFICHAGE BACK BUTTON
    back_button = pygame.image.load("images/back_button.png").convert_alpha()
    fenetre.blit(back_button, ((W/2)-100, (H - (H/8))-61))

    #CHANGEMENT FONT POUR LISTE
    myfont = pygame.font.SysFont("Consolas", 20)

    data = load_card_list()

    for i in range(len(data)):
        fond_carte = pygame.image.load("images/bg_cardList.png").convert_alpha()
        fond_rarity = pygame.image.load("images/bg_"+rarity_to_string(data[i]["Rarity"])+".png").convert()
        fenetre.blit(fond_carte, ((W-(W/5)-105), (40+i*23)-11))
        fenetre.blit(fond_rarity, (W-(W/5)-105+(208-7), (40+i*23)-11))

        #COST
        text = [myfont.render(str(data[i]["Cost"]), True, [0,0,0])]
        my_image = text[0]
        rect = my_image.get_rect()
        rect.center = [(W-(W/5)-95), (40+i*23)]
        fenetre.blit(my_image, rect)

        #NAME
        text = [myfont.render(data[i]["name"], True, [255,255,255])]
        my_image = text[0]
        rect = my_image.get_rect()
        rect.center = [(W-(W/5)), (40+i*23)]
        fenetre.blit(my_image, rect)
    
    #Rafraichissement de l'ecran
    pygame.display.flip()

    return deck

def load_card_list():
    #Chargement liste des cartes
    json_data = open('decks/card_list.json')
    data = json.load(json_data)
    json_data.close()
    return data
    

def print_deck(fenetre, deck_name):
    W=fenetre.get_width()
    H=fenetre.get_height()
    
    #Choix police
    myfont = pygame.font.SysFont(None, 35)

    #Affichage nom du deck
    text = [myfont.render(deck_name, True, [185,169,255])]
    my_image = text[0]
    rect = my_image.get_rect()
    rect.center = [W/5, 13]
    fenetre.blit(my_image, rect)

    #Changement font pour liste
    myfont = pygame.font.SysFont("Consolas", 20)
    
    deck = load_deck(deck_name)

    
    for i in range(len(deck)):
        fond_carte = pygame.image.load("images/bg_cardList.png").convert_alpha()
        fond_rarity = pygame.image.load("images/bg_"+rarity_to_string(deck[i]["Rarity"])+".png").convert()
        fenetre.blit(fond_carte, (W/5-105, (40+i*23)-11))
        fenetre.blit(fond_rarity, (W/5-105+(208-7), (40+i*23)-11))

        #COST
        text = [myfont.render(str(deck[i]["Cost"]), True, [0,0,0])]
        my_image = text[0]
        rect = my_image.get_rect()
        rect.center = [((W/5)-95), (40+i*23)]
        fenetre.blit(my_image, rect)
        
        #NAME
        text = [myfont.render(deck[i]["name"], True, [255,255,255])]
        my_image = text[0]
        rect = my_image.get_rect()
        rect.center = [W/5, (40+i*23)]
        fenetre.blit(my_image, rect)

    return deck
