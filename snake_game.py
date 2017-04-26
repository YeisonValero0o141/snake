#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Snake Game.
"""

# import modules
import sys
from random import randint

import pygame

# to avoid pyc files in python 2
sys.dont_write_bytecode = True

from src.settings import Settings
import src.functions_snake as fs
from src.snake import Snake
from src.raton import Raton
from src.score_board import ScoreBoard
from src.mainboard import MainBoard


def main():
    """The function that will run the game."""
    # initialize pygame's engine
    pygame.init()

    # instance Settins class
    settings = Settings()

    # set size's screen
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    # set title's screen
    pygame.display.set_caption("Snake")

    # scoreboard
    score_board = ScoreBoard(screen, settings)

    # main menu
    mainboard = MainBoard(screen, settings)

    #  mouse
    raton = Raton(screen, settings)

    # snake
    snake = Snake(screen, settings, fs)

    # pygame's clock
    clock = pygame.time.Clock()

    # counter to avoid sudden movemensts
    counter = settings.counter_time_between_movements

    # hide cursor
    pygame.mouse.set_visible(False)

    # main loop
    while True:
        # set fps
        clock.tick(11)

        # wheter game is neither nor paused
        if not settings.pause and not settings.main_menu:
            # update snake's position
            snake.update()

            # update scoreboard
            score_board.update()

            # increase counter
            counter += 1

            # update counter of movements of settings
            settings.counter_time_between_movements = counter

        # wheter the game isn't on the main menu and
        # game doesn't be paused
        if not settings.main_menu and not settings.pause:
            # move snake
            snake.move()

        # just on game mode 2
        if settings.play_2 and not settings.main_menu:
            # change positions wheter snake achieve any borders
            snake.achieve_walls()

        # see wheter snake is dead or just player won game
        # Just if the game isn'ton main menu
        if snake.is_snake_dead() or settings.play_won and not settings.main_menu:

            if settings.play_won:
                fs.pause(2)
            else:
                fs.pause(0.40)

            # change flags to appear main menu
            fs.change_flags(settings)
            # check if a record was beat
            mainboard.check_beat_record()
            # reinstance snake to restore inital values
            snake = Snake(screen, settings, fs)
            # if so, wait until user finish to write his/her name
            fs.wait_write_name(screen, settings, mainboard, score_board)


        # check if one bitten have occurred. Just if the game
        # isn't on main menu
        if raton.is_colliding() and not settings.main_menu:
            # play bite sound
            snake.play_sound_bite()

            # increase lenght of snake
            snake.increase_lenght()

            # change position of mouse
            raton.change_position()

            # increase score of scoreboard
            raton.increase_point()

            # call the method again to know if it's still colliding or not
            while raton.is_colliding():
                # change position of mouse again
                raton.change_position()

        # check if player won
        score_board.max_score_was_achieved()

        # check events of game
        fs.check_events(screen, counter, mainboard, settings, snake)

        # update all objects in screen
        fs.update_screen(screen, raton, snake, raton, settings,
                                score_board, mainboard)


if __name__ == "__main__":
    main()
