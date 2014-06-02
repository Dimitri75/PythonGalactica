import pygame
from pygame.locals import *
from credits_func import *
from options_func import *
from game_func import *


###### Main Function ######
#(1) Initialize Game Menu #
def main(): 
    pygame.init()
     
    fenetre = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Galactica")
    continuer = 1
     
    fond = pygame.image.load("images/background.jpg").convert()
    title = pygame.image.load("images/title.png").convert()
    button_play = pygame.image.load("images/play_no_highlight.jpg").convert()
    button_play_h = pygame.image.load("images/play_highlight.jpg").convert()
    button_deck = pygame.image.load("images/deck_no_highlight.jpg").convert()
    button_deck_h = pygame.image.load("images/deck_highlight.jpg").convert()
    button_options = pygame.image.load("images/options_no_highlight.jpg").convert()
    button_options_h = pygame.image.load("images/options_highlight.jpg").convert()
    button_credits = pygame.image.load("images/credits_no_highlight.jpg").convert()
    button_credits_h = pygame.image.load("images/credits_highlight.jpg").convert()
    button_quit = pygame.image.load("images/quit_no_highlight.jpg").convert()
    button_quit_h = pygame.image.load("images/quit_highlight.jpg").convert()
    fenetre.blit(fond, (0,0))
    fenetre.blit(title, (165,0))
    fenetre.blit(button_play, (257,123))
    fenetre.blit(button_deck, (257,172))
    fenetre.blit(button_options, (257,221))
    fenetre.blit(button_credits, (257,270))
    fenetre.blit(button_quit, (257,319))
    pygame.display.flip()
    play_r = button_play.get_rect()
    play_r.x, play_r.y = 257, 123
    deck_r = button_deck.get_rect()
    deck_r.x, deck_r.y = 257, 172
    options_r = button_options.get_rect()
    options_r.x, options_r.y = 257, 221
    credits_r = button_credits.get_rect()
    credits_r.x, credits_r.y = 257, 270
    quit_r = button_quit.get_rect()
    quit_r.x, quit_r.y = 257, 319

    while continuer:
        menu_routine(fenetre)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                #Bouton QUIT
                if ( x in range(257,383)) and (y in range(319,348)):
                    continuer = 0
                #Bouton PLAY
                elif ( x in range(257,383)) and (y in range (123,152)):
                    game_main(fenetre)
                #Bouton DECK BUILDER
                elif ( x in range(257,383)) and (y in range (172,201)):
                    print("Bouton deck builder")
                #Bouton CREDITS
                elif ( x in range(257,383)) and (y in range (270,299)):
                    credits_print(fenetre)
                #Bouton OPTIONS
                elif ( x in range(257,383)) and (y in range (221,250)):
                    options_print(fenetre)
                        
        if quit_r.collidepoint(pygame.mouse.get_pos()):
            fenetre.blit(button_quit_h, (257,319))
            pygame.display.flip()
        elif play_r.collidepoint(pygame.mouse.get_pos()):
            fenetre.blit(button_play_h, (257,123))
            pygame.display.flip()
        elif deck_r.collidepoint(pygame.mouse.get_pos()):
            fenetre.blit(button_deck_h, (257,172))
            pygame.display.flip()
        elif options_r.collidepoint(pygame.mouse.get_pos()):
            fenetre.blit(button_options_h, (257,221))
            pygame.display.flip()
        elif credits_r.collidepoint(pygame.mouse.get_pos()):
            fenetre.blit(button_credits_h, (257,270))
            pygame.display.flip()
    pygame.quit()

def menu_routine(fenetre):
    pygame.display.set_caption("Galactica")
    fond = pygame.image.load("images/background.jpg").convert()
    title = pygame.image.load("images/title.png").convert()
    button_play = pygame.image.load("images/play_no_highlight.jpg").convert()
    button_deck = pygame.image.load("images/deck_no_highlight.jpg").convert()
    button_options = pygame.image.load("images/options_no_highlight.jpg").convert()
    button_credits = pygame.image.load("images/credits_no_highlight.jpg").convert()
    button_quit = pygame.image.load("images/quit_no_highlight.jpg").convert()
    fenetre.blit(fond, (0,0))
    fenetre.blit(title, (165,0))
    fenetre.blit(button_play, (257,123))
    fenetre.blit(button_deck, (257,172))
    fenetre.blit(button_options, (257,221))
    fenetre.blit(button_credits, (257,270))
    fenetre.blit(button_quit, (257,319))
    pygame.display.flip()
    
if __name__ == "__main__":
    main()
