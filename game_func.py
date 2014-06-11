import pygame
from pygame.locals import *
from card_loading import *
from pprint import pprint

#Fonction principale de jeu
def game_main(fenetre):
    #Mise en place de la vue de la partie
    pygame.display.set_caption("Galactica - Partie en cours")
    fond = pygame.image.load("images/background_game.jpg").convert()
    button_ff = pygame.image.load("images/ff_no_highlight.jpg").convert()
    button_ff_h = pygame.image.load("images/ff_highlight.jpg").convert()
    button_next = pygame.image.load("images/next_no_highlight.jpg").convert()
    button_next_h = pygame.image.load("images/next_highlight.jpg").convert()
    health_bar = pygame.image.load("images/healthbar.png").convert()
    fenetre.blit(fond, (0,0))
    fenetre.blit(button_ff, (835,695))
    fenetre.blit(button_next, (835,660))
    fenetre.blit(health_bar, (500,650))

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
    list_image_maps = print_hands(fenetre, hand_player, hand_enemy)
    
    #Stats de la partie mise a jour en temps reel
    stats = {'hp_player' : '30', 'hp_enemy' : '30', 'mana_player' : '1', 'mana_enemy' : '1', 'player_pool' : '1', 'enemy_pool' : '1'}
    continuer = 1

    #MouseOver Meilleur lecture de la carte
    big_card = pygame.image.load("images/card_model.png").convert_alpha()
    card_subri = pygame.image.load("images/card_subri.png").convert()
    isNotHover = True
    fontHover = pygame.font.Font(None, 38)
    
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
        increment_Hover = 0
        for i in list_image_maps:
            if i.collidepoint(pygame.mouse.get_pos()):  
                isNotHover = False
                name = fontHover.render(str(hand_player[increment_Hover]['name']), 1, (255, 255, 255))
                cost = fontHover.render(str(hand_player[increment_Hover]['Cost']), 1, (255, 255, 255))
                health = fontHover.render(str(hand_player[increment_Hover]['Health']), 1, (255, 255, 255))
                attack = fontHover.render(str(hand_player[increment_Hover]['Attack']), 1, (255, 255, 255))
                temp_image_card = pygame.image.load("decks/img/hover-"+str(hand_player[increment_Hover]['name'])+".png").convert()
                fenetre.blit(temp_image_card, (470,210))
                fenetre.blit(big_card, (400,200))
                fenetre.blit(card_subri,(0+(increment_Hover*68),610))
                if len(str(hand_player[increment_Hover]['name']))>6:
                    fenetre.blit(name, (490,420))
                else:
                    fenetre.blit(name, (35+490,420))
                fenetre.blit(cost, (435,235))
                fenetre.blit(health, (660,565))
                fenetre.blit(attack, (435,565))
                list_image_maps = print_hands(fenetre, hand_player, hand_enemy)
                pygame.display.flip()
                break
            else:
                increment_Hover += 1
                isNotHover = True
        if isNotHover:
             list_image_maps = game_routine(fenetre, stats, deck_player, deck_enemy, hand_player, hand_enemy)

#Methode appelee au debut du tour de l'IA
def turn_enemy(stats, hand_enemy, deck_enemy):
    if int(stats['mana_enemy']) < 10:
        stats['mana_enemy'] = str(int(stats['mana_enemy']) + 1)
    draw_card(stats, hand_enemy, deck_enemy, "enemy")
    #APPEL DE L'IA se trouvera ici

#Methode appelee a la fin du tour de l'IA
def turn_player(stats, hand_player, deck_player):
    if int(stats['mana_player']) < 10:
        stats['mana_player'] = str(int(stats['mana_player']) + 1)
    draw_card(stats, hand_player, deck_player, "player")


#Methode d'actualisation de la vue GENERALE de la partie
def game_routine(fenetre, stats, deck_player, deck_enemy, hand_player, hand_enemy):
    fond = pygame.image.load("images/background_game.jpg").convert()
    button_ff = pygame.image.load("images/ff_no_highlight.jpg").convert()
    button_next = pygame.image.load("images/next_no_highlight.jpg").convert()
    fenetre.blit(fond, (0,0))
    fenetre.blit(button_ff, (835,695))
    fenetre.blit(button_next, (835,660))
    game_stats(fenetre, stats, deck_player, deck_enemy)
    list_image_maps = print_hands(fenetre, hand_player, hand_enemy)
    pygame.display.flip()
    return list_image_maps

#Methode d'actualisation des statistiques de la partie
def game_stats(fenetre, stats, deck_player, deck_enemy):   
    font = pygame.font.Font(None, 36)
    health_bar = pygame.image.load("images/healthbar.png").convert()
    
    hp_player = font.render(stats['hp_player'], 1, (255, 255, 255))
    hp_enemy = font.render(stats['hp_enemy'], 1, (255, 255, 255))
    mana_player = font.render("Mana : "+stats['mana_player'], 1, (0, 0, 255))
    mana_enemy = font.render("Mana : "+stats['mana_enemy'], 1 , (0, 0, 255))
    cards_left_player = font.render("Deck : "+str(len(deck_player)),1 , (0, 255, 0))
    cards_left_enemy = font.render("Deck : "+str(len(deck_enemy)),1 , (0, 255, 0))

    fenetre.blit(health_bar, (580,25))
    fenetre.blit(health_bar, (580,640))
    fenetre.blit(hp_player, (640,655)) 
    fenetre.blit(hp_enemy, (640,40))
    fenetre.blit(mana_player, (710,680))
    fenetre.blit(mana_enemy, (800,60))
    fenetre.blit(cards_left_player, (710, 640))
    fenetre.blit(cards_left_enemy, (800, 20))
    

def print_hands(fenetre, hand_player, hand_enemy):
    font = pygame.font.Font(None, 20)
    font_name = pygame.font.Font(None, 15)
    model_card_front = pygame.image.load("images/card_model_hand.png").convert_alpha()
    list_image_maps = []
    model_card_back = pygame.image.load("images/back_card_model.jpg").convert()
    
    #Affichage de la main du joueur
    for i in range(len(hand_player)):
        temp_image = pygame.image.load("decks/img/"+str(hand_player[i]['name'])+".png").convert()
        im = model_card_front.get_rect()
        im.x, im.y = (i*68),610
        list_image_maps.append(im)
        fenetre.blit(temp_image, (18+(i*68),610))
        fenetre.blit(model_card_front, (0+(i*68),610))
        
        
        name = font_name.render(str(hand_player[i]['name']), 1, (255, 255, 255))
        cost = font.render(str(hand_player[i]['Cost']), 1, (255, 255, 255))
        health = font.render(str(hand_player[i]['Health']), 1, (255, 255, 255))
        attack = font.render(str(hand_player[i]['Attack']), 1, (255, 255, 255))
        if len(str(hand_player[i]['name']))>6:
            fenetre.blit(name, (10+(i*68),657))
        else:
            fenetre.blit(name, (25+(i*68),657))
        fenetre.blit(cost, (5+(i*68),614))
        fenetre.blit(health, (57+(i*68),687))
        fenetre.blit(attack, (5+(i*68),687))
    #Affichage de la main de l'IA
    for i in range(len(hand_enemy)):
        fenetre.blit(model_card_back, (0+(i*34),0))

    return list_image_maps
