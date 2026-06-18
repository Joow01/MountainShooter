#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from Code.const import WIN_WINDTH, COLOR_BLOOD


class Menu :
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/MenuBG.png')
        self.rect = self.surf.get_rect(left=0, top=0)
        self.title_font = pygame.font.Font(
            './assets/Fonte/static/Cinzel-Bold.ttf',50 )

    def run(self, ):
        pygame.mixer_music.load('./assets/Menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(text_size=100, text="Sangue", text_color=COLOR_BLOOD, text_center_pos=(WIN_WINDTH / 2, 70))
            self.menu_text(text_size=100, text="Eterno", text_color=COLOR_BLOOD, text_center_pos=(WIN_WINDTH / 2, 145))
            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    pygame.quit() # Close Window
                    quit() # End Pygame

    def menu_text(self, text_size: int, text: str,
                  text_color: tuple, text_center_pos: tuple):

        text_font = pygame.font.Font(
            "./assets/Fonte/static/Cinzel-Bold.ttf",
            text_size
        )

        # Sombra preta
        shadow_surf = text_font.render(text, True, (0, 0, 0))
        shadow_rect = shadow_surf.get_rect(
            center=(text_center_pos[0] + 3, text_center_pos[1] + 3)
        )

        #Texto principal
        text_surf = text_font.render(text, True, text_color)
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(shadow_surf, shadow_rect)
        self.window.blit(text_surf, text_rect)