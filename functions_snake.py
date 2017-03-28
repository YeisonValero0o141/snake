#!/usr/bin/env python
# -*- coding: utf-8 -*-

# name of the file functions_snake.py

# se importa los módulos
import pygame, sys
# se importa la clase serpiente
from snake import Snake
# se importa la clase Raton
from raton import Raton
# se importa el método para número aleatorios
from numpy.random import randint
# se importa el método sleep de time
from time import sleep

####### function to draw the walls #######
def draw_wall_up(screen, settings):
    """Dibuja el muero de la parte superior de la pantalla."""
    pygame.draw.line(screen, (settings.wall_color), (settings.wall_position_up_1), (settings.wall_position_up_2), settings.wall_size)


def draw_wall_down(screen, settings):
    """Dibuja el muero de la parte inferior de la pantalla."""
    pygame.draw.line(screen, (settings.wall_color), (settings.wall_position_down_1), (settings.wall_position_down_2), settings.wall_size)


def draw_wall_left(screen, settings):
    """Dibuja el muro del lado lateral izquierdo de la pantalla"""
    pygame.draw.line(screen, (settings.wall_color), (settings.wall_position_left_1), (settings.wall_position_left_2), settings.wall_size)


def draw_wall_right(screen, settings):
    """Dibuja el muro del lado lateral derecha de la pantalla."""
    pygame.draw.line(screen, (settings.wall_color), (settings.wall_position_right_1), (settings.wall_position_right_2), settings.wall_size)


def draw_walls(screen, settings):
    """Dibuja los muro a los borde de la pantalla."""

    draw_wall_up(screen, settings)

    draw_wall_down(screen, settings)

    draw_wall_left(screen, settings)

    draw_wall_right(screen, settings)


####### SNAKE #######
def build_snake_whole(screen, snake_whole, settings):
    """"Construye a la serpiente."""
    snakes = settings.snake_build_helper
    reset_movements_settings(settings)
    for i in range(settings.length_initial):
        # define la posición x
        position_x = settings.initial_position_x
        # define la posición y
        position_y = settings.initial_position_y
        # instancia el segmento de la serpiente
        part_snake = Snake(screen, settings, position_x, position_y)
        # lo añade a la lista
        snakes.append(part_snake)
        # la lista es añadida al grupo
        snake_whole.add(snakes)

    # guarda los segmentos de la serpiente recogidos en la clase Settings
    settings.snake_build_helper = snakes

# función para mover al a serpiente según move_keydown
def move_snake_whole(screen, raton, snake_whole, settings):
    """Elimina el último segmento de la serpiente y crea uno nuevo al comienzo.
    Dando la ilusión de movimiento."""
    # guarda los atributos de la clase como  variables de la función
    snakes = settings.snake_build_helper
    snake = settings.snake_head
    last_snake_segment = settings.snake_tail

    # toma el último segmento de la serpiente
    last_snake_segment = snakes.pop()

    # elimina el último segmento
    snake_whole.remove(last_snake_segment)

    # se fija la posición del nuevo segmento que será creado
    position_x = snakes[0].rect.x + settings.change_position_x
    position_y = snakes[0].rect.y + settings.change_position_y

    # crea un crea un nuevo segmento de la serpiente
    snake = Snake(screen, settings, position_x, position_y)

    # inserta el segmento al comienzo de la lista
    snakes.insert(0, snake)

    # añade el nuevo segmento de la serpiente al grupo
    snake_whole.add(snake)

    # actualiza la lista almacenada en la clase
    settings.snake_build_helper = snakes
    # actualiza los atributos de la clase
    settings.snake_head = snake
    settings.snake_tail = last_snake_segment


def reset_movements_settings(settings):
    """Resetea los valores que fijan el movimiento de la
    serpiente para que cuándo muera si
    se vuelva construir se mueva como al comienzo."""
    # resetea position de la serpiente a la inicial
    settings.change_position_y = 0
    settings.change_position_x = settings.snake_width + settings.snake_margin
    # resetea el restreador de movimiento
    settings.traceback_movements = ["K_RIGHT"]


def check_snake_bite_itself(settings):
    """Comprueba si la serpiente se mueve sobre si misma."""
    # guarda los atribuos como variables de la serpiente
    snake = settings.snake_head
    snakes = settings.snake_build_helper[:]
    for x in range(len(snakes)):
        if x == 0:
            pass
        else:
            last_snake_segment = snakes.pop()
            if snake.rect.colliderect(last_snake_segment.rect):
                # cambia la bandera para que aparezca el menú principal
                settings.main_menu = True
                settings.play_1 = False
                settings.play_2 = False
                return True

# Funciones para mover la serpiente con los eventos de las flechas serpiente
# y verifica si la serpiente choca con los muros
def move_keydown(event, counter, settings):
    """Mueve la serpiente e impide que haga movimientos bruscos"""
    # guarda el valor del atributo de la clase como una variable de la función
    traceback_movements = settings.traceback_movements
    counter_move_now = settings.traceback_counter

    if event.key == pygame.K_UP:
        # si el moviento anterior no es contrario al del actual y no es en el mismo segundo
        if not traceback_movements[-1] == "K_DOWN" and not counter == counter_move_now[-1]:
            settings.change_position_x = 0
            settings.change_position_y = (settings.snake_height +settings.snake_margin) * -1
            traceback_movements.append("K_UP")
            counter_move_now.append(counter)
            # remueve el primer elemento de la lista
            del traceback_movements[0]
            del counter_move_now[0]

    elif event.key == pygame.K_DOWN:
        # si el moviento anterior no es contrario al del actual y no es en el mismo segundo
        if not traceback_movements[-1] == "K_UP" and not counter == counter_move_now[-1]:
            settings.change_position_x = 0
            settings.change_position_y = (settings.snake_height +settings.snake_margin)
            traceback_movements.append("K_DOWN")
            counter_move_now.append(counter)
            # remueve el primer elemento de la lista
            del traceback_movements[0]
            del counter_move_now[0]

    elif event.key == pygame.K_LEFT:
        # si el moviento anterior no es contrario al del actual y no es en el mismo segundo
        if not traceback_movements[-1] == "K_RIGHT" and not counter == counter_move_now[-1]:
            settings.change_position_x = (settings.snake_width + settings.snake_margin) * -1
            settings.change_position_y = 0
            traceback_movements.append("K_LEFT")
            counter_move_now.append(counter)
            # remueve el primer elemento de la lista
            del traceback_movements[0]
            del counter_move_now[0]


    elif event.key == pygame.K_RIGHT:
        # si el moviento anterior no es contrario al del actual y no es en el mismo segundo
        if not traceback_movements[-1] == "K_LEFT" and not counter == counter_move_now[-1]:
            settings.change_position_x = (settings.snake_width +settings.snake_margin)
            settings.change_position_y = 0
            traceback_movements.append("K_RIGHT")
            counter_move_now.append(counter)
            # remueve el primer elemento de la lista
            del traceback_movements[0]
            del counter_move_now[0]

    elif event.key == pygame.K_q:
        exit()

    # actualiza la lista de la clase
    traceback_movements = settings.traceback_movements
    settings.traceback_counter = counter_move_now


def check_colliions_snake_wall(settings):
    """Comprueba si la serpiente alcanzó cualquieras de los muros. Devuelve True es así, False sino."""
    snake = settings.snake_head
    if snake.rect.top < 0:
        return True
    elif snake.rect.bottom > 545:
        return True
    elif snake.rect.left < 0:
        return True
    elif snake.rect.right > 1028:
        return True
    else:
        return False


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


def increase_lenght_of_snake(screen, settings, snake_whole):
    """
    Increase snake by one segment.

    The segment, it will be appended at last segment.
    """
    # take all segments
    segments = settings.snake_build_helper
    # take the last segments to use its position to append the new segment
    last_segment = settings.snake_tail

    # utilize last_segment's position to set position of the new segment
    position_x = last_segment.rect.x
    position_y = last_segment.rect.y

    # create new sement at the end of the snake (the tail)
    last_snake_segment = Snake(screen, settings, position_x, position_y)

    # append segment in the list of segments
    segments.append(last_snake_segment)

    # add new the segment in the snake
    snake_whole.add(last_snake_segment)

    # update list of segments
    settings.snake_build_helper = segments
    # and the last segment (the tail)
    settings.snake_tail = last_snake_segment


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
###     FUNCIONES IMPORTANTES     ###
#####################################
def update_screen(screen, raton, snake_whole, ratones, settings, score_board, play_2=False):
    """Actualiza la pantalla."""
    # pinta el color en la pantalla
    screen.fill(settings.background_color)

    # si no se le pasa ningún paramétro
    if not play_2:
        # dibuja lineas por muros en los bordes de la pantalla
        draw_walls(screen, settings)

    # dibuja la tabla de puntuación
    score_board.blitme()

    # dibuja el ratón
    raton.blitme()

    # dibuja la serpiente en la pantalla
    snake_whole.draw(screen)

    # dibuja los cambios en la pantalla
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

    # dibuja lineas por muros en los bordes de la pantalla
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


def check_events(counter, settings):
    """Verifica si el usuario desea salir del juego o quiere mover a la serpiente."""
    # Toma todos los eventos del juego
    for event in pygame.event.get():
        # si el usuario clickea la x en la barra de título
        if event.type == pygame.QUIT:
            exit()
        # si el usuario aprienta cualquier botón
        elif event.type == pygame.KEYDOWN:
            move_keydown(event, counter, settings)


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
