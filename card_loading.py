import json
import random

def load_deck(deck_name):
    json_data = open('decks/'+deck_name+'.json')
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


    
