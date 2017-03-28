#!/usr/bin/env python
# -*- coding: utf-8 -*-

# name of the file score_board.py

# se importa el módulo
import pygame.font

class ScoreBoard():
    """Un intento de representar a una tabla de puntuación con un rectángulo."""

    def __init__(self, screen, settings):
        """Inicializa todos los atributos de la clase y fija su posición inicial."""
        self.screen = screen
        self.settings = settings

        # obtine el rectángulo de la imágen
        self.screen_rect = self.screen.get_rect()

        # almacena el color de la imágen
        self.color_text = self.settings.text_color_score
        # selecciona la tipografía
        self.font = pygame.font.SysFont(None, 48)
        # guarda la puntuación
        self.points = self.settings.board_point_initial
        # guarda el texto
        self.text = self.settings.text_scores
        # lo renderiza
        self.message = self.font.render(self.text + str(self.points), True, self.color_text, self.settings.background_color)

        # consigue el rectángulo del mensaje
        self.rect = self.message.get_rect()
        self.rect.centery = self.screen_rect.top + 28
        self.rect.centerx = self.screen_rect.centerx


    def update(self):
        """Actualiza la puntuanción de la tabla."""
        self.points = self.settings.board_point_initial
        self.message = self.font.render(self.text + str(self.points), True, self.color_text, self.settings.background_color)


    def blitme(self):
        """Dibuja la tabla de posición."""
        self.screen.blit(self.message, self.rect)
