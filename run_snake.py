#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Snake Game
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
# se importa el módulo para tratar muchos sprite como grupos
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

    # se establece el tamaño de la ventana
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

    while True:
        # variables tipo bandera para saber si el usuario quiere juegar
        main_menu = settings.main_menu
        play_1 = settings.play_1
        play_2 = settings.play_2

        # set fps
        clock.tick(10)

        if main_menu:
            fs.main_menu(screen, settings, score_board, mainboard)

        # update snake's position
        snake_whole.update()

        # update scoreboard
        score_board.update()

        # increase counter
        counter += 1

        # update counter of movements of settings
        settings.counter_time_between_movements = counter

        # check events of game
        fs.check_events(counter, settings, snake_whole)

        # move snake
        snake_whole.move()

        # see if snake is biting itself
        snake_bite_itself = snake_whole.is_biting_itself()

        if snake_whole.is_snake_dead(play_1=True):
            # pause game
            fs.pause(0.40)
            # change flags to appear main menu
            fs.change_flags(settings)
            # reinstance snake to restore inital values
            snake_whole = SnakeWhole(screen, settings, fs)
            # check if a record was beat
            mainboard.check_beat_record()
            # if so, wait until user finish to write his/her name
            fs.wait_write_name(screen, settings, mainboard,
                                                    score_board)

        # check if one bitten have occurred
        if raton.is_colliding():
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
        fs.update_screen(screen, raton, snake_whole, raton, settings, score_board)


if __name__ == "__main__":
    # run game
    main()
