#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from Code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, MAP_WIDTH
from Code.Entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

        self.facing_right = True
        self.frame_index = 0
        self.animation_speed = 0.15
        self.moving = False
        self.idle_frames = [
            pygame.transform.scale(
            pygame.image.load('./assets/PlayerIdle1,1.png').convert_alpha(),
            (250, 250)),
            pygame.transform.scale(
            pygame.image.load('./assets/PlayerIdle1,2.png').convert_alpha(),
            (250, 250)),
            pygame.transform.scale(
            pygame.image.load('./assets/PlayerIdle1,3.png').convert_alpha(),
            (250,250)),
        ]
        self.walk_frames = [
            pygame.transform.scale(
            pygame.image.load('./assets/PlayerWalk1,1.png').convert_alpha(),
            (250, 250)),
            pygame.transform.scale(
            pygame.image.load('./assets/PlayerWalk1,2.png').convert_alpha(),
            (250, 250)),
            pygame.transform.scale(
            pygame.image.load('./assets/PlayerWalk1,3.png').convert_alpha(),
            (250, 250)),
            pygame.transform.scale(
            pygame.image.load('./assets/PlayerWalk1,4.png').convert_alpha(),
            (250, 250)),
        ]
        self.frames = self.idle_frames
        self.surf = self.frames[0]

    def get_surf(self):
        if self.facing_right:
            return self.surf

        return pygame.transform.flip(self.surf, True, False)

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.surf = self.frames[int(self.frame_index)]

    def move(self):
        pressed_key = pygame.key.get_pressed()
        self.moving = False
        if pressed_key[pygame.K_UP] and self.rect.top > 380:
            self.rect.y -= ENTITY_SPEED['Player']
            self.moving = True
        if pressed_key[pygame.K_DOWN] and self.rect.bottom < WIN_HEIGHT:
            self.rect.y += ENTITY_SPEED['Player']
            self.moving = True
        if pressed_key[pygame.K_LEFT] and self.rect.left > -300:
            self.rect.x -= ENTITY_SPEED['Player']
            self.facing_right = False
            self.moving = True
        if pressed_key[pygame.K_RIGHT] and self.rect.right < MAP_WIDTH:
            self.rect.x += ENTITY_SPEED['Player']
            self.facing_right = True
            self.moving = True
        if self.moving:
            self.frames = self.walk_frames
        else:
            self.frames = self.idle_frames
        self.animate()