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
        self.objects_position_list = [(0,0)]

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
        mcgyver = pygame.image.load(mcgyver_image).convert_alpha()
        guardian = pygame.image.load(guardian_image).convert_alpha()

        # Go throught the boardgame list
        line_nb = 0
        for line in self.structure:
			case_nb = 0
			for sprite in line:
				# calcul teh position in pixels
				x = case_nb * sprite_size
				y = line_nb * sprite_size
				if sprite == 'm':		   #m = wall
					window.blit(wall, (x,y))
				elif sprite == 'g':		   #g = guardian
					window.blit(guardian, (x,y))
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
        # Objects collected
        needle = False
        tube = False
        ether = False

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

######   # methode to take object

class Object:
    """Class for the creation of objects"""
    def __init__(self, board, image):
        self.board = board
        self.image = pygame.image.load(image).convert_alpha()
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0

    def generate(self, board):
        """"Chose a random position for an object"""
        position_objet = False
        # Return 2 random numbers for line and case in the board
        while (position_objet != True):
            line_nb = random.randint(0,14)
            case_nb = random.randint(0,14)
            # Verify that it is a good place for the object
            if board.structure[case_nb][line_nb] == '0':
                for tuple in board.objects_position_list:
                    if tuple != (case_nb,line_nb) and position_objet == False:
                        self.case_x = case_nb
                        self.case_y = line_nb
                        self.x = self.case_x * sprite_size
                        self.y = self.case_y * sprite_size
                        board.objects_position_list.append((self.case_x, self.case_y))
                        position_objet = True

    def show(self, window):
        # show object on the window 
        image = self.image
        window.blit(image, (self.x,self.y))
