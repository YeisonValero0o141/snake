#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Settings of the game.
"""

# import module
import pygame


class Settings():
    """
    Contains all settings of the game.

    Like size of screen, background color, size of snake, and so on.
    Even messages to be shown and data to store.
    """

    def __init__(self):
        """Store all data"""
        ######## Screen ########
        # size
        self.screen_width = 1025
        self.screen_height = 545
        # background color
        self.background_color = (96, 125, 139)


        ######## Mouse ########
        # size
        self.raton_width = 16
        self.raton_height = 16
        # color
        self.raton_color = (121, 85, 72)
        # score
        self.raton_point = 1

        # positions of mouse
        # first range position of x
        self.raton_range_pos_x1 = 6
        # second range position of x
        self.raton_range_pos_x2 = 1004

        # first range position of x
        self.raton_range_pos_y1 = 9
        # second range position of y
        self.raton_range_pos_y2 = 522


        ######## Wall ########
        self.wall_size = 10
        self.wall_color = (33, 33, 33)
        # set position of walls. 1 it's start position and 2 it's the last one
        self.wall_position_up_1 = (0, 3)
        self.wall_position_up_2 = (1023, 3)
        self.wall_position_down_1 = (0, 542)
        self.wall_position_down_2 = (1023, 542)
        self.wall_position_left_1 = (0, 2)
        self.wall_position_left_2 = (0, 542)
        self.wall_position_right_1 = (1023, 2)
        self.wall_position_right_2 = (1023, 542)

        # will contains all position of walls
        self.wall_positions = [
            [self.wall_position_up_1, self.wall_position_up_2],
            [self.wall_position_down_1, self.wall_position_down_2],
            [self.wall_position_right_1, self.wall_position_right_2],
            [self.wall_position_left_1, self.wall_position_left_2]
         ]


        ######## Snake ########

        # initial length
        self.length_initial = 5

        # width, height and margin
        self.snake_width = 16
        self.snake_height = 15
        self.snake_margin = 3

        # color
        self.snake_color = (255, 255, 255)

        # posición inicial
        self.initial_position_x = 450 - (self.snake_width + self.snake_margin)
        self.initial_position_y = 230

        # how far the snake wil move
        self.change_position_x = self.snake_height + self.snake_margin
        self.change_position_y = 0
        # will contain all segments of snake
        self.snake_build_helper = []
        # first segment of snake (head)
        self.snake_head = None
        # last segment of snake (tail)
        self.snake_tail = None

        # lists to avoid sudden change in the manage of snakge
        self.traceback_movements = ["K_RIGHT"]
        self.traceback_counter = [0]
        # counter to avoid sudden and fast movements
        self.counter_time_between_movements = 0


        ######## SCOREBOARD ########
        self.board_width = 30
        self.board_height = 10
        self.board_point_initial = 0
        # font of scoreboard
        self.text_color_score = (30, 30, 30)
        self.text_scores = "Score: "
        self.text_highest_score = "Highest Score: "
        # flag to know if player won
        self.play_won = False
        # max score. If player achieve this score, s/he will win.
        #  3 it's beacause of walls, will count for both game modes
        self.max_score = ((self.screen_width - 3) // self.raton_width) * ((self.screen_height - 3) // self.raton_height)
        self.congra_message = "You have won!"
        self.congra_size = (300, 80)
        self.congra_pos = (380, 220)

        ######## RECORD NAME ########
        # will contains the name of beater
        self.name_of_beater = []
        # flag. By default, il will be False because the user doesn't start writing its name
        self.write_finish = False
        # lenght of letter allowed
        self.allowed_number_letter = 16



        ######## MAIN MENU ########
        self.text_mainboard_1 = "Play 1"
        self.text_mainboard_2 = "Play 2"
        self.text_mainboard_3 = "Exit"
        # color of the first text (white)
        self.text_mainboard_color_1 = (250, 250, 250)
        # color black to mark defferent
        self.text_mainboard_color_2 = (0, 0, 0)
        # flags to decide what menu or game mode the game is in
        self.main_menu = True
        self.play_1 = False
        self.play_2 = False
        # tracer of the options ch
        self.traceback_cursor = ["Play 1"]



        ######## PAUSE ########
        # flag
        self.pause = False
        # text to draw on screen
        self.pause_text = "PAUSE"
        # text's color
        self.pause_color_text = (55, 71, 79)
        # x and y position will be in the middle of screen
        self.pause_position_y = 225
        self.pause_position_x = 430
        # width text
        self.pause_width = 150
        self.pause_height = 70
        # size font
        self.pause_size_font = 60
