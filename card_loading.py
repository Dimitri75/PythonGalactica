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
    elif capacity == 3:
        return "1 damage to board"

def is_rarityMax_in_deck(deck, name):
    maxRare = 5
    maxEpic = 2
    maxLegendary = 1
    i = 0
    for card in deck:
        if card['name'] == name:
            i += 1
    if len(deck) > 0:
        if (card['Rarity'] == 1) and (i == maxRare):
            return True
        elif (card['Rarity'] == 2) and (i == maxEpic):
            return True
        elif (card['Rarity'] == 3) and (i == maxLegendary):
            return True
    return False 

def rarity_to_string(rarity):
    if rarity == 0:
        return "com"
    elif rarity ==1:
        return "rare"
    elif rarity == 2:
        return "epic"
    elif rarity == 3:
        return "legendary"
    return ""