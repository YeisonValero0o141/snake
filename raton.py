#!/usr/bin/env python
# -*- coding: utf-8 -*-

# name of the file raton.py

# se importan los módulo
import pygame
# se importa el método para número aleatorios
from random import randint


class Raton():
    """Representa a un ratón con un cuadrado."""

    def __init__(self, screen, settings, position_x_raton, position_y_raton):
        """Inicializa los atribuos de la clase"""
        self.screen = screen
        self.settings = settings

        # crea un cuadrado
        self.image = pygame.Surface([self.settings.raton_width, self.settings.raton_height])

        # se pinta con el color establecido
        self.image.fill(self.settings.raton_color)

        # almacena el valor del ratón
        self.point = settings.raton_point

        # se consigue el rectángulo de la imágen
        self.rect = self.image.get_rect()

        # se fija su posición
        self.rect.x = position_x_raton
        self.rect.y = position_y_raton


    def increase_point(self, settings):
        """Incremento el puntaje de la table de puntuación"""
        self.settings.board_point_initial += self.point


    def blitme(self):
        """Dibuja el ratón en su posición actual en la pantalla."""
        self.screen.blit(self.image, self.rect)
