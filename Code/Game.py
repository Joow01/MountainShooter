import sys
import pygame

from Code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from Code.Level import Level
from Code.Menu import Menu
from Code.Cutscene import Cutscene


class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:
                cutscene = Cutscene(self.window)
                cutscene.run()

                level = Level(self.window, 'Level 1', menu_return)
                level_return = level.run()

                if level_return == "game_over":
                    self.game_over_screen()

                elif level_return == "level_2":
                    level2 = Level(
                        self.window,
                        'Terrace',
                        menu_return,
                        player=level.player
                    )
                    level2_return = level2.run()

                    if level2_return == "demo_end":
                        self.demo_end_screen()


            elif menu_return == MENU_OPTION[1]:  # Continue
                level = Level(self.window, 'Level 1', menu_return)
                level_return = level.run()
                if level_return == "game_over":
                    self.game_over_screen()
                elif level_return == "level_2":
                    level2 = Level(self.window, 'Terrace', menu_return, player=level.player)
                    level2_return = level2.run()
                    if level2_return == "demo_end":
                        self.demo_end_screen()
            elif menu_return == MENU_OPTION[3]:  # Exit
                pygame.quit()
                sys.exit()

    def game_over_screen(self):
        font_title = pygame.font.Font('./Assets/Fonte/static/Cinzel-Bold.ttf', 90)
        font_text = pygame.font.Font('./Assets/Fonte/static/Cinzel-Bold.ttf', 36)

        clock = pygame.time.Clock()

        while True:
            self.window.fill((0, 0, 0))

            title = font_title.render("GAME OVER", True, (170, 20, 40))
            title_rect = title.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2 - 80))
            self.window.blit(title, title_rect)

            text = font_text.render("Press ENTER to return to menu", True, (212, 175, 55))
            text_rect = text.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2 + 40))
            self.window.blit(text, text_rect)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    return

            clock.tick(60)

    def demo_end_screen(self):
        font_title = pygame.font.Font('./Assets/Fonte/static/Cinzel-Bold.ttf', 60)
        font_text = pygame.font.Font('./Assets/Fonte/static/Cinzel-Bold.ttf', 32)
        coming_soon = font_text.render(
            "Score System Coming Soon"
                "(Sistema de pontos Em Breve)",
            True,
            (180, 180, 180)
        )

        coming_rect = coming_soon.get_rect(
            center=(WIN_WIDTH // 2, WIN_HEIGHT // 2 + 50)
        )

        self.window.blit(coming_soon, coming_rect)
        clock = pygame.time.Clock()

        while True:
            self.window.fill((0, 0, 0))

            title = font_title.render("END OF DEMO", True, (212, 175, 55))
            title_rect = title.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2 - 60))
            self.window.blit(title, title_rect)
            text = font_text.render("The battle for Eternal Blood has just begun...", True, (170, 20, 40))
            text_rect = text.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2 + 10))
            self.window.blit(text, text_rect)
            hint = font_text.render("Press ENTER to return to menu", True, (180, 180, 180))
            hint_rect = hint.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2 + 80))
            self.window.blit(hint, hint_rect)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    return

            clock.tick(60)