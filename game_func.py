import pygame
import time
import copy
from pygame.locals import *
from card_loading import *
from ia import *

#Fonction principale de jeu
def game_main(fenetre, mode, deck1, deck2):
    #Mise en place de la vue de la partie
    pygame.display.set_caption("Galactica - Partie en cours")
    fond = pygame.image.load("images/background_game.jpg").convert()
    button_ff = pygame.image.load("images/ff_no_highlight.jpg").convert()
    button_ff_h = pygame.image.load("images/ff_highlight.jpg").convert()
    button_next = pygame.image.load("images/next_no_highlight.jpg").convert()
    button_next_h = pygame.image.load("images/next_highlight.jpg").convert()
    fenetre.blit(fond, (0,0))
    fenetre.blit(button_ff, (835,695))
    fenetre.blit(button_next, (835,660))
    fontWL = pygame.font.Font(None, 75)
    #Creer des rectangles pour le Mouse Over
    ff_r = button_ff.get_rect()
    ff_r.x, ff_r.y = 835,695
    next_r = button_next.get_rect()
    next_r.x, next_r.y = 835,660
    pygame.display.flip()

    #Chargement des decks de base
    deck_name = deck1
    deck_name_ia = deck2
    deck_player = load_deck(deck_name)
    deck_enemy = load_deck(deck_name_ia)

    #Mains de depart
    hand_player = initial_hand(deck_player)
    hand_enemy = initial_hand(deck_enemy)
    list_image_maps = print_hands(fenetre, hand_player, hand_enemy)

    #Board de la partie
    board = {'enemy0' : 'empty', 'enemy1' : 'empty', 'enemy2' : 'empty', 'enemy3' : 'empty', 'enemy4' : 'empty', 'player0' : 'empty', 'player1' : 'empty', 'player2' : 'empty', 'player3' : 'empty', 'player4' : 'empty'}
    board['cimetery_enemy'] = []
    board['cimetery_player'] = []
    is_attacking = False
    display_board(fenetre, board, is_attacking)
    
    #Stats de la partie mise a jour en temps reel
    stats = {'hp_player' : '30', 'hp_enemy' : '30', 'mana_player' : '1', 'mana_enemy' : '1', 'player_pool' : '1', 'enemy_pool' : '1'}
    continuer = 1


    #Drag&Drop
    is_dragged = False
    firstFrame = True
    card_from_board = -1
    #MouseOver Meilleur lecture de la carte
    big_card = pygame.image.load("images/card_model.png").convert_alpha()
    card_subri = pygame.image.load("images/card_subri.png").convert()
    card_playable = pygame.image.load("images/card_subri_green.png").convert()
    isNotHover = True
    fontHover = pygame.font.Font(None, 38)
    id_selected_card = 0
    #Boucle principale de jeu & 1er tour
    draw_card(stats, hand_player, deck_player, "player")
    while continuer:
        if (int(stats['hp_player'])<=0):
            name = fontWL.render("YOU LOSE !", 1, (255, 255, 255))
            fenetre.blit(name, (200,200))
            continuer = 0
            pygame.display.flip()
            time.sleep(3)
        elif (int(stats['hp_enemy'])<=0):
            name = fontWL.render("YOU WIN !", 1, (255, 255, 255))
            fenetre.blit(name, (200,200))
            continuer = 0
            pygame.display.flip()
            time.sleep(3)
        if is_dragged:
            fenetre.blit(card, pygame.mouse.get_pos())
            pygame.display.flip()
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
                    if mode == 0:
                        swap(fenetre, stats, board)
                        hand_player, hand_enemy = hand_enemy, hand_player
                        deck_player, deck_enemy = deck_enemy, deck_player
                        turn_player(stats, board, hand_player, deck_player)
                    elif mode == 1:
                        turn_player(stats, board, hand_player, deck_player)
                        turn_enemy(stats, board, hand_enemy, deck_enemy)
                    
                #Drag de la carte a partir de la main
                for i in range(len(hand_player)):
                    if ( x in range(0+(i*68),0+(i*68)+68)) and (y in range(610,704)):
                        is_dragged = True
                        if firstFrame:
                            firstFrame = False
                            rect = pygame.Rect((0+(i*68)),610, 68, 94)
                            card = fenetre.subsurface(rect)
                            card = card.copy()
                            tempCard = hand_player[i]
                            del(hand_player[i])
                            list_image_maps = game_routine(fenetre, board, stats, deck_player, deck_enemy, hand_player, hand_enemy, is_attacking)

                #Drag de la carte a partir du board
                for i in range(0,5):
                    if board['player'+str(i)] != 'empty':
                        if board['player'+str(i)]['can_attack'] == 1:
                            if (x in range(150+(i*150),150+(i*150)+68)) and (y in range(350,350+94)):
                                is_dragged = True
                                is_attacking = True
                                card_from_board = i
                                if firstFrame:
                                    firstFrame = False
                                    rect = pygame.Rect((150+(i*150)),350, 68, 94)
                                    card = fenetre.subsurface(rect)
                                    card = card.copy()
                                    tempCard = board['player'+str(i)]
                                    board['player'+str(i)] = 'empty'
                                    list_image_maps = game_routine(fenetre, board, stats, deck_player, deck_enemy, hand_player, hand_enemy, is_attacking)
                                    
            #Drop de la carte
            if event.type == pygame.MOUSEBUTTONUP:
                if is_dragged:
                    x, y = event.pos
                    card_to_hand = True
                    is_dragged = False
                    is_attacking = False
                    firstFrame = True
                    if card_from_board != -1:
                        for i in range(0,5):
                            if board['enemy'+str(i)] != 'empty':
                                if (x in range(150+(i*150),150+(i*150)+68)) and (y in range(150,150+94)):
                                    if is_taunt_on_board(board) == -1:
                                        card_to_hand = False
                                        board['player'+str(card_from_board)] = copy.deepcopy(tempCard)
                                        board['player'+str(card_from_board)]['can_attack'] = 0
                                        attack_combat(board, card_from_board, i)
                                        card_from_board = -1
                                        break
                                    elif is_taunt_on_board(board) == i:
                                        card_to_hand = False
                                        board['player'+str(card_from_board)] = copy.deepcopy(tempCard)
                                        board['player'+str(card_from_board)]['can_attack'] = 0
                                        attack_combat(board, card_from_board, i)
                                        card_from_board = -1
                                        break
                    if card_from_board != -1:
                        card_to_hand = False
                        board['player'+str(card_from_board)] = tempCard
                        if (x in range(580,580+125)) and (y in range(25,25+61)):
                            if is_taunt_on_board(board) == -1:
                                board['player'+str(card_from_board)]['can_attack'] = 0
                                attack_enemy_hero(stats, board, card_from_board) 
                        card_from_board = -1
                    else:
                        for i in range(0,5):
                            if ( x in range(150+(i*150),150+(i*150)+70)) and (y in range(350,350+96)):
                                if board['player'+str(i)] == 'empty':
                                    if is_card_playable(tempCard['Cost'], stats, board):
                                        tempCard['can_attack'] = 0
                                        board['player'+str(i)] = copy.deepcopy(tempCard)
                                        call_capacity(stats, board, hand_player, deck_player, i)
                                        stats['player_pool'] = str(int(stats['player_pool']) - int(tempCard['Cost']))
                                        card_to_hand = False
                    if card_to_hand:
                        hand_player.append(tempCard)
        #MOUSE OVER (met les boutons en rouge lorsque la souris est au dessus)
        if ff_r.collidepoint(pygame.mouse.get_pos()):
            fenetre.blit(button_ff_h, (835,695))
            pygame.display.flip()
        elif next_r.collidepoint(pygame.mouse.get_pos()):
            fenetre.blit(button_next_h, (835,660))
            pygame.display.flip()
        #MOUSE OVER de la main du joueur
        increment_Hover = 0     
        for i in list_image_maps:
            if i.collidepoint(pygame.mouse.get_pos()):
                isNotHover = False
                name = fontHover.render(str(hand_player[increment_Hover]['name']), 1, (255, 255, 255))
                cost = fontHover.render(str(hand_player[increment_Hover]['Cost']), 1, (255, 255, 255))
                health = fontHover.render(str(hand_player[increment_Hover]['Health']), 1, (255, 255, 255))
                attack = fontHover.render(str(hand_player[increment_Hover]['Attack']), 1, (255, 255, 255))
                tempString = capacity_to_string(hand_player[increment_Hover]['Capacity'])
                if len(tempString) < 8:
                    tempString = "          "+tempString
                capacity = fontHover.render(tempString, 1, (255, 255, 255))
                temp_image_card = pygame.image.load("decks/img/hover-"+str(hand_player[increment_Hover]['name'])+".png").convert()
                fenetre.blit(temp_image_card, (470,210))
                fenetre.blit(big_card, (400,200))
                if id_selected_card != increment_Hover:
                    id_selected_card = increment_Hover
                    game_routine(fenetre, board, stats, deck_player, deck_enemy, hand_player, hand_enemy, is_attacking)
                    if is_card_playable(hand_player[increment_Hover]['Cost'],stats,board):
                        fenetre.blit(card_playable, (0+(increment_Hover*68),610))
                    else:
                        fenetre.blit(card_subri,(0+(increment_Hover*68),610))
                if len(str(hand_player[increment_Hover]['name']))>6:
                    fenetre.blit(name, (490,420))
                else:
                    fenetre.blit(name, (35+490,420))
                fenetre.blit(cost, (435,235))
                fenetre.blit(capacity, (440, 470))
                fenetre.blit(health, (660,565))
                fenetre.blit(attack, (435,565))
                list_image_maps = print_hands(fenetre, hand_player, hand_enemy)
                pygame.display.flip()
                break
            else:
                increment_Hover += 1
                isNotHover = True
        if isNotHover:
             list_image_maps = game_routine(fenetre, board, stats, deck_player, deck_enemy, hand_player, hand_enemy, is_attacking)




#Methode d'affichage du board
def display_board(fenetre, board, is_attacking):
    font = pygame.font.Font(None, 20)
    font_name = pygame.font.Font(None, 15)
    font_capacity = pygame.font.Font(None, 9)
    board_case_empty = pygame.image.load("images/card_drop_green.jpg").convert()
    board_case_attack = pygame.image.load("images/card_drop_yellow.jpg").convert()
    board_case_full = pygame.image.load("images/card_drop_red.jpg").convert()
    board_case_taunt = pygame.image.load("images/card_drop_purple.jpg").convert()
    
    for i in range(0,5):
        if board['enemy'+str(i)] == 'empty':
            fenetre.blit(board_case_empty, (150 +(i*150),145))
        else:
            if is_attacking and is_taunt_existing(board, i):
                 fenetre.blit(board_case_taunt, (150 +(i*150),145))
            else:
                if board['enemy'+str(i)]['can_attack'] == 1:
                    fenetre.blit(board_case_attack, (150 +(i*150),145))
                else:
                    fenetre.blit(board_case_full, (150 +(i*150),145))
            model_card_front = pygame.image.load("images/card_model_hand.png").convert_alpha()
            temp_image = pygame.image.load("decks/img/"+str(board['enemy'+str(i)]['name'])+".png").convert()
            fenetre.blit(temp_image, (168+(i*150),150))
            fenetre.blit(model_card_front, (150+(i*150),150))   
            
            name = font_name.render(str(board['enemy'+str(i)]['name']), 1, (255, 255, 255))
            cost = font.render(str(board['enemy'+str(i)]['Cost']), 1, (255, 255, 255))
            if 'Wounded' in board['enemy'+str(i)]:
                health = font.render(str(board['enemy'+str(i)]['Health']), 1, (255, 0, 0))
            else:
                health = font.render(str(board['enemy'+str(i)]['Health']), 1, (255, 255, 255))
            attack = font.render(str(board['enemy'+str(i)]['Attack']), 1, (255, 255, 255))
            tempString = capacity_to_string(board['enemy'+str(i)]['Capacity'])
            if len(tempString) < 8:
                tempString = "          "+tempString
            capacity = font_capacity.render(tempString, 1, (255, 255, 255))
            if len(str(board['enemy'+str(i)]['name']))>6:
                fenetre.blit(name, (160+(i*150),197))
            else:
                fenetre.blit(name, (175+(i*150),197))
            fenetre.blit(cost, (155+(i*150),154))
            fenetre.blit(capacity, (155+(i*150),207))
            fenetre.blit(health, (207+(i*150),227))
            fenetre.blit(attack, (155+(i*150),227))
    for i in range(0,5):
        if board['player'+str(i)] == 'empty':
            fenetre.blit(board_case_empty, (150 +(i*150),345))
        else:
            if board['player'+str(i)]['can_attack'] == 1:
                fenetre.blit(board_case_attack, (150 +(i*150),345))
            else:
                fenetre.blit(board_case_full, (150 +(i*150),345))
            model_card_front = pygame.image.load("images/card_model_hand.png").convert_alpha()
            temp_image = pygame.image.load("decks/img/"+str(board['player'+str(i)]['name'])+".png").convert()
            fenetre.blit(temp_image, (168+(i*150),350))
            fenetre.blit(model_card_front, (150+(i*150),350))  
            
            name = font_name.render(str(board['player'+str(i)]['name']), 1, (255, 255, 255))
            cost = font.render(str(board['player'+str(i)]['Cost']), 1, (255, 255, 255))
            if 'Wounded' in board['player'+str(i)]:
                health = font.render(str(board['player'+str(i)]['Health']), 1, (255, 0, 0))
            else:
                health = font.render(str(board['player'+str(i)]['Health']), 1, (255, 255, 255))
            attack = font.render(str(board['player'+str(i)]['Attack']), 1, (255, 255, 255))
            tempString = capacity_to_string(board['player'+str(i)]['Capacity'])
            if len(tempString) < 8:
                tempString = "          "+tempString
            capacity = font_capacity.render(tempString, 1, (255, 255, 255))
            if len(str(board['player'+str(i)]['name']))>6:
                fenetre.blit(name, (160+(i*150),397))
            else:
                fenetre.blit(name, (175+(i*150),397))
            fenetre.blit(cost, (155+(i*150),354))
            fenetre.blit(capacity, (155+(i*150),407))
            fenetre.blit(health, (207+(i*150),427))
            fenetre.blit(attack, (155+(i*150),427))
            
def swap(fenetre, stats, board):
    temp_board = copy.deepcopy(board)
    temp_stats = copy.deepcopy(stats)
    
    for i in range(0,5):
        board['player'+str(i)] = copy.deepcopy(board['enemy'+str(i)])
    stats['hp_player'] = stats['hp_enemy']
    stats['mana_player'] = stats['mana_enemy']
    for i in range(0,5):
        board['enemy'+str(i)] = copy.deepcopy(temp_board['player'+str(i)])
    stats['hp_enemy'] = temp_stats['hp_player']
    stats['mana_enemy'] = temp_stats['mana_player']


    temp_fond = pygame.image.load("images/swap_background.jpg").convert()
    title = pygame.image.load("images/title.png").convert()
    fenetre.blit(temp_fond, (0,0))
    fenetre.blit(title, (325,0))
    pygame.display.flip()
    time.sleep(3)
    
#Methode appelee au debut du tour de l'IA
def turn_enemy(stats, board, hand_enemy, deck_enemy):
    if int(stats['mana_enemy']) < 10:
        stats['mana_enemy'] = str(int(stats['mana_enemy']) + 1)
    for i in range(0,5):
        if board['enemy'+str(i)] != 'empty':
            board['enemy'+str(i)]['can_attack'] = 1
    stats['enemy_pool'] = stats['mana_enemy']
    draw_card(stats, hand_enemy, deck_enemy, "enemy")
    play_turn_ia(stats, board, hand_enemy)

    
#Methode appelee a la fin du tour de l'IA
def turn_player(stats, board, hand_player, deck_player):
    #Augmente la mana pool jusqu'a 10 (maximum de mana)
    if int(stats['mana_player']) < 10:
        stats['mana_player'] = str(int(stats['mana_player']) + 1)
    #En debut de tour tous les serviteurs peuvent a nouver attacker
    for i in range(0,5):
        if board['player'+str(i)] != 'empty':
            board['player'+str(i)]['can_attack'] = 1
    #On reremplit la pool de manapour le tour
    stats['player_pool'] = stats['mana_player']
    #On pioche une carte
    draw_card(stats, hand_player, deck_player, "player")


#Methode d'actualisation de la vue GENERALE de la partie
def game_routine(fenetre, board, stats, deck_player, deck_enemy, hand_player, hand_enemy, is_attacking):
    fond = pygame.image.load("images/background_game.jpg").convert()
    button_ff = pygame.image.load("images/ff_no_highlight.jpg").convert()
    button_next = pygame.image.load("images/next_no_highlight.jpg").convert()
    fenetre.blit(fond, (0,0))
    fenetre.blit(button_ff, (835,695))
    fenetre.blit(button_next, (835,660))
    game_stats(fenetre, stats, deck_player, deck_enemy)
    list_image_maps = print_hands(fenetre, hand_player, hand_enemy)
    display_board(fenetre, board, is_attacking)
    pygame.display.flip()
    
    return list_image_maps

#Methode d'actualisation des statistiques de la partie
def game_stats(fenetre, stats, deck_player, deck_enemy):   
    font = pygame.font.Font(None, 36)
    y = int(stats['hp_enemy'])
    x = int(stats['hp_player'])
    health_p = x - x%6
    health_e = y - y%6
    if health_p < 0:
        health_p = 0
    if health_e < 0:
        health_e = 0
    health_bar_p = pygame.image.load("images/healthbar_"+str(health_p)+".png").convert()
    health_bar_e = pygame.image.load("images/healthbar_"+str(health_e)+".png").convert()
    
    hp_player = font.render(stats['hp_player'], 1, (255, 255, 255))
    hp_enemy = font.render(stats['hp_enemy'], 1, (255, 255, 255))
    mana_player = font.render("Mana: "+stats['player_pool']+"/"+stats['mana_player'], 1, (0, 0, 255))
    mana_enemy = font.render("Mana: "+stats['enemy_pool']+"/"+stats['mana_enemy'], 1 , (0, 0, 255))
    cards_left_player = font.render("Deck: "+str(len(deck_player)),1 , (0, 255, 0))
    cards_left_enemy = font.render("Deck: "+str(len(deck_enemy)),1 , (0, 255, 0))

    fenetre.blit(health_bar_e, (580,25))
    fenetre.blit(health_bar_p, (580,640))
    fenetre.blit(hp_player, (640,655)) 
    fenetre.blit(hp_enemy, (640,40))
    fenetre.blit(cards_left_player, (710,680))
    fenetre.blit(mana_enemy, (800,60))
    fenetre.blit(mana_player, (710, 640))
    fenetre.blit(cards_left_enemy, (800, 20))
    

def print_hands(fenetre, hand_player, hand_enemy):
    font = pygame.font.Font(None, 20)
    font_name = pygame.font.Font(None, 15)
    font_capacity = pygame.font.Font(None, 9)
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
        tempString = capacity_to_string(hand_player[i]['Capacity'])
        if len(tempString) < 8:
            tempString = "          "+tempString
        capacity = font_capacity.render(tempString, 1, (255, 255, 255))
        if len(str(hand_player[i]['name']))>6:
            fenetre.blit(name, (10+(i*68),657))
        else:
            fenetre.blit(name, (25+(i*68),657))
        fenetre.blit(cost, (5+(i*68),614))
        fenetre.blit(capacity, (7+(i*68),670))
        fenetre.blit(health, (57+(i*68),687))
        fenetre.blit(attack, (5+(i*68),687))
    #Affichage de la main de l'IA
    for i in range(len(hand_enemy)):
        fenetre.blit(model_card_back, (0+(i*34),0))

    return list_image_maps
