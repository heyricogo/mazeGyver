#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""Game classes for the MazeGyver game"""

import pygame
import random
import json
from pygame.locals import *
from constants import *


class Board:
    """Classe for the creation of the boardgame"""

    def __init__(self, file):
        self.file = file
        self.structure = 0
        self.items_position_list = {'needle': (
            0, 0), 'tube': (0, 0), 'ether': (0, 0), 'n':0, 't':0,'e':0}

    def generate(self):
        """Methode to generate the boardgame"""
        # Open the file
        with open(self.file, "r") as file:
            board_structure = []
            for line in file:
                board_line = []
                for sprite in line:
                    # Ignore "\n" at the end of the line
                    if sprite != '\n':
                        # Append the sprite to the board_line
                        board_line.append(sprite)
                        # Append the line to the board
                board_structure.append(board_line)
                # Save the boardgame structure
            self.structure = board_structure

    def show(self, window):
        """Methode to show the boardgame in the windows game"""
        # Load images
        wall = pygame.image.load(wall_image).convert_alpha()
        guardian = pygame.image.load(guardian_image).convert_alpha()

        # Go throught the boardgame list
        line_nb = 0
        for line in self.structure:
            case_nb = 0
            for sprite in line:
                                # calcul the position in pixels
                x = case_nb * sprite_size
                y = line_nb * sprite_size
                if sprite == 'm':  # m = wall
                    window.blit(wall, (x, y))
                elif sprite == 'g':  # g = guardian
                    window.blit(guardian, (x, y))
                case_nb += 1
            line_nb += 1


class Mcgyver:
    """Class for the creation of McGyver"""

    def __init__(self, board):
        self.board = board
        self.image = pygame.image.load(mcgyver_image).convert_alpha()
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0
        # Items collected
        self.needle = False
        self.tube = False
        self.ether = False

    def move(self, direction):
        """Move McGyver"""
        # Right move
        if direction == 'right':
            # To stay in the board
            if self.case_x < (number_sprite - 1):
                # Verify that the destination case is not a wall
                if self.board.structure[self.case_y][self.case_x+1] != 'm':
                    # Move to the case
                    self.case_x += 1
                    # Calculate the real position in pixels
                    self.x = self.case_x * sprite_size

                # left move
        if direction == 'left':
            if self.case_x > 0:
                if self.board.structure[self.case_y][self.case_x-1] != 'm':
                    self.case_x -= 1
                    self.x = self.case_x * sprite_size

                # up move
        if direction == 'up':
            if self.case_y > 0:
                if self.board.structure[self.case_y-1][self.case_x] != 'm':
                    self.case_y -= 1
                    self.y = self.case_y * sprite_size

                # down move
        if direction == 'down':
            if self.case_y < (number_sprite - 1):
                if self.board.structure[self.case_y+1][self.case_x] != 'm':
                    self.case_y += 1
                    self.y = self.case_y * sprite_size
        
        self.item_taken()
        
        # variable dans dict pour dire que item pris ou pas

    # methode to verify if McGyver takes an item
    def item_taken(self):
        for key, value in self.board.items_position_list.items():
            if value == (self.case_x, self.case_y):
                if key == 'needle':
                    self.needle = True
                    self.board.items_position_list['n'] = 1
                if key == 'tube':
                    self.tube = True
                    self.board.items_position_list['t'] = 1
                if key == 'ether':
                    self.ether = True
                    self.board.items_position_list['e'] = 1


class Item:
    """Class for the creation of objects"""

    def __init__(self, board, image):
        self.board = board
        # self.image = pygame.image.load(image).convert()
        self.image_name = image
        self.image = image
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0

    def generate(self, board):
        """"Chose a random position for an object"""
        position_item = False
        # Return 2 random numbers for line and case in the board
        while (position_item != True):
            case_nb = random.randint(0, 14)
            line_nb = random.randint(0, 14)
            # Verify that it is a good place for the object
            if board.structure[case_nb][line_nb] == '0':
                for key, value in board.items_position_list.items():
                    if value == (0, 0):
                        if value != (case_nb, line_nb) and position_item == False:
                            # board.structure[case_nb][line_nb] == 'i'
                            self.case_x = case_nb
                            self.case_y = line_nb
                            self.x = self.case_x * sprite_size
                            self.y = self.case_y * sprite_size
                            board.items_position_list[key] = (case_nb, line_nb)
                            position_item = True

    def show(self, window):
        # show object on the window
        if self.image_name == needle_image:
            if self.board.items_position_list['n'] == 0:
                image = pygame.image.load(needle_image).convert()
                window.blit(image, (self.x, self.y))
        if self.image_name == tube_image:
            if self.board.items_position_list['t'] == 0:
                image = pygame.image.load(tube_image).convert()
                window.blit(image, (self.x, self.y))
        if self.image_name == ether_image:
            if self.board.items_position_list['e'] == 0:
                image = pygame.image.load(ether_image).convert()
                window.blit(image, (self.x, self.y))
