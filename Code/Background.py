import pygame
from Code.Entity import Entity
from Code.Const import WIN_WIDTH


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

        if name == 'Level1BG4':
            self.surf = pygame.transform.smoothscale(self.surf, (WIN_WIDTH, 520))
            self.rect = self.surf.get_rect(left=0, top=400)

        else:
            original_w = self.surf.get_width()
            original_h = self.surf.get_height()

            scale = WIN_WIDTH / original_w

            new_w = int(original_w * scale)
            new_h = int(original_h * scale)

            self.surf = pygame.transform.smoothscale(self.surf, (new_w, new_h))
            self.rect = self.surf.get_rect(left=0, top=0)

    def move(self):
        pass