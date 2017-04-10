#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Functions of the game.

Functions such as: check events of game, draw all objects, close
game, pause game and so on.
"""

# import modules
# sys from library standard
import sys
# sleep function of time
from time import sleep
# pygame library
import pygame
# pygame's font
import pygame.font
# Snake class
from snake import Snake
# Raton (mouse) class
from raton import Raton

#####################################
#####    IMPORTANT FUNCTIONS    #####
#####################################
def update_screen(screen, raton, snake_whole, ratones, settings, score_board, mainboard):
    """Update screen."""
    # fill screen with the background color
    screen.fill(settings.background_color)

    # wheter main menu is running
    if settings.main_menu:
        # the main menu, it's the only one is drawn
        draw_menu(settings, mainboard)
    else:
        # just draw them if it's on game mode 1
        if settings.play_1:
            # draw the walls on borders
            draw_walls(screen, settings)

        # blit scoreboard
        score_board.blitme()

        # blit mouse
        raton.blitme()

        # draw snake
        snake_whole.draw(screen)

        # if and only if the game is not paused
        if settings.pause:
            # draw a rect on screen
            draw_rect_text_pause(screen, settings)

    # flip screen
    pygame.display.flip()


def check_events(screen, counter, mainboard, settings, snake_whole):
    """
    Check events of game.
    Such as: move snake, close game and write name.
    """
    # take all events of game
    for event in pygame.event.get():
        # if user press x in the tile bar
        if event.type == pygame.QUIT:
            exit()
        # wheter user press any buttons
        elif event.type == pygame.KEYDOWN and not settings.main_menu:
            change_snake_direction(event, counter, settings, snake_whole)

        if event.type == pygame.KEYDOWN and settings.main_menu:
            # move cursor and see if user pick a choice
            main_menu(event, settings, mainboard)


def exit():
    """Close game."""
    sys.exit()


def pause(seconds):
    """Pause game by n seconds."""
    sleep(seconds)

####### FUCNTION TO DRAW WALLS #######
def draw_walls(screen, settings):
    """Draw walls on border of screen."""
    # list with all positions of walls
    positions = settings.wall_positions
    # wall's size
    size = settings.wall_size
    # wall's color
    color = settings.wall_color
    # iterate over the list of all positions
    for position in positions:
        # draw wall
        pygame.draw.line(screen, color, position[0], position[1], size)

####### FUCNTIONS FOR SNAKE #######
def reset_values_settings(settings):
    """
    Reset values tracer of movements, positions, score and segments.

    This make sure that when user start again to play snake
    appears in the initial position and not the last one
    """
    # come back to the initial position
    settings.change_position_y = 0
    settings.change_position_x = settings.snake_width + settings.snake_margin
    # score
    settings.board_point_initial = 0
    # list of segments
    settings.snake_build_helper = []
    # tracer of movements
    settings.traceback_movements = ["K_RIGHT"]


def clean_tracers(traceback_movements, counter_move_now):
    """Remove the first elements of the list of tracer movements
    and counter."""
    del traceback_movements[0]
    del counter_move_now[0]


def add_rastreo_tracer(traceback_movements, counter_move_now, movement, counter):
    """Add the trace to the tracer movements and counter."""
    traceback_movements.append(movement)
    counter_move_now.append(counter)


def change_snake_direction(event, counter, settings, snake_whole):
    """
    Move snake and does not allow sudden movements like opposite
    movements.

    For example if snake is going to lefward avoid snake go to
    rightward. Also avoid movements in the same second.
    """

    # take tracer of movements and counter
    traceback_movements = settings.traceback_movements
    counter_move_now = settings.traceback_counter

    # wheter it's not same second and movement is not the opposite.
    # Also if the is not paused. This apply for all conditionals
    if event.key == pygame.K_UP and not settings.pause:
        if not traceback_movements[-1] == "K_DOWN" and not counter == counter_move_now[-1]:
            # move up
            snake_whole.move_up()

            # add trace of movements and counter to the tracer
            add_rastreo_tracer(traceback_movements, counter_move_now,
            "K_UP", counter)

            # remove the first item of list of both tracer
            clean_tracers(traceback_movements, counter_move_now)

    elif event.key == pygame.K_DOWN and not settings.pause:
        if not traceback_movements[-1] == "K_UP" and not counter == counter_move_now[-1]:
            # move downward
            snake_whole.move_down()

            # add trace of movements and counter to the tracer
            add_rastreo_tracer(traceback_movements, counter_move_now,
            "K_DOWN", counter)

            # remove the first item of list of both tracer
            clean_tracers(traceback_movements, counter_move_now)

    elif event.key == pygame.K_LEFT and not settings.pause:
        if not traceback_movements[-1] == "K_RIGHT" and not counter == counter_move_now[-1]:
            # move left
            snake_whole.move_left()

            # add trace of movements and counter to the tracer
            add_rastreo_tracer(traceback_movements, counter_move_now,
            "K_LEFT", counter)

            # remove the first item of list of both tracer
            clean_tracers(traceback_movements, counter_move_now)


    elif event.key == pygame.K_RIGHT and not settings.pause:
        if not traceback_movements[-1] == "K_LEFT" and not counter == counter_move_now[-1]:
            # move right
            snake_whole.move_right()

            # add trace of movements and counter to the tracer
            add_rastreo_tracer(traceback_movements, counter_move_now,
            "K_RIGHT", counter)

            # remove the first item of list of both tracer
            clean_tracers(traceback_movements, counter_move_now)


    elif event.key == pygame.K_SPACE:
        # pause game
        pause_game(settings)



####### PAUSE #######
def pause_game(settings):
    """Change flag to pause game."""
    # change value. This is to utilize the function to
    # pause and remove pause
    settings.pause = not settings.pause


def draw_rect_text_pause(screen, settings):
    """Draw text of pause on screen."""
    # color
    color = settings.pause_color_text
    # positions
    positions = (settings.pause_position_x, settings.pause_position_y)
    # size
    size = (settings.pause_width, settings.pause_height)
    # draw rect of pause
    pygame.draw.rect(screen, color, (positions[0], positions[1],
    size[0], size[1]))
    # dra message in rect
    draw_text_pause(screen, settings)


def draw_text_pause(screen, settings):
    """Draw text of pause in rect of pause."""
    # take text and color. Use the same of snake
    text = settings.pause_text
    color = settings.snake_color
    # background color
    background_color = settings.pause_color_text
    # size font
    size_font = settings.pause_size_font
    # font
    font = pygame.font.SysFont(None, size_font)
    # message to draw
    message = font.render(text, True, color, background_color)
    # get rect of message
    message_rect = message.get_rect()
    # set position
    message_rect.x = 434
    message_rect.y = 237
    # blit message
    screen.blit(message, message_rect)


####### FUNCTIONS FOR MAIN MENU #######
def move_cursor(event, mainboard, settings):
    """
    Check wheter user moves cursor or pick a choice.
    """
    if event.key == pygame.K_UP or event.key == pygame.K_LEFT:
        # change color of text 1
        mainboard.change_color_text1()
        # and add it to the tracer of cursor
        settings.traceback_cursor.append("Play 1")

    elif event.key == pygame.K_RIGHT:
        # change color of text 2
        mainboard.change_color_text2()
        # add it to the tracer of cursor
        settings.traceback_cursor.append("Play 2")

    elif event.key == pygame.K_DOWN:
        # change color of text 3
        mainboard.change_color_text3()
        # add it to tracer of cursor
        settings.traceback_cursor.append(False)

    elif event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
        # see what game mode user choice
        if settings.traceback_cursor[-1] == "Play 1":
            # change flag to play 1 game mode
            flag_play(settings, settings.traceback_cursor[-1])
        elif settings.traceback_cursor[-1] == "Play 2":
            # change flag to play 2 game mode
            flag_play(settings, settings.traceback_cursor[-1])
        elif settings.traceback_cursor[-1] == False:
            exit()


def flag_play(settings, play):
    """Change flags to run one the game modes."""
    if play == "Play 1":
        settings.play_1 = True
        settings.play_2 = False
    elif play == "Play 2":
        settings.play_1 = False
        settings.play_2 = True

    settings.main_menu = False


def change_flags(settings):
    """Change flags to appears main menu."""
    settings.play_1 = False
    settings.play_2 = False
    settings.main_menu = True

def main_menu(event, settings, mainboard):
    """
    If user pressed one of the key arrows, move cursor or enter
    in one game move.
    """
    move_cursor(event, mainboard, settings)
    # clean the whole list which cotains name of play with highest score
    # to avoid appear agains when the record will be beatten
    settings.name_of_beater = []


def draw_menu(settings, mainboard):
    """Draw main menu."""
    # draw the three texts of main menu
    mainboard.blit_text1()
    mainboard.blit_text2()
    mainboard.blit_text3()

    # draw text and highest score
    mainboard.blit_text_score()
    mainboard.blit_score()

    # draw name of player with highest score
    mainboard.blit_name()


####### FUNCTIONS FOR RECORD NAME #######
def draw_record_name(mainboard):
    """Draw name of beater and its score."""
    # write name in filename_2
    mainboard.write_file(mainboard.filename_2, True)
    # update its name and score
    mainboard.update_name()
    mainboard.update_record()

    # draw name and score
    mainboard.blit_text_score()
    mainboard.blit_score()


def wait_write_name(screen, settings, mainboard, score_board):
    """Wait until user finish to write its name."""
    while  settings.write_finish:
        # Toma todos los eventos del juego
        for event in pygame.event.get():
            # si el usuario clickea la x en la barra de título
            if event.type == pygame.QUIT:
                exit()
            # si el usuario aprienta cualquier botón
            elif event.type == pygame.KEYDOWN:
                write_your_name(event, settings)

        # limit the number of letter
        limit_words(settings)

        # fill screen with the background color
        screen.fill(settings.background_color)

        # draw and update name of beater
        draw_record_name(mainboard)
        # flip screen
        pygame.display.flip()


def limit_words(settings):
    """
    Delete all characters of name of beater wheter it is large than it is allowed.
    """
    # take list that contains name of beater
    name = settings.name_of_beater
    # take list allowed number of character
    number_letter = settings.allowed_number_letter
    # if larger that it's allwed
    if len(name) > number_letter:
        # pop the last character
        name.pop()


def write_your_name(event, settings):
    """
    Trace the buttons that was pressed by user.
    Add them to the list of the name to store its name too.
    """
    # take list of name beater
    name = settings.name_of_beater
    if event.key == pygame.K_a:
        name.append("A")
    elif event.key == pygame.K_b:
        name.append("B")
    elif event.key == pygame.K_c:
        name.append("C")
    elif event.key == pygame.K_d:
        name.append("D")
    elif event.key == pygame.K_e:
        name.append("E")
    elif event.key == pygame.K_f:
        name.append("F")
    elif event.key == pygame.K_g:
        name.append("G")
    elif event.key == pygame.K_h:
        name.append("H")
    elif event.key == pygame.K_i:
        name.append("I")
    elif event.key == pygame.K_j:
        name.append("J")
    elif event.key == pygame.K_k:
        name.append("K")
    elif event.key == pygame.K_l:
        name.append("L")
    elif event.key == pygame.K_m:
        name.append("M")
    elif event.key == pygame.K_n:
        name.append("N")
    elif event.key == pygame.K_o:
        name.append("O")
    elif event.key == pygame.K_p:
        name.append("P")
    elif event.key == pygame.K_q:
        name.append("Q")
    elif event.key == pygame.K_r:
        name.append("R")
    elif event.key == pygame.K_s:
        name.append("S")
    elif event.key == pygame.K_t:
        name.append("T")
    elif event.key == pygame.K_u:
        name.append("U")
    elif event.key == pygame.K_v:
        name.append("V")
    elif event.key == pygame.K_w:
        name.append("W")
    elif event.key == pygame.K_x:
        name.append("X")
    elif event.key == pygame.K_y:
        name.append("Y")
    elif event.key == pygame.K_x:
        name.append("X")
    elif event.key == pygame.K_z:
        name.append("Z")
    elif event.key == pygame.K_SPACE:
        name.append(" ")
    elif event.key == pygame.K_RETURN:
        settings.write_finish = False
    elif event.key == pygame.K_BACKSPACE:
        # if there is no item in the list of name
        try:
            # delete last letter
            name.pop()
        except IndexError:
            # do nothing
            pass
