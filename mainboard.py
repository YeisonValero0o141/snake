#!/usr/bin/env python
# -*- coding: utf-8 -*-

# name of the file of mainboard.py

# importa el módulo
# importa la fuente de pygame
import pygame.font

class MainBoard():
    """La clase representa a una menú principal."""

    def __init__(self, screen, settings):
        """Incializa todos los atributos de la clase y fija su posición inical."""
        # se almacenan los parámetros como atributos
        self.screen = screen
        self.settings = settings

        # guarda el nombre de los archivos
        self.filename_1 = "highest_score.txt"
        self.filename_2 = "name_beater.txt"

        # toma el rectángulo de la pantalla
        self.screen_rect = self.screen.get_rect()

        # guarda el texto y color
        self.text_1 = self.settings.text_mainboard_1
        self.text_2 = self.settings.text_mainboard_2
        self.text_3 = self.settings.text_mainboard_3
        self.color_1 = self.settings.text_mainboard_color_1
        self.color_2 = self.settings.text_mainboard_color_2
        self.color_2 = self.settings.text_mainboard_color_2

        # el texto de la máxima puntuación
        self.text_highest_score = settings.text_highest_score

        # máxima puntuación
        self.highest_score = self.load_file(self.filename_1)

        # nombre del jugador del nuevo récord
        self.name_beater = self.load_file(self.filename_2, True)

        # fija que se usará la tipografía de pygame por defecto
        # take font
        self.font = pygame.font.SysFont(None, 60)

        # renderiza el texto 1
        self.message_1 = self.font.render(self.text_1, True, self.color_2, self.settings.background_color)

        # renderiza el texto 2
        self.message_2 = self.font.render(self.text_2, True, self.color_1, self.settings.background_color)

        # renderiza el texto 3
        self.message_3 = self.font.render(self.text_3, True, self.color_1, self.settings.background_color)

        # renderiza el texto de la máxima puntuación
        self.message_text_score = self.font.render(self.text_highest_score, True, self.color_2, self.settings.background_color)

        # renderiza la máxima puntuación
        self.message_score = self.font.render(self.highest_score, True, self.color_2, self.settings.background_color)

        # renderiza el nombre del jugador con la puntuación más alta
        self.message_name = self.font.render(self.name_beater, True, self.color_2, self.settings.background_color)

        # toma el ractángulo del texto 1, 2 y del 3
        self.rect_1 = self.message_1.get_rect()
        self.rect_2 = self.message_2.get_rect()
        self.rect_3 = self.message_3.get_rect()

        # consigue el rectángulo del texto de la más alta puntuación
        self.message_score_rect = self.message_text_score.get_rect()

        # consigue el rectángulo de la más alta puntuación
        self.score_rect = self.message_score.get_rect()

        # consigue el rectángulo del nombre del jugador cno la puntuación más alta
        self.name_rect = self.message_name.get_rect()

        # establece la posición del texto 1, 2 y del 3
        self.rect_1.centerx = self.screen_rect.centerx - 90
        self.rect_1.centery = self.screen_rect.centery - 40

        self.rect_2.centerx = self.screen_rect.centerx + 60
        self.rect_2.centery = self.screen_rect.centery - 38

        self.rect_3.centerx = self.screen_rect.centerx - 15
        self.rect_3.centery = self.screen_rect.centery + 25

        # fija la posición inicial del mensaje de la máxima puntuación
        self.message_score_rect.centerx = self.screen_rect.centerx - 150
        self.message_score_rect.centery = self.screen_rect.centery - 130

        # establece la posición de la máxima puntuación
        self.score_rect.centerx = self.screen_rect.centerx + 50
        self.score_rect.centery = self.screen_rect.centery - 130

        # establece la posición del nombre del jugador con la puntuación más alta
        self.name_rect.left = self.screen_rect.centerx + 100
        self.name_rect.centery = self.screen_rect.centery - 130


    def change_color_text1(self):
        """"Cambia el color al texto 1."""
        # renderiza el texto 1
        self.message_1 = self.font.render(self.text_1, True, self.color_2, self.settings.background_color)

        # renderiza el texto 2
        self.message_2 = self.font.render(self.text_2, True, self.color_1, self.settings.background_color)

        # renderiza el texto 3
        self.message_3 = self.font.render(self.text_3, True, self.color_1, self.settings.background_color)


    def change_color_text2(self):
        """Cambia el color al texto 2."""
        # renderiza el texto 1
        self.message_1 = self.font.render(self.text_1, True, self.color_1, self.settings.background_color)

        # renderiza el texto 2
        self.message_2 = self.font.render(self.text_2, True, self.color_2, self.settings.background_color)

        # renderiza el texto 3
        self.message_3 = self.font.render(self.text_3, True, self.color_1, self.settings.background_color)


    def change_color_text3(self):
        """Cambia el color al texto 3."""
        # renderiza el texto 1
        self.message_1 = self.font.render(self.text_1, True, self.color_1, self.settings.background_color)

        # renderiza el texto 2
        self.message_2 = self.font.render(self.text_2, True, self.color_1, self.settings.background_color)

        # renderiza el texto 3
        self.message_3 = self.font.render(self.text_3, True, self.color_2, self.settings.background_color)


    def write_file(self, filename, name=False):
        """Escribe el nuevo récord en el archivo highest_score.txt"""
        if name:
            # almacena la lista de la clase en la variable
            names = self.settings.name_of_beater
            # se usará para pasar el contenido de la lista a string
            name = ""
            # lo pasa a un string para obtener el nombre completo y no items de la lista
            for x in names:
                # se guarda letra por letra
                name += x
            # se guarda el nombre completo en content
            content = name
        else:
            # almacena la puntuación actual
            score = self.settings.board_point_initial
            # se pasa a string para poder ser escrito en el archivo
            score = str(score)
            # se guarda el número pasado a string en content
            content = score

        # si no existe o no fue encontrado, lo crea
        with open(filename, "w") as file_object:
            file_object.write(content)


    def load_file(self, filename, name=False):
        """Carga el archivo y devuelve el contenido."""
        # maneja las exepciones
        try:
            # abre el archivo, si existe existe, lo hace en modo lectura
            with open(filename) as file_object:
                # lee la información del archivo y borra el salto de linea
                content = file_object.read().rstrip()

        except:
            if name:
                # si se le pasa el parámetro escribe el nombre
                self.write_file(filename, True)
            else:
                # si no escribe el récord
                self.write_file(filename)
        else:
            return content


    def check_beat_record(self):
        """Verifica si se ha roto el récord."""
        # guarda el valor devuelto y lo pasa a entero
        record = self.load_file(self.filename_1)
        record = int(record)
        # almacena la puntuación actual
        score = self.settings.board_point_initial
        if score > record:
            # si la puntuación es mayor escribe el nuevo récord en el archivo
            self.write_file(self.filename_1)
            # cambia el valor
            self.settings.write_finish = False
            # llama a la función para escriba el nombre
            self.settings.write_finish = True
        elif score <= record:
            # si es menor no hace nada
            pass


    def update_record(self):
        """Actualiza la puntuación máxima."""
        # máxima puntuanción
        self.highest_score = self.load_file(self.filename_1)
        # renderiza la máxima puntuación
        self.message_score = self.font.render(self.highest_score, True, self.color_2, self.settings.background_color)


    def update_name(self):
        """Actualiza el nombre."""
        # nombre del jugador del nuevo récord
        self.name_beater = self.load_file(self.filename_2)
        # renderiza el nombre del jugador con la puntuación más alta
        self.message_name = self.font.render(self.name_beater, True, self.color_2, self.settings.background_color)
        self.blit_name()


    def blit_text1(self):
        """Dibuja el text 1 del menú principal."""
        self.screen.blit(self.message_1, self.rect_1)


    def blit_text2(self):
        """Dibuja el text 2 del menú principal."""
        self.screen.blit(self.message_2, self.rect_2)


    def blit_text3(self):
        """Dibuja el texto 2 del menú princial."""
        self.screen.blit(self.message_3, self.rect_3)


    def blit_text_score(self):
        """Dibuja la puntuación encima del menú principal."""
        self.screen.blit(self.message_text_score, self.message_score_rect)


    def blit_score(self):
        """Dibuja la puntuación más alta puntuación."""
        self.screen.blit(self.message_score, self.score_rect)


    def blit_name(self):
        """Dibuja el nombre del jugador con la puntuación más alta."""
        self.screen.blit(self.message_name, self.name_rect)
