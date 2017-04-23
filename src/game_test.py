#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Test all characters of game.
"""
import unittest
import sys

import pygame

sys.dont_write_bytecode = True

from settings import Settings
import functions_snake as fs
from snake import Snake

pygame.init()

# some objects needed by some objects
settings = Settings()
size = (settings.screen_width, settings.screen_height)
screen = pygame.display.set_mode(size)

class TestSnake(unittest.TestCase):
    """Test for all methods of Snake class."""

    def test_make_the_right_firsts_segments(self):
        """Test make_firsts_segments method."""
        length_initial = settings.length_initial
        snake = Snake(screen, settings, fs, '../sounds/mordisco.wav')
        self.assertEqual(len(snake), length_initial, msg='Snake len ({0}) is not {1}'.format(len(snake), length_initial))


    def test_increase_lenght(self):
        """Test increase_lenght method."""
        snake = Snake(screen, settings, fs, '../sounds/mordisco.wav')
        len_snake = len(settings.snake_build_helper)

        for x in range(1, 51):
            expected_len = len_snake + x
            snake.increase_lenght()
            self.assertEqual(len(snake), expected_len, msg='the increase failed beacause {0} is not equal than {1}'.format(len(snake), expected_len))

    def test_collide_with_walls(self):
        """Test does_collide_with_walls method."""
        snake = Snake(screen, settings, fs, '../sounds/mordisco.wav')
        head = settings.snake_head
        # this positions colllide with walls
        bad_positions = [
            (-1, 389), (569, 1000), (-1, -1),
            (1029, 545), (-438, -39), (1284, 600)
        ]
        # this ones don't
        well_positions = [
            (1005, 520), (893, 100), (338, 131),
            (540, 301), (16, 281), (789, 102)
        ]

        for bad_pos in bad_positions:
            # change head's position
            head.rect.x = bad_pos[0]
            head.rect.y = bad_pos[1]
            self.assertTrue(snake.does_collide_with_walls(), msg='position {} is not wrong'.format(bad_pos))

        for well_pos in well_positions:
            # change head's position
            head.rect.x = well_pos[0]
            head.rect.y = well_pos[1]
            self.assertFalse(snake.does_collide_with_walls(), msg='positions {} is wrong'.format(well_pos))


    def test_achieve_walls(self):
        """Test achive_walls method."""
        snake = Snake(screen, settings, fs, '../sounds/mordisco.wav')
        head = settings.snake_head
        # change position of snake's head
        head.rect.y = -45
        snake.achieve_walls()
        self.assertEqual(head.rect.y, 525)



if __name__ == '__main__':
    unittest.main()
