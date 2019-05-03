#!/usr/bin/python3
# -*- coding: Utf-8 -*

import pygame
from pygame.locals import *

from classes import *
from constants import *

pygame.init()

try:
    # Open the Pygame window
    window = pygame.display.set_mode((window_side, window_side))
    #Icone
    icon = pygame.image.load(icon_image)
    pygame.display.set_icon(icon)
    #Titre
    pygame.display.set_caption(window_title)

    # Load background image
    background = pygame.image.load("background.jpg").convert()
    window.blit(background, (0,0))

    # Genarate the boardgame
    board = Board(n1)
    board.generate()
    board.show(window)

    # Generate McGyver
    mcgyver = Mcgyver(board)

    # Refesh window
    pygame.display.flip()

    # Multiple move
    pygame.key.set_repeat(400,30)

    # Game loop
    loop = 1
    while loop:
        for event in pygame.event.get():                                                    # We go through the list of all the events received
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:       # If any of these events are of type QUIT
                loop = 0                                                               # Stop loop

            # McGyver Move
            elif event.key == K_RIGHT:
                mcgyver.move('right')
            elif event.key == K_LEFT:
                mcgyver.move('left')
            elif event.key == K_UP:
                mcgyver.move('up')
            elif event.key == K_DOWN:
                mcgyver.move('down')

    # New position
    window.blit(background, (0,0))
    board.show(window)
    pygame.display.flip()

    # Victoiry
    if board.structure[mcgyver.case_y][mcgyver.case_x] == 'g':
        loop = 0

finally:
    pygame.quit()
    exit()
