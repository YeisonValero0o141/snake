#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The snake of the game.
"""

# import modules
import pygame
# import Sprite class
from pygame.sprite import Sprite, Group


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



class SnakeWhole(Group):
    """Represent whole snake with its segments."""

    def __init__(self, screen, settings, fs):
        """Initialize snake with a few segments. Store attributes."""
        # store screen and settings parameter like attributes
        self.screen = screen
        self.settings = settings
        # save modules of functions
        self.fs = fs

        # restore value of movements and tracer of movements. This is
        # useful when user start to play again in a different or same mode of game
        self.fs.reset_values_settings(settings)

        # make segments of snake
        self.make_firsts_segments()

        # call superclass' init. Make group of sprites
        super(SnakeWhole, self).__init__(settings.snake_build_helper)


    def make_firsts_segments(self):
        """Make the firsts segments of snake and add it."""
        # take list of segments
        segments = self.settings.snake_build_helper
        # lenght initial of snake
        lenght = self.settings.length_initial

        # loop up through the inital lenght
        for i in range(lenght):
            # position x and y
            x = self.settings.initial_position_x
            y = self.settings.initial_position_y

            # make segment
            segment = Snake(self.screen, self.settings, x, y)

            # add to the list of segments
            segments.append(segment)


    def move(self):
        """
        Move snake.

        Delete the last segment of snake to emulate that snake is moving.
        """
        # list of segments
        segments = self.settings.snake_build_helper

        # take snake's tail (last segment)
        last_snake_segment = segments.pop()

        # delete the last segment
        self.remove(last_snake_segment)

        # set new segment's position (head)
        x = segments[0].rect.x + self.settings.change_position_x
        y = segments[0].rect.y + self.settings.change_position_y

        # head
        snake = Snake(self.screen, self.settings, x, y)

        # insert head like the first segment (head)
        segments.insert(0, snake)

        # add new segment to snake group
        self.add(snake)

        # update head and tail in settings
        self.settings.snake_head = snake
        self.settings.snake_tail = last_snake_segment


    def is_biting_itself(self):
        """
        Check if snake bite itself.

        If so, return True. Otherwise return False.
        """
        # take a copy of list of segments
        snakes = self.settings.snake_build_helper[:]
        # and snake's head
        snake_head = self.settings.snake_head
        # iterate over its lenght
        for x in range(len(snakes)):
            # the head doesn't count
            if x == 0:
                # do nothing
                pass
            else:
                # pop the last segment
                last_snake_segment = snakes.pop()
                # check if it collide
                if snake_head.rect.colliderect(last_snake_segment.rect):
                    # return True
                    return True
        # otherwise, return False
        return False


    def does_collide_with_walls(self):
        """
        Check wheter snake collide with the walls or not.

        Return True if so, otherwise return False.
        """
        # take snake's head
        snake = self.settings.snake_head
        # return True if at least colllide with one wall
        if snake.rect.top < 0:
            return True
        elif snake.rect.bottom > 545:
            return True
        elif snake.rect.left < 0:
            return True
        elif snake.rect.right > 1028:
            return True
        # otherwise, return False
        else:
            return False
