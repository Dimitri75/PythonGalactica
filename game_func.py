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
    fenetre.blit(button_ff, (515,455))
    fenetre.blit(button_next, (515,430))
    ff_r = button_ff.get_rect()
    ff_r.x, ff_r.y = 515,455
    next_r = button_next.get_rect()
    next_r.x, next_r.y = 515,430
    pygame.display.flip()

    #Chargement des decks de base
    deck_name = 'deck_base'
    deck_player = load_deck(deck_name)
    deck_enemy = load_deck(deck_name)

    #Mains de depart
    hand_player = initial_hand(deck_player)
    hand_enemy = initial_hand(deck_enemy)
    print_hand(fenetre, hand_player)
    
    #Stats de la partie mise à jour en temps reel
    stats = {'hp_player' : '30', 'hp_enemy' : '30', 'mana_player' : '1', 'mana_enemy' : '1'}
    continuer = 1

    #Boucle principale de jeu
    while continuer:
        game_routine(fenetre, stats, deck_player, deck_enemy, hand_player)
        for event in pygame.event.get():
            if event.type == pygame.quit:
                continuer = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                #Bouton SURRENDER
                if ( x in range(515,640)) and (y in range(455,480)):
                    continuer = 0
                #Bouton NEXT TURN
                if ( x in range(515,640)) and (y in range(430,455)):
                    turn_enemy(stats, hand_enemy, deck_enemy)
                    turn_player(stats, hand_player, deck_player)
        #MOUSE OVER (met les boutons en rouge lorsque la souris est au dessus)
        if ff_r.collidepoint(pygame.mouse.get_pos()):
            fenetre.blit(button_ff_h, (515,455))
            pygame.display.flip()
        elif next_r.collidepoint(pygame.mouse.get_pos()):
            fenetre.blit(button_next_h, (515,430))
            pygame.display.flip()

#Methode appelée au debut du tour de l'IA
def turn_enemy(stats, hand_enemy, deck_enemy):
    stats['mana_enemy'] = str(int(stats['mana_enemy']) + 1);

#Methode appelée à la fin du tour de l'IA
def turn_player(stats, hand_player, deck_player):
    stats['mana_player'] = str(int(stats['mana_player']) + 1);


#Methode d'actualisation de la vue GENERALE de la partie
def game_routine(fenetre, stats, deck_player, deck_enemy, hand_player):
    fond = pygame.image.load("images/game_background_small.jpg").convert()
    button_ff = pygame.image.load("images/ff_no_highlight.jpg").convert()
    button_next = pygame.image.load("images/next_no_highlight.jpg").convert()
    fenetre.blit(fond, (0,0))
    fenetre.blit(button_ff, (515,455))
    fenetre.blit(button_next, (515,430))
    game_stats(fenetre, stats, deck_player, deck_enemy)
    print_hand(fenetre, hand_player)
    pygame.display.flip()

#Methode d'actualisation des statistiques de la partie
def game_stats(fenetre, stats, deck_player, deck_enemy):   
    font = pygame.font.Font(None, 36)
    
    hp_player = font.render(stats['hp_player'], 1, (255, 255, 255))
    hp_enemy = font.render(stats['hp_enemy'], 1, (255, 255, 255))
    mana_player = font.render(stats['mana_player'], 1, (255, 255, 255))
    mana_enemy = font.render(stats['mana_enemy'], 1 , (255, 255, 255))
    cards_left_player = font.render(str(len(deck_player)),1 , (255, 255, 255))
    cards_left_enemy = font.render(str(len(deck_enemy)),1 , (255, 255, 255))
    
    fenetre.blit(hp_player, (310,430)) 
    fenetre.blit(hp_enemy, (310,25))
    fenetre.blit(mana_player, (405,450))
    fenetre.blit(mana_enemy, (400,45))
    fenetre.blit(cards_left_player, (595, 402))
    fenetre.blit(cards_left_enemy, (600, 3))

def print_hand(fenetre, hand_player):
    font = pygame.font.Font(None, 15)
    font_name = pygame.font.Font(None, 12)
    #for i in range(5):
    #    temp = hand_player[i]['name']+' - A : '+str(hand_player[i]['Attack'])+' - H : '+str(hand_player[i]['Health'])+' - C : '+str(hand_player[i]['Cost'])
    #    card = font.render(temp, 1, (255, 255, 255))
    #    fenetre.blit(card, (0, 400+(i*10)))
    model = pygame.image.load("images/card_model_hand.png").convert()
    for i in range(len(hand_player)):
        fenetre.blit(model, (0+(i*50),410))
        name = font_name.render(str(hand_player[i]['name']), 1, (255, 255, 255))
        cost = font.render(str(hand_player[i]['Cost']), 1, (255, 255, 255))
        health = font.render(str(hand_player[i]['Health']), 1, (255, 255, 255))
        attack = font.render(str(hand_player[i]['Attack']), 1, (255, 255, 255))
        fenetre.blit(name, (8+(i*50),444))
        fenetre.blit(cost, (5+(i*50),414))
        fenetre.blit(health, (45+(i*50),470))
        fenetre.blit(attack, (5+(i*50),470))
