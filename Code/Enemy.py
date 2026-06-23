import pygame

from Code.Entity import Entity


class Enemy(Entity):
    def load_frame(self, path, scale):
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

        self.walk_frames = [
            self.load_frame('./assets/Enemywalk1.png', 4),
            self.load_frame('./assets/Enemywalk2.png', 4),
            self.load_frame('./assets/Enemywalk3.png', 4),
            self.load_frame('./assets/Enemywalk4.png', 4),
        ]

        self.frames = self.walk_frames
        self.frame_index = 0
        self.animation_speed = 0.12
        self.surf = self.frames[0]
        self.rect = self.surf.get_rect(left=position[0], top=position[1])

    def get_surf(self):
        if self.facing_right:
            return self.surf

        return pygame.transform.flip(self.surf, True, False)

    def animate(self):
        self.frame_index += self.animation_speed

        if self.frame_index >= len(self.frames):
            self.frame_index = 0

        old_center = self.rect.center
        self.surf = self.frames[int(self.frame_index)]
        self.rect = self.surf.get_rect(center=old_center)

    def move_towards_player(self, player):
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