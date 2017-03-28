#!/usr/bin/env python
# -*- coding: utf-8 -*-

# name of the file run_snake.py

# se importan los módulos
import pygame
# se importa las constantes del juego
from settings import Settings
# se importa las funcions del juego con el alias de fs
import functions_snake as fs
# se importa el módulo para tratar muchos sprite como grupos
from pygame.sprite import Group
# se importa el ratón
from raton import Raton
# se importa el método para número aleatorios
from numpy.random import randint
# se importa la tabla de puntuación
from score_board import ScoreBoard
# se importa el menú principal
from mainboard import MainBoard


def main():
    """La función que correrá el juego."""
    # se inicializa pygame
    pygame.init()

    # se instacia la clase Settings
    settings = Settings()

    # se establece el tamaño de la ventana
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    # fija el título de la ventana
    pygame.display.set_caption("Snake")

    # se instacia la tabla de puntuación
    score_board = ScoreBoard(screen, settings)

    # se instancia el menú principal
    mainboard = MainBoard(screen, settings)

    # crea nuevas coordenas aleatorias para la posición del ratón
    position_x_raton = randint(8, 1007)
    position_y_raton= randint(8, 530)

    # se instacia el ratón
    raton = Raton(screen, settings, position_x_raton, position_y_raton)

    # el grupo que contendrá todos los segmentos de la serpiente
    snake_whole = Group()

    # reloj de pygame
    clock = pygame.time.Clock()

    # variable para ser usada para la llamada de fs.build_snake_whole una sola vez
    call_one_time = settings.call_one_time

    # almacena el valor del atributo de la clase en la variable
    counter = settings.counter_time_between_movements

    # se oculta el cursor (la flechita)
    pygame.mouse.set_visible(False)

    while True:
        # variables tipo bandera para saber si el usuario quiere juegar
        main_menu = settings.main_menu
        play_1 = settings.play_1
        play_2 = settings.play_2

        # limita el número de frames por segundos
        clock.tick(10)

        if main_menu:
            fs.main_menu(screen, settings, score_board, mainboard)

        if play_1:

            if call_one_time == 1:

                # armamos la serpiente completa
                fs.build_snake_whole(screen, snake_whole, settings)
                # cambiamos su valor para que no se vuelva a ejecutar
                call_one_time = 2

            # actualiza la posición de la serpiente
            snake_whole.update()

            # actualiza la tabla de puntuación
            score_board.update()

            # incrementa el contador y actualiza el atributo de la clase
            counter += 1
            settings.counter_time_between_movements = counter

            # verifica si el usuario quiere cerrar el juego o mover la serpiente
            fs.check_events(counter, settings)

            # mueve la serpiente
            fs.move_snake_whole(screen, raton, snake_whole, settings)

            # verifica si la serpiente se muerde a sí misma
            snake_bite_itself = fs.check_snake_bite_itself(settings)

            if snake_bite_itself:
                # pausa el juego
                fs.pause(0.40)
                # vacía el grupo
                snake_whole.empty()
                # vacía la lista
                settings.snake_build_helper = []
                # verifica si se batió un record
                mainboard.check_beat_record()
                fs.wait_write_name(screen, settings, mainboard, score_board)
                # se resetea el puntaje
                settings.board_point_initial = 0
                # vuelve counstruir a la serpiente en su posición inicial
                fs.build_snake_whole(screen, snake_whole, settings)

            # comprueba si la serpiente choca con los muros y guarda el valor retornado
            collisions_snake_walls = fs.check_colliions_snake_wall(settings)

            # verifica si hubo una colisión
            if collisions_snake_walls:
                # pausa el juego
                fs.pause(0.40)
                # cambia la bandera para que aparezca el menú principal
                settings.main_menu = True
                settings.play_1 = False
                settings.play_2 = False
                # si hubo una colisión vuelve al menú principal
                # vacía el grupo y la lista
                snake_whole.empty()
                settings.snake_build_helper = []
                # verifica si se batió un record
                mainboard.check_beat_record()
                fs.wait_write_name(screen, settings, mainboard, score_board)
                # se resetea el puntaje
                settings.board_point_initial = 0
                # vuelve a armar a la serpiente en su posición inicial
                fs.build_snake_whole(screen, snake_whole, settings)

            # verifica si hay colisiones y guarda valor retornado
            collisions_raton = fs.check_collisions(raton, snake_whole, screen, settings)

            # si hubo colisiones
            if collisions_raton:
                # reproduce el sonido de mordisco
                settings.snake_head.sound_bite.play()

                # crea nuebas coordenas aleatorias para la posición del ratón
                position_x_raton = randint(8, 1003)
                position_y_raton= randint(8, 522)

                # se instacia el ratón
                raton = Raton(screen, settings, position_x_raton, position_y_raton)

                # aumenta el puntaje de la tabla de puntuación
                raton.increase_point(settings)

                # verifica si el ratón ocupa el espacio de la serpiente
                position_available = fs.avoid_raton_body_of_snake(raton, settings)

                while position_available:
                    # crea nuebas coordenas aleatorias para la posición del ratón
                    position_x_raton = randint(7, 1003)
                    position_y_raton= randint(7, 522)

                    # se instacia el ratón
                    raton = Raton(screen, settings,     position_x_raton, position_y_raton)
                    # se vuelve a llamar a la función para evitar un bucle infinito
                    position_available = fs.avoid_raton_body_of_snake(raton, settings)


            # actualiza todos los objetos en la pantalla
            fs.update_screen(screen, raton, snake_whole, raton, settings, score_board)

        elif play_2:

            if call_one_time == 1:

                # armamos la serpiente completa
                fs.build_snake_whole(screen, snake_whole, settings)
                # cambiamos su valor para que no se vuelva a ejecutar
                call_one_time = 2

            # actualiza la posición de la serpiente
            snake_whole.update()

            # actualiza la tabla de puntuación
            score_board.update()

            # incrementa el contador y actualiza el atributo de la clase
            counter += 1
            settings.counter_time_between_movements = counter

            # verifica si el usuario quiere cerrar el juego o mover la serpiente
            fs.check_events(counter, settings)

            # mueve la serpiente
            fs.move_snake_whole(screen, raton, snake_whole, settings)

            # verifica si la serpiente se muerde a sí misma
            snake_bite_itself = fs.check_snake_bite_itself(settings)

            if snake_bite_itself:
                # pausa el juego
                fs.pause(0.40)
                # vacía el grupo
                snake_whole.empty()
                # vacía la lista
                settings.snake_build_helper = []
                # verifica si se batió un record
                mainboard.check_beat_record()
                fs.wait_write_name(screen, settings, mainboard, score_board)
                # resetea el valor del puntaje
                settings.board_point_initial = 0
                # vuelve counstruir a la serpiente en su posición inicial
                fs.build_snake_whole(screen, snake_whole, settings)

            fs.snake_achieve_walls(screen, settings)

            # verifica si hay colisiones y guarda valor retornado
            collisions_raton = fs.check_collisions(raton, snake_whole, screen, settings)

            # si hubo colisiones
            if collisions_raton:
                # reproduce el sonido de mordisco
                settings.snake_head.sound_bite.play()

                # crea nuevas coordenas aleatorias para la posición del ratón
                position_x_raton = randint(0, 1007)
                position_y_raton= randint(0, 530)

                # se instacia el ratón
                raton = Raton(screen, settings, position_x_raton, position_y_raton)

                # aumenta el puntaje de la tabla de puntuación
                raton.increase_point(settings)

                # verifica si el ratón ocupa el espacio de la serpiente
                position_available = fs.avoid_raton_body_of_snake(raton, settings)

                while position_available:
                    # crea nuevas coordenas aleatorias para la posición del ratón
                    position_x_raton = randint(0, 1007)
                    position_y_raton= randint(0, 530)

                    # se instacia el ratón
                    raton = Raton(screen, settings, position_x_raton, position_y_raton)
                    # se vuelve a llamar a la función para evitar un bucle infinito
                    position_available = fs.avoid_raton_body_of_snake(raton, settings)


            # actualiza todos los objetos en la pantalla
            fs.update_screen(screen, raton, snake_whole, raton, settings, score_board, play_2=True)


if __name__ == "__main__":
    main()
