#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Snake Game.
"""

# import modules
# import random number from standard library
from random import randint
# import pygame library
import pygame
# import game's settings
from settings import Settings
# import game's functions with the alias of fs
import functions_snake as fs
# import Snake
from snake import SnakeWhole
# import mouse
from raton import Raton
# import scoreboard
from score_board import ScoreBoard
# import main menu
from mainboard import MainBoard


def main():
    """The function that will run the game."""
    # initialize pygame's engine
    pygame.init()

    # instance Settins class
    settings = Settings()

    # set size's screen and open it
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
    snake_whole = SnakeWhole(screen, settings, fs)

    # pygame's clock
    clock = pygame.time.Clock()

    # counter to avoid sudden movemensts
    counter = settings.counter_time_between_movements

    # hide cursor
    pygame.mouse.set_visible(False)

    # main loop
    while True:
        # set fps
        clock.tick(10)

        # update snake's position
        snake_whole.update()

        # update scoreboard
        score_board.update()

        # wheter game is not paused
        if not settings.pause:
            # increase counter
            counter += 1

        # update counter of movements of settings
        settings.counter_time_between_movements = counter

        # check events of game
        fs.check_events(screen, counter, mainboard, settings, snake_whole)

        # wheter the game isn't on the main menu and
        # game doesn't be paused
        if not settings.main_menu and not settings.pause:
            # move snake
            snake_whole.move()

        # just on game mode 2
        if settings.play_2:
            # change positions wheter snake achieve any borders
            snake_whole.snake_achieve_walls()

        # see wheter snake is dead or not. Just if the game isn't
        # on main menu
        if snake_whole.is_snake_dead() and not settings.main_menu:
            # pause game
            fs.pause(0.40)
            # change flags to appear main menu
            fs.change_flags(settings)
            # check if a record was beat
            mainboard.check_beat_record()
            # reinstance snake to restore inital values
            snake_whole = SnakeWhole(screen, settings, fs)
            # if so, wait until user finish to write his/her name
            fs.wait_write_name(screen, settings, mainboard,
                                                score_board)


        # check if one bitten have occurred. Just if the game
        # isn't on main menu
        if raton.is_colliding() and not settings.main_menu:
            # play bite sound
            settings.snake_head.sound_bite.play()

            # increase lenght of snake
            snake_whole.increase_lenght_of_snake()

            # change position of mouse
            raton.change_position()

            # increase score of scoreboard
            raton.increase_point(settings)

            # call the method again to know if it's still colliding
            while raton.is_colliding():
                # change position of mouse
                raton.change_position()

        # update all objects in screen
        fs.update_screen(screen, raton, snake_whole, raton, settings, score_board, mainboard)


if __name__ == "__main__":
    # run game
    main()
