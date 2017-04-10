#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Mainboard of game."""

# import pygame's font
import pygame.font

class MainBoard():
    """Represent main menu."""

    def __init__(self, screen, settings):
        """
        Store all attributes of class and set its initial position.
        """
        # save parameter like attributes
        self.screen = screen
        self.settings = settings

        # store file names
        self.filename_1 = "highest_score.txt"
        self.filename_2 = "name_beater.txt"

        # take screen's rectangle
        self.screen_rect = self.screen.get_rect()

        # store text and its color
        self.text_1 = self.settings.text_mainboard_1
        self.text_2 = self.settings.text_mainboard_2
        self.text_3 = self.settings.text_mainboard_3
        self.color_1 = self.settings.text_mainboard_color_1
        self.color_2 = self.settings.text_mainboard_color_2
        self.color_2 = self.settings.text_mainboard_color_2

        # text for highest score
        self.text_highest_score = settings.text_highest_score

        # highest score
        self.highest_score = self.load_file(self.filename_1)

        # name of player wiht new record
        self.name_beater = self.load_file(self.filename_2, True)
        # set font by default
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

        # render name of beater with highest score
        self.message_name = self.font.render(self.name_beater, True, self.color_2, self.settings.background_color)

        # get rectangle of message 1, 2 and 3
        self.rect_1 = self.message_1.get_rect()
        self.rect_2 = self.message_2.get_rect()
        self.rect_3 = self.message_3.get_rect()

        # get highest score message's rectangle
        self.message_score_rect = self.message_text_score.get_rect()

        # get highest score's rectangle
        self.score_rect = self.message_score.get_rect()

        # get name of beater's rectangle
        self.name_rect = self.message_name.get_rect()

        # set positions of messages
        self.rect_1.centerx = self.screen_rect.centerx - 90
        self.rect_1.centery = self.screen_rect.centery - 40

        self.rect_2.centerx = self.screen_rect.centerx + 60
        self.rect_2.centery = self.screen_rect.centery - 38

        self.rect_3.centerx = self.screen_rect.centerx - 15
        self.rect_3.centery = self.screen_rect.centery + 25

        # set poisition of score message
        self.message_score_rect.centerx = self.screen_rect.centerx - 150
        self.message_score_rect.centery = self.screen_rect.centery - 130

        # set highest score's position
        self.score_rect.centerx = self.screen_rect.centerx + 50
        self.score_rect.centery = self.screen_rect.centery - 130

        # set name of beater's position
        self.name_rect.left = self.screen_rect.centerx + 100
        self.name_rect.centery = self.screen_rect.centery - 130


    def change_color_text1(self):
        """"Change color of text 1."""
        self.message_1 = self.font.render(self.text_1, True, self.color_2, self.settings.background_color)

        self.message_2 = self.font.render(self.text_2, True, self.color_1, self.settings.background_color)

        self.message_3 = self.font.render(self.text_3, True, self.color_1, self.settings.background_color)


    def change_color_text2(self):
        """Change color of text 2."""
        self.message_1 = self.font.render(self.text_1, True, self.color_1, self.settings.background_color)

        self.message_2 = self.font.render(self.text_2, True, self.color_2, self.settings.background_color)

        self.message_3 = self.font.render(self.text_3, True, self.color_1, self.settings.background_color)


    def change_color_text3(self):
        """Change color of text 3."""
        self.message_1 = self.font.render(self.text_1, True, self.color_1, self.settings.background_color)

        self.message_2 = self.font.render(self.text_2, True, self.color_1, self.settings.background_color)

        self.message_3 = self.font.render(self.text_3, True, self.color_2, self.settings.background_color)


    def write_file(self, filename, name=False):
        """Write name of beater or score in a given file."""
        # work with name of player with highest score
        if name:
            # store name of beater list of settings class
            name_of_beater = self.settings.name_of_beater
            # pass each leter
            name = "".join(name_of_beater)
            # save name
            content = name
        # work with score
        else:
            # store current store
            score = self.settings.board_point_initial
            # it's pass to string to be written in file
            score = str(score)
            # save score
            content = score

        # if it doesn't exists or didn't was find, it create it
        with open(filename, "w") as file_object:
            file_object.write(content)


    def load_file(self, filename, name=False):
        """Load file and return its content"""
        try:
            # open file
            with open(filename) as file_object:
                # read content and delete jump line
                content = file_object.read().rstrip()
        except IOError:
            if name:
                # write name in file
                self.write_file(filename, True)
            else:
                # write score in file
                self.write_file(filename)
        else:
            return content


    def check_beat_record(self):
        """Check if the record was beat."""
        # save file's content and convert to int
        record = self.load_file(self.filename_1)
        record = int(record)
        # store current score
        score = self.settings.board_point_initial
        # see if it's greater
        if score > record:
            # write new highest score in filename_1
            self.write_file(self.filename_1)
            # change flag to write new name
            self.settings.write_finish = True
        # otherwise
        elif score <= record:
            # do nothing
            pass


    def update_record(self):
        """Update highest score."""
        # highest score
        self.highest_score = self.load_file(self.filename_1)
        # render it
        self.message_score = self.font.render(self.highest_score, True, self.color_2, self.settings.background_color)
        # and blit it
        self.blit_score()


    def update_name(self):
        """Update name of player with highest score."""
        # load file
        self.name_beater = self.load_file(self.filename_2)
        # render name
        self.message_name = self.font.render(self.name_beater, True, self.color_2, self.settings.background_color)
        # blit it
        self.blit_name()


    def blit_text1(self):
        """Draw play 1 message of the main menu."""
        self.screen.blit(self.message_1, self.rect_1)


    def blit_text2(self):
        """Draw play 2 message of the main menu."""
        self.screen.blit(self.message_2, self.rect_2)


    def blit_text3(self):
        """Draw exit message of the main menu."""
        self.screen.blit(self.message_3, self.rect_3)


    def blit_text_score(self):
        """Draw score text of menu."""
        self.screen.blit(self.message_text_score, self.message_score_rect)


    def blit_score(self):
        """Draw highest score."""
        self.screen.blit(self.message_score, self.score_rect)


    def blit_name(self):
        """Blit name of player on screen"""
        self.screen.blit(self.message_name, self.name_rect)
