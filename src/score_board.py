#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Scoreboard of game.

Copyright: (c) 2017 by Yeison Valero.
License: MIT, see LICENSE for more information.
"""

# font of pygame
import pygame.font

class ScoreBoard():
    """Scoreboard."""

    def __init__(self, screen, settings):
        """
        Store all attribute of class and set its initial positions.
        """
        # save screen and settings parameter like attributes
        self.screen = screen
        self.settings = settings

        # get image's rectangle
        self.screen_rect = self.screen.get_rect()
        # store color of text
        self.color_text = self.settings.text_color_score
        # set font and its size
        self.font = pygame.font.Font(None, 48)
        # store score
        self.points = self.settings.board_point_initial
        # max score
        self.max_score = self.settings.max_score

        # save text
        self.text = self.settings.text_scores
        # render message
        self.message = self.font.render(self.text + str(self.points), True, self.color_text, self.settings.background_color)

        # get rect of scoreboard
        self.rect = self.message.get_rect()
        self.rect.centery = self.screen_rect.top + 28
        self.rect.centerx = self.screen_rect.centerx


    def max_score_was_achieved(self):
        """Check if max score was achieved.
        return bool.
        """
        if self.points >= self.max_score:
            self.settings.play_won = True
        else:
            self.settings.play_won = False


    def update(self):
        """Update scoreboard."""
        # score
        self.points = self.settings.board_point_initial
        # message
        self.message = self.font.render(self.text + str(self.points), True, self.color_text, self.settings.background_color)


    def blitme(self):
        """Blit scoreboard."""
        self.screen.blit(self.message, self.rect)
