import pygame

from pygame.locals import *

#Méthode pour savoir si une carte est jouable
def is_card_playable(card_cost, stats, board):
    isTherePlace = False
    for i in range(0,5):
        if board['player'+str(i)] == 'empty':
            isTherePlace = True

    if isTherePlace:
        if int(stats['player_pool']) >= card_cost:
            return True
    return False

#Intelligence Artificielle ... ou pas !
def play_turn_ia(stats, board, hand_enemy):
    #FIFO - Premiere carte jouable Premiere carte jouée
    for i in range(len(hand_enemy)):
        if is_card_playable_ia(hand_enemy[i]['Cost'], stats, board):
             x = get_empty_slot(board,'enemy')
             board['enemy'+str(x)] = hand_enemy[i]
             board['enemy'+str(x)]['can_attack'] = 0
             del(hand_enemy[i])
             return
        

def get_empty_slot(board, target):
    place = -1
    if target == 'enemy':
        for i in range(0,5):
            if board['enemy'+str(i)] == 'empty':
                return i
    elif target == 'player':
        for i in range(0,5):
            if board['player'+str(i)] == 'empty':
                return i
    return place
            
#Méthode pour savoir si une carte est jouable
def is_card_playable_ia(card_cost, stats, board):
    isTherePlace = False
    for i in range(0,5):
        if board['enemy'+str(i)] == 'empty':
            isTherePlace = True

    if isTherePlace:
        if int(stats['enemy_pool']) >= card_cost:
            return True
    return False

#Methode qui gère l'attack entre deux cartes
def attack_combat(board, index_p, index_e):
    initial_hp_p = board['player'+str(index_p)]['Health']
    initial_hp_e = board['enemy'+str(index_e)]['Health']
    
    board['enemy'+str(index_e)]['Health'] -= board['player'+str(index_p)]['Attack']
    board['player'+str(index_p)]['Health'] -= board['enemy'+str(index_e)]['Attack']
    
    if int(board['enemy'+str(index_e)]['Health']) < initial_hp_e:
        board['enemy'+str(index_e)]['Wounded'] = True
    if int(board['player'+str(index_p)]['Health']) < initial_hp_p:
        board['player'+str(index_p)]['Wounded'] = True

        
    if int(board['enemy'+str(index_e)]['Health']) <= 0:
        board['cimetery_enemy'].append(board['enemy'+str(index_e)])
        board['enemy'+str(index_e)] = 'empty'
    if int(board['player'+str(index_p)]['Health']) <= 0:
        board['cimetery_player'].append(board['enemy'+str(index_e)])
        board['player'+str(index_p)] = 'empty'

def attack_enemy_hero(stats, board, index_p):
    hp_enemy = int(stats['hp_enemy'])
    hp_enemy -= board['player'+str(index_p)]['Attack']
    stats['hp_enemy'] = str(hp_enemy)

        
