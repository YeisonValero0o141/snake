#!/usr/bin/env python
# -*- coding: utf-8 -*-

# name of the file snake.py

# se importan los módulos
import pygame
# se importa la clase Sprite
from pygame.sprite import Sprite


class Snake(Sprite):
    """Clase que representará a una serpiente."""

    def __init__(self, screen, settings, position_x, position_y):
        """Inicializa los atributos de la clase."""
        # se heredan los atribuos de la clase padre
        super(Snake, self).__init__()
        # almacena los parámetros screen y settings como atributos
        self.screen = screen
        self.settings = settings

        # se obtiene el rectángulo de la pantalla
        self.screen_rect = self.screen.get_rect()

        # abre el archivo que representará a la serpiente
        self.image = pygame.image.load("images/snake.png")

        # toma el rectángulo de la imágen
        self.rect = self.image.get_rect()

        # fija su posición inicializa
        self.rect.x = position_x
        self.rect.y = position_y

        self.sound_bite = pygame.mixer.Sound('sonidos/mordisco.wav')
