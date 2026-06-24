import pygame

from Code.Entity import Entity
from Code.Const import WIN_WIDTH, WIN_HEIGHT


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

        if name == 'Terrace':
            self.surf = pygame.image.load('./Assets/Terrace.png').convert_alpha()
            self.surf = pygame.transform.smoothscale(
                self.surf,
                (WIN_WIDTH, WIN_HEIGHT)
            )
            self.rect = self.surf.get_rect(left=0, top=0)

        elif name == 'Level1BG4':
            zoom = 1.7
            self.surf = pygame.transform.smoothscale(
                self.surf,
                (int(WIN_WIDTH * zoom), int(520 * zoom))
            )
            self.rect = self.surf.get_rect(
                left=-(self.surf.get_width() - WIN_WIDTH) // 2,
                top=520
            )

        else:
            original_w = self.surf.get_width()
            original_h = self.surf.get_height()

            zoom = 1.7
            scale = (WIN_WIDTH / original_w) * zoom

            new_w = int(original_w * scale)
            new_h = int(original_h * scale)

            self.surf = pygame.transform.smoothscale(
                self.surf,
                (new_w, new_h)
            )

            self.rect = self.surf.get_rect(
                left=-(new_w - WIN_WIDTH) // 2,
                top=-(new_h - WIN_HEIGHT) // 2
            )

            if name == 'Level1BG3':
                self.rect.y -= 300

    def move(self):
        pass