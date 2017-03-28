#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The snake of the game.
"""

# import modules
import pygame
# import Sprite class
from pygame.sprite import Sprite


class Snake(Sprite):
    """
    Snake.

    Use littles segments to represent a snake.
    """

    def __init__(self, screen, settings, position_x, position_y):
        """Store all attributes."""
        # initialize superclass
        super(Snake, self).__init__()
        # store screen and settings
        self.screen = screen
        self.settings = settings

        # take rectangle of screen
        self.screen_rect = self.screen.get_rect()

        # load image of snake
        self.image = pygame.image.load("images/snake.png")

        # take rectangles of image
        self.rect = self.image.get_rect()

        # set initial position
        self.rect.x = position_x
        self.rect.y = position_y

        # load bite sound
        self.sound_bite = pygame.mixer.Sound('sonidos/mordisco.wav')
