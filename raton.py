#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Mouse of the game. Not the cursor.
"""

# import modules
import pygame
# import random numbers
from random import randint


class Raton():
    """
    The mouse.

    Utilize a segment to represent the mouse, this will be eaten by the snake.
    """

    def __init__(self, screen, settings):
        """Store attributes."""
        # store screen and settings like an attributes
        self.screen = screen
        self.settings = settings

        # size
        self.width = self.settings.raton_width
        self.height = self.settings.raton_height

        # color
        self.color = self.settings.raton_color

        # range positions
        # ranges position of x and y
        self.range_x1 = self.settings.raton_range_pos_x1
        self.range_x2 = self.settings.raton_range_pos_x2
        # ranges of positions of y
        self.range_y1 = self.settings.raton_range_pos_y1
        self.range_y2 = self.settings.raton_range_pos_y2

        # segment that will represent the mouse
        self.image = pygame.Surface((self.width, self.height))

        # fill mouse with color
        self.image.fill(self.color)

        # value of mouse
        self.point = settings.raton_point

        # take rect of the segment
        self.rect = self.image.get_rect()

        # set position
        self.change_position()


    def change_position(self):
        """Set position randomly."""
        self.rect.x = randint(self.range_x1, self.range_x2)
        self.rect.y = randint(self.range_y1, self.range_y2)


    def increase_point(self, settings):
        """Increase the score of scoreboard."""
        self.settings.board_point_initial += self.point


    def is_colliding(self):
        """Return True wheter it's colliding, otherwise False."""
        # take all segments of snake
        segments = self.settings.snake_build_helper[:]
        # iterate over each segments
        for segment in segments:
            # check with their rectangles if they're colliding
            if self.rect.colliderect(segment.rect):
                # if so, return True
                return True
        # otherwise, return False
        return False


    def blitme(self):
        """Blit mouse on its current position."""
        self.screen.blit(self.image, self.rect)
