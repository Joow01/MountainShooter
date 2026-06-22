import pygame
from Code.Const import WIN_WIDTH, WINDOW_HEIGHT, COLOR_GOLD, COLOR_BLOOD


class Cutscene:
    def __init__(self, window):
        self.window = window
        self.bg = pygame.image.load('./assets/Level0BGComp.png')
        self.bg = pygame.transform.scale(self.bg, (WIN_WIDTH, WINDOW_HEIGHT))
        self.font = pygame.font.Font('./assets/Fonte/static/Cinzel-Bold.ttf', 34)

        self.lines = [
            (
                "For centuries, the Eternal Blood Castle stood untouched.",
                "(Por séculos, o Castelo do Sangue Eterno permaneceu intocado.)"
            ),
            (
                "Tonight, sacred hunters and monsters have breached its walls.",
                "(Esta noite, caçadores sagrados e Monstros atravessaram suas muralhas.)"
            ),
            (
                "The Vampire Lord is weakened.",
                "(O Lorde Vampiro está enfraquecido.)"
            ),
            (
                "You are the last knight of his guard.",
                "(Você é o último cavaleiro de sua guarda.)"
            ),
            (
                "Defend the throne.",
                "(Defenda o trono.)"
            )
        ]

    def run(self):
        clock = pygame.time.Clock()

        line_index = 0

        while True:

            # Fundo preto
            self.window.fill((0, 0, 0))

            # Texto principal
            # Texto em inglês
            english = self.font.render(
                self.lines[line_index][0],
                True,
                COLOR_GOLD
            )

            english_rect = english.get_rect(
                center=(WIN_WIDTH // 2, WINDOW_HEIGHT // 2 - 30)
            )

            self.window.blit(english, english_rect)

            # Tradução em português
            portuguese = self.font.render(
                self.lines[line_index][1],
                True,
                (180, 180, 180)
            )

            portuguese_rect = portuguese.get_rect(
                center=(WIN_WIDTH // 2, WINDOW_HEIGHT // 2 + 30)
            )

            self.window.blit(portuguese, portuguese_rect)

            # Texto auxiliar
            hint = self.font.render(
                "ENTER",
                True,
                COLOR_BLOOD
            )

            hint_rect = hint.get_rect(
                center=(WIN_WIDTH // 2, WINDOW_HEIGHT - 100)
            )

            self.window.blit(hint, hint_rect)

            pygame.display.flip()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RETURN:
                        line_index += 1

                        if line_index >= len(self.lines):
                            return

                    if event.key == pygame.K_ESCAPE:
                        return

            clock.tick(60)