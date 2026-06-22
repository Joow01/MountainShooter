import pygame
from Code.Const import WIN_WIDTH, COLOR_BLOOD, MENU_OPTION, COLOR_GOLD,  COLOR_BRIGHT_BLOOD


class Menu :
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/MenuBG.png')
        self.rect = self.surf.get_rect(left=0, top=0)
        self.title_font = pygame.font.Font(
            './assets/Fonte/static/Cinzel-Bold.ttf',50 )

    def run(self, ):
        menu_option = 0
        pygame.mixer_music.load('./assets/Menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            #DRAW IMAGES
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(text_size=100, text="ETERNAL", text_color=COLOR_BLOOD, text_center_pos=(WIN_WIDTH / 2, 70), glow=True)
            self.menu_text(text_size=100, text="BLOOD", text_color=COLOR_BLOOD, text_center_pos=(WIN_WIDTH / 2, 145), glow=True)

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(text_size=70, text=MENU_OPTION[i], text_color=COLOR_BRIGHT_BLOOD,text_center_pos=(WIN_WIDTH / 2, 350 + 70 * i))
                else:
                    self.menu_text(text_size=70, text=MENU_OPTION[i], text_color=COLOR_GOLD, text_center_pos=(WIN_WIDTH / 2, 350 + 70 *i))
            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() # Close Window
                    quit() # End Pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  #DOWN KEY
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP: #UP KEY
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN: #ENTER
                        return MENU_OPTION[menu_option]


    def menu_text(self, text_size: int, text: str,
                  text_color: tuple, text_center_pos: tuple, glow=False):

        text_font = pygame.font.Font(
            "./assets/Fonte/static/Cinzel-Bold.ttf",
            text_size
        )

        #Glow
        if glow:
            glow_surf = text_font.render(text, True, (255, 70, 70))
            glow_surf.set_alpha(100)

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1),(-1, 1), (1, -1)] :
                glow_rect = glow_surf.get_rect(
                    center=(text_center_pos[0] + dx,
                            text_center_pos[1] + dy)
                )
                self.window.blit(glow_surf, glow_rect)
        # Shadow
        shadow_surf = text_font.render(text, True, (0, 0, 0))
        shadow_rect = shadow_surf.get_rect(
            center=(text_center_pos[0] + 3, text_center_pos[1] + 3)
        )

        #Texto principal
        text_surf = text_font.render(text, True, text_color)
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(shadow_surf, shadow_rect)
        self.window.blit(text_surf, text_rect)