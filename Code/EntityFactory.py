from Code.Background import Background
from Code.Const import WIN_HEIGHT
from Code.Player import Player
from Code.Enemy import Enemy


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:

            case 'Level1BG':
                list_bg = []
                list_bg.append(Background('Level1BG3', position=(0, 0)))
                list_bg.append(Background('Level1BG4', position=(0, 520)))
                list_bg.append(Background('Level1BG1', position=(0, 0)))
                list_bg.append(Background('Level1BG0', position=(0, 0)))
                return list_bg

            case 'TerraceBG':
                return [
                    Background('Terrace', position=(0, 0))
                ]

            case 'Player':
                return Player('PlayerIdle1,1', (10, WIN_HEIGHT // 2))

            case 'Enemy':
                return Enemy('Enemywalk1', (1700, 700))

        return []