#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The snake of the game.
"""

# import modules
import pygame
# import Sprite class
from pygame.sprite import Sprite, Group


class Segment(Sprite):
    """
    It will be utilized to represent a snake.
    """

    def __init__(self, screen, settings, position_x, position_y):
        """Store all attributes."""
        # initialize superclass
        super(Segment, self).__init__()
        # store screen and settings
        self.screen = screen
        self.settings = settings

        # take rectangle of screen
        self.screen_rect = self.screen.get_rect()

        # store height and width
        self.height = settings.snake_height
        self.width =  settings.snake_width

        # color
        self.color = settings.snake_color

        # load image of snake
        # create a square to represent the snake
        self.image = pygame.Surface((self.height, self.width))

        # fill with white
        self.image.fill(self.color)

        # take rectangles of image
        self.rect = self.image.get_rect()

        # set initial position
        self.rect.x = position_x
        self.rect.y = position_y



class Snake(Group):
    """Represent whole snake with segments."""

    def __init__(self, screen, settings, fs):
        """Initialize snake with a few segments. Store all attributes too."""
        # store screen and settings parameter like attributes
        self.screen = screen
        self.settings = settings
        # save modules of functions
        self.fs = fs

        # store height and margin
        self.height = settings.snake_height
        self.margin = settings.snake_margin

        # get rectangle of screen
        self.screen_rect = self.screen.get_rect()

        # restore value of movements and tracer of movements. This is
        # useful when user start to play again in a different or same mode of game
        self.fs.reset_values_settings(settings)

        # load bite sound
        self.sound_bite = pygame.mixer.Sound('sounds/mordisco.wav')

        # make segments of snake
        self.make_firsts_segments()

        # call superclass' init. Make group of sprites
        super(Snake, self).__init__(settings.snake_build_helper)


    def play_sound_bite(self):
        """Play sound bite."""
        self.sound_bite.play()


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
            segment = Segment(self.screen, self.settings, x, y)

            # add to the list of segments
            segments.append(segment)

        # update snake' head in settings
        self.settings.snake_head = segments[0]


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
        snake = Segment(self.screen, self.settings, x, y)

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


    def is_snake_dead(self, play_1=False):
        """If snake is dead change flag variable, if not, keep the
        same vaue."""
        # first check is snake bite itself
        if self.is_biting_itself():
            return True
        # snake just collide with walls in the first mode game
        elif self.does_collide_with_walls() and self.settings.play_1:
            return True
        # otherwise, False
        else:
            return False


    def increase_lenght(self):
        """
        Increase snake by one segment.

        The segment, it will be appended at last segment.
        """
        # take all segments
        segments = self.settings.snake_build_helper
        # take the last segments to use its position to
        # append the new segment
        last_segment = self.settings.snake_tail

        # utilize last_segment's position to set position of the new segment
        x = last_segment.rect.x
        y = last_segment.rect.y

        # create new sement at the end of the snake (the tail)
        last_segment = Segment(self.screen, self.settings, x, y)

        # append segment in the list of segments
        segments.append(last_segment)

        # add the new segment to the snake
        self.add(last_segment)


    def achieve_walls(self):
        """
        Change position if snake achieve any borders of screen.
        """
        # take snake's head
        snake = self.settings.snake_head
        # wheter snake achive top of border
        if snake.rect.top < self.screen_rect.top:
            # change its position
            snake.rect.y = 525
        # wheter snake achive bottom of border
        elif snake.rect.bottom > self.screen_rect.bottom:
            # change its postion
            snake.rect.y = 5
        # if snake achive left side border of screen
        elif snake.rect.left < 0:
            # change its position
            snake.rect.x = 1000
        # if snake achive right side border of screen
        elif snake.rect.right > 1023:
            # change its position
            snake.rect.x = 5 + 1

        # update settings's variable
        self.settings.snake_head = snake


    def move_up(self):
        """Change variables of directions to go upward."""
        self.settings.change_position_x = 0
        self.settings.change_position_y =  (self.height + self.margin) * -1


    def move_down(self):
        """Change variables of directions to go downward."""
        self.settings.change_position_x = 0
        self.settings.change_position_y = self.height + self.margin


    def move_left(self):
        """Change variables of directions to go leftward."""
        self.settings.change_position_x = (self.height + self.margin) * -1
        self.settings.change_position_y = 0


    def move_right(self):
        """Change variables of directions to go rightward."""
        self.settings.change_position_x = self.height + self.margin
        self.settings.change_position_y = 0
