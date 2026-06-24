import pygame

from Code.Entity import Entity


class Enemy(Entity):
    @staticmethod
    def load_frame(path, scale):
        image = pygame.image.load(path).convert_alpha()
        return pygame.transform.scale(
            image,
            (image.get_width() * scale, image.get_height() * scale)
        )

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

        self.facing_right = True
        self.speed = 2
        self.life = 3
        self.damage = 8

        self.aggro = False
        self.aggro_distance = 600

        self.damage_done = False
        self.damage_frame = 3

        self.attack_distance = 200
        self.attack_cooldown = 1000
        self.last_attack_time = 0
        self.attacking = False

        self.animation_speed = 0.12
        self.attack_animation_speed = 0.10
        self.death_animation_speed = 0.01

        self.frame_index = 0
        self.dying = False
        self.dead = False
        self.death_time = 0
        self.death_duration = 2000

        self.idle_frames = [
            self.load_frame('./Assets/EnemyIdle1.png', 4),
            self.load_frame('./Assets/EnemyIdle2.png', 4),
            self.load_frame('./Assets/EnemyIdle3.png', 4),
            self.load_frame('./Assets/EnemyIdle4.png', 4),
            self.load_frame('./Assets/EnemyIdle5.png', 4),
            self.load_frame('./Assets/EnemyIdle6.png', 4),
            self.load_frame('./Assets/EnemyIdle7.png', 4),
            self.load_frame('./Assets/EnemyIdle8.png', 4),
        ]

        self.walk_frames = [
            self.load_frame('./Assets/Enemywalk1.png', 4),
            self.load_frame('./Assets/Enemywalk2.png', 4),
            self.load_frame('./Assets/Enemywalk3.png', 4),
            self.load_frame('./Assets/Enemywalk4.png', 4),
        ]

        self.attack_frames = [
            self.load_frame('./Assets/EnemyAttack_2,0.png', 4),
            self.load_frame('./Assets/EnemyAttack_2,1.png', 4),
            self.load_frame('./Assets/EnemyAttack_2,2.png', 4),
            self.load_frame('./Assets/EnemyAttack_2,3.png', 4),
        ]

        self.death_frames = [
            self.load_frame('./Assets/EDead1.png', 4),
            self.load_frame('./Assets/EDead2.png', 4),
        ]

        self.frames = self.idle_frames
        self.surf = self.frames[0]
        self.rect = self.surf.get_rect(left=position[0], top=position[1])

    def get_surf(self):
        if self.facing_right:
            return self.surf
        return pygame.transform.flip(self.surf, True, False)

    def animate(self):
        if self.dying:
            self.frame_index += self.death_animation_speed
        elif self.attacking:
            self.frame_index += self.attack_animation_speed
        else:
            self.frame_index += self.animation_speed

        if self.frame_index >= len(self.frames):
            if self.dying:
                self.frame_index = len(self.frames) - 1

                if pygame.time.get_ticks() - self.death_time > self.death_duration:
                    self.dead = True

                return

            self.frame_index = 0

            if self.attacking:
                self.attacking = False
                self.frames = self.idle_frames

        old_center = self.rect.center
        self.surf = self.frames[int(self.frame_index)]
        self.rect = self.surf.get_rect(center=old_center)

    def die(self):
        if not self.dying:
            self.dying = True
            self.attacking = False
            self.frames = self.death_frames
            self.frame_index = 0
            self.death_time = pygame.time.get_ticks()

    def move_towards_player(self, player):
        if self.dying:
            self.animate()
            return

        distance_x = abs(player.rect.centerx - self.rect.centerx)
        distance_y = abs(player.rect.centery - self.rect.centery)
        current_time = pygame.time.get_ticks()

        if not self.aggro:
            if distance_x < self.aggro_distance and distance_y < self.aggro_distance:
                self.aggro = True
            else:
                self.frames = self.idle_frames
                self.animate()
                return

        if distance_x < self.attack_distance and distance_y < self.attack_distance:
            if not self.attacking and current_time - self.last_attack_time > self.attack_cooldown:
                self.attacking = True
                self.frames = self.attack_frames
                self.frame_index = 0
                self.damage_done = False
                self.last_attack_time = current_time

            if self.attacking and int(self.frame_index) == self.damage_frame and not self.damage_done:
                if player.defending and player.stamina > 0:
                    player.stamina -= 10
                else:
                    player.life -= self.damage

                self.damage_done = True

            self.animate()
            return

        self.frames = self.walk_frames

        if player.rect.centerx > self.rect.centerx:
            self.rect.x += self.speed
            self.facing_right = True
        elif player.rect.centerx < self.rect.centerx:
            self.rect.x -= self.speed
            self.facing_right = False

        if player.rect.centery > self.rect.centery:
            self.rect.y += self.speed
        elif player.rect.centery < self.rect.centery:
            self.rect.y -= self.speed

        self.animate()

    def move(self):
        pass