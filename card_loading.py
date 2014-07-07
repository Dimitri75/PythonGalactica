import json
import pygame
import random

def load_deck(deck_name):
    json_data = open('decks/decklist/'+deck_name+'.json')
    data = json.load(json_data)
    json_data.close()
    return data

def initial_hand(deck):
    l = []
    for x in range(5):
        temp = random.choice(deck)
        l.append(temp)
        deck.remove(temp)
    return l

def draw_card(stats, hand, deck, who):
    if len(deck)==0:
        if who=="enemy":
            stats['hp_enemy'] = str(int(stats['hp_enemy'])-1)
        elif who=="player":
            stats['hp_player'] = str(int(stats['hp_player'])-1)
        return 0
    if len(hand)==8:
        deck.remove(random.choice(deck))
        return 0
    temp = random.choice(deck)
    hand.append(temp)
    deck.remove(temp)

def capacity_to_string(capacity):
    if capacity == 0:
        return ""
    elif capacity == 1:
        return "Draw a card"
    elif capacity == 2:
        return "Taunt"

    

