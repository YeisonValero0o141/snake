#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Scoreboard of game.
"""

# import modules
# os from library standard
import os
# font of pygame
import pygame.font

class ScoreBoard():
    """Scoreboard."""

    def __init__(self, screen, settings):
        """
        Store all attribute of class and set its initial positions.
        """
        self.screen = screen
        self.settings = settings

        # get image's rectangle
        self.screen_rect = self.screen.get_rect()

        # store color of text
        self.color_text = self.settings.text_color_score
        # set font and fontsize
        self.font = pygame.font.SysFont(None, 48)
        # store score
        self.points = self.settings.board_point_initial
        # save text
        self.text = self.settings.text_scores
        # render message
        self.message = self.font.render(self.text + str(self.points), True, self.color_text, self.settings.background_color)

        # get rect of scoreboard
        self.rect = self.message.get_rect()
        self.rect.centery = self.screen_rect.top + 28
        self.rect.centerx = self.screen_rect.centerx


    def update(self):
        """Update scoreboard."""
        # score
        self.points = self.settings.board_point_initial
        # message
        self.message = self.font.render(self.text + str(self.points), True, self.color_text, self.settings.background_color)


    def blitme(self):
        """Blit scoreboard."""
        self.screen.blit(self.message, self.rect)
