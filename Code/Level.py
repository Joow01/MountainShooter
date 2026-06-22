#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame

from Code.Const import WIN_WIDTH, WIN_HEIGHT
from Code.Entity import Entity
from Code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1BG'))
        self.entity_list.append(EntityFactory.get_entity('Player'))


    def run(self, ):
        pygame.mixer_music.load(f'./assets/Level1Music.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            while True:
                clock.tick(60)

                self.window.fill((0, 0, 0))

                player = self.entity_list[-1]

                camera_x = player.rect.centerx - WIN_WIDTH // 2
                camera_y = player.rect.centery - WIN_HEIGHT // 2

                camera_x = max(-400, min(camera_x, 400))
                camera_y = max(-120, min(camera_y, 120))

                for ent in self.entity_list:
                    draw_rect = ent.rect.copy()
                    draw_rect.x -= camera_x
                    draw_rect.y -= camera_y

                    if hasattr(ent, "get_surf"):
                        self.window.blit(ent.get_surf(), draw_rect)
                    else:
                        self.window.blit(ent.surf, draw_rect)

                    ent.move()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                pygame.display.flip()


