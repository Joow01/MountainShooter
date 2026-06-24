import pygame
import sys
from Code.Const import (
    WIN_WIDTH,
    WIN_HEIGHT,
    COLOR_BLOOD,
    MENU_OPTION,
    COLOR_GOLD,
    COLOR_BRIGHT_BLOOD
)


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./Assets/MenuBG.png').convert()
        self.surf = pygame.transform.scale(self.surf, (WIN_WIDTH, WIN_HEIGHT))
        self.rect = self.surf.get_rect(left=0, top=0)
        self.title_font = pygame.font.Font('./Assets/Fonte/static/Cinzel-Bold.ttf', 50)

    def run(self):
        menu_option = 0
        pygame.mixer_music.load('./Assets/Menu.mp3')
        pygame.mixer_music.play(-1)

        while True:
            self.window.blit(self.surf, self.rect)

            self.menu_text(100, "ETERNAL", COLOR_BLOOD, (WIN_WIDTH / 2, 70), glow=True)
            self.menu_text(100, "BLOOD", COLOR_BLOOD, (WIN_WIDTH / 2, 145), glow=True)

            for i in range(len(MENU_OPTION)):
                color = COLOR_BRIGHT_BLOOD if i == menu_option else COLOR_GOLD
                self.menu_text(
                    70,
                    MENU_OPTION[i],
                    color,
                    (WIN_WIDTH / 2, 330 + 65 * i)
                )

            # Comandos
            self.menu_text(24, "CONTROLS", COLOR_GOLD, (WIN_WIDTH / 2, WIN_HEIGHT - 170))
            self.menu_text(22, "Arrow Keys - Move", (180, 180, 180), (WIN_WIDTH / 2, WIN_HEIGHT - 135))
            self.menu_text(22, "Z - Attack", (180, 180, 180), (WIN_WIDTH / 2, WIN_HEIGHT - 105))
            self.menu_text(22, "Left Shift - Shield", (180, 180, 180), (WIN_WIDTH / 2, WIN_HEIGHT - 75))
            self.menu_text(22, "ENTER - Confirm", (180, 180, 180), (WIN_WIDTH / 2, WIN_HEIGHT - 45))

            if MENU_OPTION[menu_option] == "Score":
                self.menu_text(
                    28,
                    "Survival Mode and Score coming soon",
                    COLOR_BRIGHT_BLOOD,
                    (WIN_WIDTH / 2, 610)
                )
                self.menu_text(
                    24,
                    "Modo Sobrevivência e Pontuação em breve",
                    (180, 180, 180),
                    (WIN_WIDTH / 2, 645)
                )

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        menu_option = (menu_option + 1) % len(MENU_OPTION)

                    if event.key == pygame.K_UP:
                        menu_option = (menu_option - 1) % len(MENU_OPTION)

                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple, glow=False):
        text_font = pygame.font.Font("./Assets/Fonte/static/Cinzel-Bold.ttf", text_size)

        if glow:
            glow_surf = text_font.render(text, True, (255, 70, 70))
            glow_surf.set_alpha(100)

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]:
                glow_rect = glow_surf.get_rect(
                    center=(text_center_pos[0] + dx, text_center_pos[1] + dy)
                )
                self.window.blit(glow_surf, glow_rect)

        shadow_surf = text_font.render(text, True, (0, 0, 0))
        shadow_rect = shadow_surf.get_rect(
            center=(text_center_pos[0] + 3, text_center_pos[1] + 3)
        )

        text_surf = text_font.render(text, True, text_color)
        text_rect = text_surf.get_rect(center=text_center_pos)

        self.window.blit(shadow_surf, shadow_rect)
        self.window.blit(text_surf, text_rect)