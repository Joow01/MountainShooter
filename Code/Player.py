#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from Code.Const import ENTITY_SPEED, WIN_HEIGHT, MAP_WIDTH
from Code.Entity import Entity


class Player(Entity):
    def load_frame(self, path, scale):
        image = pygame.image.load(path).convert_alpha()
        return pygame.transform.scale(
            image,
            (image.get_width() * scale, image.get_height() * scale)
        )
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.defending = False
        self.defense_frames = [
        self.load_frame('./assets/Protect.png', 4)]
        self.max_life = 100
        self.life = self.max_life
        self.max_stamina = 100
        self.stamina = self.max_stamina
        self.attack_cooldown = 800
        self.last_attack = 0
        self.animation_speed = 0.20
        self.attack_animation_speed = 0.15
        self.attack_frames = [
        self.load_frame('./assets/PlayerAttack1,1.png', 4),
        self.load_frame('./assets/PlayerAttack1,2.png', 4),
        self.load_frame('./assets/PlayerAttack1,3.png', 4),
        self.load_frame('./assets/PlayerAttack1,4.png', 4),]
        self.attacking = False
        self.attack_finished = False
        self.facing_right = True
        self.frame_index = 0
        self.animation_speed = 0.15
        self.moving = False
        self.idle_frames = [
            pygame.transform.scale(
            pygame.image.load('./assets/PlayerIdle1,1.png').convert_alpha(),(180, 280)),
            pygame.transform.scale(
            pygame.image.load('./assets/PlayerIdle1,2.png').convert_alpha(),(180, 280)),
            pygame.transform.scale(
            pygame.image.load('./assets/PlayerIdle1,3.png').convert_alpha(),(180,280)),]
        self.walk_frames = [
            pygame.transform.scale(
            pygame.image.load('./assets/PlayerWalk1,1.png').convert_alpha(),(180, 280)),
            pygame.transform.scale(
            pygame.image.load('./assets/PlayerWalk1,2.png').convert_alpha(),(180, 280)),
            pygame.transform.scale(
            pygame.image.load('./assets/PlayerWalk1,3.png').convert_alpha(),(180, 280)),
            pygame.transform.scale(
            pygame.image.load('./assets/PlayerWalk1,4.png').convert_alpha(),(180, 280)),]
        self.frames = self.idle_frames
        self.surf = self.frames[0]

    def get_surf(self):
        if self.facing_right:
            return self.surf

        return pygame.transform.flip(self.surf, True, False)

    def animate(self):
        if self.attacking:
            self.frame_index += self.attack_animation_speed
        else:
            self.frame_index += self.animation_speed

        if self.frame_index >= len(self.frames):
            self.frame_index = 0

            if self.attacking:
                self.attacking = False

        old_center = self.rect.center
        self.surf = self.frames[int(self.frame_index)]
        self.rect = self.surf.get_rect(center=old_center)

    def move(self):
        pressed_key = pygame.key.get_pressed()
        self.moving = False

        # Defesa
        if pressed_key[pygame.K_e] and self.stamina > 0 and not self.attacking:
            self.defending = True
            self.stamina -= 0.01
        else:
            self.defending = False

        if not self.defending:

            if pressed_key[pygame.K_w] and self.rect.top > 290:
                self.rect.y -= ENTITY_SPEED['Player']
                self.moving = True

            if pressed_key[pygame.K_s] and self.rect.bottom < WIN_HEIGHT + 350:
                self.rect.y += ENTITY_SPEED['Player']
                self.moving = True

            if pressed_key[pygame.K_a] and self.rect.left > -300:
                self.rect.x -= ENTITY_SPEED['Player']
                self.facing_right = False
                self.moving = True

            if pressed_key[pygame.K_d] and self.rect.right < MAP_WIDTH:
                self.rect.x += ENTITY_SPEED['Player']
                self.facing_right = True
                self.moving = True
        current_time = pygame.time.get_ticks()
        if (
                pressed_key[pygame.K_SPACE]
                and not self.attacking
                and current_time - self.last_attack > self.attack_cooldown
        ):
            self.attacking = True
            self.frame_index = 0
            self.last_attack = current_time

        if pressed_key[pygame.K_e] and self.stamina > 0 and not self.attacking:
            self.defending = True
            self.stamina -= 0.1
        else:
            self.defending = False

        if self.attacking:
            self.frames = self.attack_frames
        elif self.defending:
            self.frames = self.defense_frames
        elif self.moving:
            self.frames = self.walk_frames
        else:
            self.frames = self.idle_frames

        if not self.defending and self.stamina < self.max_stamina:
            self.stamina += 0.5

        self.animate()