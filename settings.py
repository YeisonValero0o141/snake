#!/usr/bin/env python
# -*- coding: utf-8 -*-

# name of the file settings.py

# se importa el módulo
import pygame

class Settings():
    """La clase contiene todas las constantes del juego."""

    def __init__(self):
        """Inicializa todos los atributos de la clase."""
        # constantes de la pantalla
        self.screen_width = 1023
        self.screen_height = 545
        self.background_color = (96, 125, 139)

        # constantes del ratón
        self.raton_width = 16
        self.raton_height = 16
        self.raton_color = (121, 85, 72)
        self.raton_point = 1

        # constantes del muro
        self.wall_size = 10
        self.wall_color = (33, 33, 33)
        # fija la pisición del muro en los bordes de la pantalla. Donde 1 es posición inicial y 2 es posición final
        self.wall_position_up_1 = (0, 3)
        self.wall_position_up_2 = (1023, 3)
        self.wall_position_down_1 = (0, 542)
        self.wall_position_down_2 = (1023, 542)
        self.wall_position_left_1 = (0, 2)
        self.wall_position_left_2 = (0, 542)
        self.wall_position_right_1 = (1023, 2)
        self.wall_position_right_2 = (1023, 542)

        # constantes de la serpiente

        # longitud inicial
        self.length_initial = 5

        # alto, ancho y margen
        self.snake_width = 16
        self.snake_height = 15
        self.snake_margin = 3

        # posición inicial
        self.initial_position_x = 450 - (self.snake_width + self.snake_margin)
        self.initial_position_y = 230

        # variable bandera para la construcción de la misma
        self.call_one_time = 1

        # variable para saber si hubo una colición
        self.collision_snake = False

        # cuánto se moverá la serpiente
        self.change_position_x = self.snake_width + self.snake_margin
        self.change_position_y = 0
        # almacena los segmentos de la serpiente para construirla
        self.snake_build_helper = []
        # primer segmento de la serpiente
        self.snake_head = None
        # último segmento de la serpiente
        self.snake_tail = None

        # listas para imperdir cambios bruscos en el manejo de la serpiente
        self.traceback_movements = ["K_RIGHT"]
        self.traceback_counter = [0]
        # contador para evitar movimientos bruscos en el mismo segundo
        self.counter_time_between_movements = 0

        # constantes de la tabla de puntuación
        self.board_width = 30
        self.board_height = 10
        self.board_point_initial = 0
        # tipografía del texto de la table de puntuación
        self.text_color_score = (30, 30, 30)
        self.text_scores = "Score: "
        self.text_highest_score = "Highest Score: "

        # constantes del nombre del jugador con la más alta puntuación
        # lista en que se guarda el nombre completo
        self.name_of_beater = []
        # variable tipo bandera. Por defecto será False
        # por qué el usurioa no inicia el juego escribiento su nombre
        self.write_finish = False

        # constantes del menú principal
        self.text_mainboard_1 = "Play 1"
        self.text_mainboard_2 = "Play 2"
        self.text_mainboard_3 = "Exit"
        self.text_mainboard_color_1 = (250, 250, 250)
        self.text_mainboard_color_2 = (0, 0, 0)
        self.main_menu = True
        self.play_1 = False
        self.play_2 = False
        self.traceback_cursor = ["Play 1"]
        # carácteres permitos
        self.allowed_number_letter = 16
