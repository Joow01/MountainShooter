import pygame

from Code.Const import WIN_WIDTH, WINDOW_HEIGHT, MENU_OPTION
from Code.Level import Level
from Code.Menu import Menu
from Code.Cutscene import Cutscene

class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WINDOW_HEIGHT))

    def run(self, ):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:  # New Game
                cutscene = Cutscene(self.window)
                cutscene.run()

                level = Level(self.window, 'Level 1', menu_return)
                level.run()

            elif menu_return == MENU_OPTION[1]:  # Continue
                level = Level(self.window, 'Level 1', menu_return)
                level.run()
            elif  menu_return == MENU_OPTION[3]:
                pygame.quit()  # Close Window
                quit()  # End Pygame

            else:
                pass

