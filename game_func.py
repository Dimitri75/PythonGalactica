import pygame
from pygame.locals import *
from card_loading import *
from pprint import pprint

#Fonction principale de jeu
def game_main(fenetre):
    #Mise en place de la vue de la partie
    pygame.display.set_caption("Galactica - Partie en cours")
    fond = pygame.image.load("images/game_background_small.jpg").convert()
    button_ff = pygame.image.load("images/ff_no_highlight.jpg").convert()
    button_ff_h = pygame.image.load("images/ff_highlight.jpg").convert()
    button_next = pygame.image.load("images/next_no_highlight.jpg").convert()
    button_next_h = pygame.image.load("images/next_highlight.jpg").convert()
    fenetre.blit(fond, (0,0))
    fenetre.blit(button_ff, (835,695))
    fenetre.blit(button_next, (835,660))

    #Creer des rectangles pour le Mouse Over
    ff_r = button_ff.get_rect()
    ff_r.x, ff_r.y = 835,695
    next_r = button_next.get_rect()
    next_r.x, next_r.y = 835,660
    pygame.display.flip()

    #Chargement des decks de base
    deck_name = 'deck_base'
    deck_name_ia = 'deck_base_ia'
    deck_player = load_deck(deck_name)
    deck_enemy = load_deck(deck_name_ia)

    #Mains de depart
    hand_player = initial_hand(deck_player)
    hand_enemy = initial_hand(deck_enemy)
    print_hands(fenetre, hand_player, hand_enemy)
    
    #Stats de la partie mise a jour en temps reel
    stats = {'hp_player' : '30', 'hp_enemy' : '30', 'mana_player' : '1', 'mana_enemy' : '1'}
    continuer = 1

    #Boucle principale de jeu
    while continuer:
        
        for event in pygame.event.get():
            if event.type == pygame.quit:
                continuer = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                #Bouton SURRENDER
                if ( x in range(835,960)) and (y in range(695,720)):
                    continuer = 0
                #Bouton NEXT TURN
                if ( x in range(835,960)) and (y in range(660,685)):
                    turn_enemy(stats, hand_enemy, deck_enemy)
                    turn_player(stats, hand_player, deck_player)
        #MOUSE OVER (met les boutons en rouge lorsque la souris est au dessus)
        if ff_r.collidepoint(pygame.mouse.get_pos()):
            fenetre.blit(button_ff_h, (835,695))
            pygame.display.flip()
        elif next_r.collidepoint(pygame.mouse.get_pos()):
            fenetre.blit(button_next_h, (835,660))
            pygame.display.flip()
        else:
            game_routine(fenetre, stats, deck_player, deck_enemy, hand_player, hand_enemy)

#Methode appelee au debut du tour de l'IA
def turn_enemy(stats, hand_enemy, deck_enemy):
    stats['mana_enemy'] = str(int(stats['mana_enemy']) + 1)
    draw_card(stats, hand_enemy, deck_enemy, "enemy")
    #APPEL DE L'IA se trouvera ici

#Methode appelee a la fin du tour de l'IA
def turn_player(stats, hand_player, deck_player):
    stats['mana_player'] = str(int(stats['mana_player']) + 1)
    draw_card(stats, hand_player, deck_player, "player")


#Methode d'actualisation de la vue GENERALE de la partie
def game_routine(fenetre, stats, deck_player, deck_enemy, hand_player, hand_enemy):
    fond = pygame.image.load("images/game_background_small.jpg").convert()
    button_ff = pygame.image.load("images/ff_no_highlight.jpg").convert()
    button_next = pygame.image.load("images/next_no_highlight.jpg").convert()
    fenetre.blit(fond, (0,0))
    fenetre.blit(button_ff, (835,695))
    fenetre.blit(button_next, (835,660))
    game_stats(fenetre, stats, deck_player, deck_enemy)
    print_hands(fenetre, hand_player, hand_enemy)
    pygame.display.flip()

#Methode d'actualisation des statistiques de la partie
def game_stats(fenetre, stats, deck_player, deck_enemy):   
    font = pygame.font.Font(None, 36)

    hp_player = font.render(stats['hp_player'], 1, (255, 255, 255))
    hp_enemy = font.render(stats['hp_enemy'], 1, (255, 255, 255))
    mana_player = font.render(stats['mana_player'], 1, (0, 0, 255))
    mana_enemy = font.render(stats['mana_enemy'], 1 , (0, 0, 255))
    cards_left_player = font.render(str(len(deck_player)),1 , (0, 255, 0))
    cards_left_enemy = font.render(str(len(deck_enemy)),1 , (0, 255, 0))
    
    fenetre.blit(hp_player, (590,650)) 
    fenetre.blit(hp_enemy, (470,40))
    fenetre.blit(mana_player, (710,660))
    fenetre.blit(mana_enemy, (640,60))
    fenetre.blit(cards_left_player, (900, 615))
    fenetre.blit(cards_left_enemy, (900, 13))

def print_hands(fenetre, hand_player, hand_enemy):
    font = pygame.font.Font(None, 20)
    font_name = pygame.font.Font(None, 15)
    model_card_front = pygame.image.load("images/card_model_hand.png").convert()
    list_image_maps = []
    model_card_back = pygame.image.load("images/back_card_model.jpg").convert()
    
    #Affichage de la main du joueur
    for i in range(len(hand_player)):
        temp_image = pygame.image.load("decks/img/"+str(hand_player[i]['name'])+".png").convert()
        fenetre.blit(model_card_front, (0+(i*68),610))
        fenetre.blit(temp_image, (18+(i*68),610))
        
        name = font_name.render(str(hand_player[i]['name']), 1, (255, 255, 255))
        cost = font.render(str(hand_player[i]['Cost']), 1, (255, 255, 255))
        health = font.render(str(hand_player[i]['Health']), 1, (255, 255, 255))
        attack = font.render(str(hand_player[i]['Attack']), 1, (255, 255, 255))
        if len(str(hand_player[i]['name']))>6:
            fenetre.blit(name, (10+(i*68),654))
        else:
            fenetre.blit(name, (25+(i*68),654))
        fenetre.blit(cost, (5+(i*68),614))
        fenetre.blit(health, (57+(i*68),685))
        fenetre.blit(attack, (5+(i*68),685))
    #Affichage de la main de l'IA
    for i in range(len(hand_enemy)):
        fenetre.blit(model_card_back, (0+(i*34),0))
