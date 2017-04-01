#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Function of the game.

Functions such as: check events of game, draw all objects, close
game, and so on.
"""

# import modules
# sys from library standard
import sys
# sleep function of time
from time import sleep
# pygame library
import pygame
# Snake class
from snake import Snake
# Raton (mouse) class
from raton import Raton

####### function to draw the walls #######
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


# Funciones para mover la serpiente con los eventos de las flechas serpiente
def move_keydown(event, counter, settings, snake_whole):
    """
    Move snake and does not allow sudden movements like opposite
    movements.

    For example if snake is going to lefward avoid snake go to
    rightward. Also avoid movements in the same second.
    """
    # guarda el valor del atributo de la clase como una variable de la función
    # take tracer of movements and counter
    traceback_movements = settings.traceback_movements
    counter_move_now = settings.traceback_counter

    # wheter it's not same second and movement is not the opposite. This apply for all conditionals
    if event.key == pygame.K_UP:
        if not traceback_movements[-1] == "K_DOWN" and not counter == counter_move_now[-1]:
            # move up
            snake_whole.move_up()

            # add trace of movements and counter to the tracer
            add_rastreo_tracer(traceback_movements, counter_move_now,
            "K_UP", counter)

            # remove the first item of list of both tracer
            clean_tracers(traceback_movements, counter_move_now)

    elif event.key == pygame.K_DOWN:
        if not traceback_movements[-1] == "K_UP" and not counter == counter_move_now[-1]:
            # move downward
            snake_whole.move_down()

            # add trace of movements and counter to the tracer
            add_rastreo_tracer(traceback_movements, counter_move_now,
            "K_DOWN", counter)

            # remove the first item of list of both tracer
            clean_tracers(traceback_movements, counter_move_now)

    elif event.key == pygame.K_LEFT:
        if not traceback_movements[-1] == "K_RIGHT" and not counter == counter_move_now[-1]:
            # move left
            snake_whole.move_left()

            # add trace of movements and counter to the tracer
            add_rastreo_tracer(traceback_movements, counter_move_now,
            "K_LEFT", counter)

            # remove the first item of list of both tracer
            clean_tracers(traceback_movements, counter_move_now)


    elif event.key == pygame.K_RIGHT:
        if not traceback_movements[-1] == "K_LEFT" and not counter == counter_move_now[-1]:
            # move right
            snake_whole.move_right()

            # add trace of movements and counter to the tracer
            add_rastreo_tracer(traceback_movements, counter_move_now,
            "K_RIGHT", counter)

            # remove the first item of list of both tracer
            clean_tracers(traceback_movements, counter_move_now)




def snake_achieve_walls(screen, settings):
    """Si la serpiente llega a la parte superior de la pantalla aparecerá en la parte inferior.
    Lo mismo va para todos los lados de la pantalla."""
    # guarda el paramétro como atributo
    screen = screen
    # obtiene el rectángulo de la pantalla
    screen_rect = screen.get_rect()
    # almacena la variable de la clase como una variable de la función
    snake = settings.snake_head
    # si la serpiente sobrepasa la parte superior de la pantalla
    if snake.rect.top < screen_rect.top:
        snake.rect.y = 525
    # si la serpiente sobrepasa la parte inferior de la pantalla
    elif snake.rect.bottom > screen_rect.bottom:
        snake.rect.y = 5
    # si la serpiente sobrepasa la parte izquierda de la pantalla
    elif settings.snake_head.rect.left < 0:
        snake.rect.x = 1000
    # si la serpiente sobrepasa la parte derecha de la pantalla
    elif settings.snake_head.rect.right > 1023:
        snake.rect.x = 5 + 1

    # actualiza la variable de la clase
    settings.snake_head = snake


# FUNCIONES PARA EL MENÚ PRINCIPAL
def move_cursor(mainboard, settings):
    """Verifica si el usuario mueve el cursos o elige una opción"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP or event.key == pygame.K_LEFT:
                # llama al método que cambia de color al textos
                mainboard.change_color_text1()
                # se añade al final de la lista
                settings.traceback_cursor.append("Play 1")

            elif event.key == pygame.K_RIGHT:
                # llama al método que cambia de color al textos
                mainboard.change_color_text2()
                # se añade al final de la lista
                settings.traceback_cursor.append("Play 2")

            elif event.key == pygame.K_DOWN:
                # llama al método que cambia de color al textos
                mainboard.change_color_text3()
                # se añade al final de la lista
                settings.traceback_cursor.append(False)

            elif event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                if settings.traceback_cursor[-1] == "Play 1":
                    settings.play_1 = True
                    settings.play_2 = False
                    settings.main_menu = False
                elif settings.traceback_cursor[-1] == "Play 2":
                    settings.play_1 = False
                    settings.play_2 = True
                    settings.main_menu = False
                elif settings.traceback_cursor[-1] == False:
                    exit()

            elif event.key == pygame.K_q:
                exit()

#####################################
####     IMPORTANT FUNCTIONS     ####
#####################################
def update_screen(screen, raton, snake_whole, ratones, settings, score_board, play_2=False):
    """Update screen."""
    # fill screen with the background color
    screen.fill(settings.background_color)

    # if it's play 2 mode
    if not play_2:
        # draw the walls on borders
        draw_walls(screen, settings)

    # blit scoreboard
    score_board.blitme()

    # blit mouse
    raton.blitme()

    # draw snake
    snake_whole.draw(screen)

    # flip screen
    pygame.display.flip()


def main_menu(screen, settings, score_board, mainboard):
    """Una sub-rutina que ejecuta el menú principal."""
    while settings.main_menu:
        move_cursor(mainboard, settings)
        update_menu(screen, settings, score_board, mainboard)
        # vacía la lista que contiene cada carácter del nombre del jugdar con la máxima puntuación
        # para que no vuelva a aperecer de nuevo cuando sea bátido el rećord
        settings.name_of_beater = []


def update_menu(screen, settings, score_board, mainboard):
    """Actualiza el menú principal."""
    # pinta el color en la pantalla
    screen.fill(settings.background_color)

    # dibuja los tres textos del menú principal en la pantalla
    mainboard.blit_text1()
    mainboard.blit_text2()
    mainboard.blit_text3()

    # actualiza la máxima puntuación
    mainboard.update_record()

    # dibuja el texto y las más alta puntuación
    mainboard.blit_text_score()
    mainboard.blit_score()

    # dibuja el nombre del jugador con la puntuación más alta
    mainboard.blit_name()

    # dra walls on border of screen
    draw_walls(screen, settings)

    # dibuja la tabla de puntuación
    score_board.blitme()

    # dibuja los cambios en la pantalla
    pygame.display.flip()


def draw_record_name(mainboard):
    """Dibuja el récord y nombrel del jugador con la más alta puntuación.
    Actualiza el nombre del jugador con la más alta puntuación."""
    # escribe el nombre en el archivo
    mainboard.write_file(mainboard.filename_2, True)
    # y lo dibuja en la pantalla
    mainboard.update_name()

    # dibuja el texto y las más alta puntuación
    mainboard.blit_text_score()
    mainboard.blit_score()


def change_flags(settings):
    """Change flags to stop game and appear main menu."""
    settings.main_menu = True
    settings.play_1 = False
    settings.play_2 = False


def wait_write_name(screen, settings, mainboard, score_board):
    while  settings.write_finish:
        # Toma todos los eventos del juego
        for event in pygame.event.get():
            # si el usuario clickea la x en la barra de título
            if event.type == pygame.QUIT:
                exit()
            # si el usuario aprienta cualquier botón
            elif event.type == pygame.KEYDOWN:
                write_your_name(event, settings)

        # elimina los carácteres si se ha pasado el limite permitido
        limit_words(settings)

        # dibuja el menú en la pantalla
        update_menu(screen, settings, score_board, mainboard)
        # dibuja y actualiza el nombre del jugador con la máxima puntuación
        draw_record_name(mainboard)


def limit_words(settings, number=10):
    """Elimina los items de la lista hasta que sea menor al parámetro pasado."""
    # almacena la lista de la clase y el número de letras permitida
    name = settings.name_of_beater
    number_letter = settings.allowed_number_letter
    if len(name) > number_letter:
        name.pop()


def check_events(counter, settings, snake_whole):
    """Verifica si el usuario desea salir del juego o quiere mover a la serpiente."""
    # Toma todos los eventos del juego
    for event in pygame.event.get():
        # si el usuario clickea la x en la barra de título
        if event.type == pygame.QUIT:
            exit()
        # si el usuario aprienta cualquier botón
        elif event.type == pygame.KEYDOWN:
            move_keydown(event, counter, settings, snake_whole)


def exit():
    """Se sale del juego."""
    sys.exit()


def pause(seconds):
    """Pausa el juego por n segundos."""
    sleep(seconds)


def write_your_name(event, settings):
    """Rastrea los botones presionados para typear un nombre.
    Los pasa uno a uno a una lista de la clase settings."""
    # almacena la lista de la clase
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
        # maneja las excepciones
        try:
            # si no hay nigún item en la lista
            name.pop()
        except IndexError:
            # para evitar un error no hace nada
            pass

    # actualiza la lista
    settings.name_of_beater = name
