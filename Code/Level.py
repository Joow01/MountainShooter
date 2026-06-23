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
        self.enemies = []
        self.enemies.append(EntityFactory.get_entity('Enemy'))

    def draw_hud(self, player):
        pygame.draw.rect(self.window, (20, 20, 20), (30, 30, 300, 25))
        pygame.draw.rect(self.window, (0, 120, 0), (30, 30, 295 * (player.life / player.max_life), 23))
        pygame.draw.rect(self.window, (34, 177, 76), (30, 30, 295 * (player.life / player.max_life), 20))
        pygame.draw.rect(self.window, (80, 255, 120), (30, 30, 295 * (player.life / player.max_life), 5))
        pygame.draw.rect(self.window, (0, 0, 0), (30, 30, 300, 25), 2)
        pygame.draw.rect(self.window, (20, 20, 20), (30, 65, 300, 20))
        pygame.draw.rect(self.window, (140, 100, 20), (32, 67, 295 * (player.stamina / player.max_stamina), 18))
        pygame.draw.rect(self.window,(212, 175, 55),(30, 65, 295 * (player.stamina / player.max_stamina), 16))
        pygame.draw.rect(self.window,(255, 220, 100),(30, 65, 295 * (player.stamina / player.max_stamina), 4))
        pygame.draw.rect(self.window, (0, 0, 0), (30, 65, 300, 20), 2)

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
                camera_y = max(-400, min(camera_y, 400))
                for ent in self.entity_list:
                    draw_rect = ent.rect.copy()
                    draw_rect.x -= camera_x
                    draw_rect.y -= camera_y
                    if hasattr(ent, "get_surf"):
                        self.window.blit(ent.get_surf(), draw_rect)
                    else:
                        self.window.blit(ent.surf, draw_rect)
                    ent.move()
                for enemy in self.enemies:
                    enemy.move_towards_player(player)
                    draw_rect = enemy.rect.copy()
                    draw_rect.x -= camera_x
                    draw_rect.y -= camera_y
                    self.window.blit(enemy.get_surf(), draw_rect)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                self.draw_hud(player)
                pygame.display.flip()


