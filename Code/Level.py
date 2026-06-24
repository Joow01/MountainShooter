import sys
import pygame
from Code.Const import WIN_WIDTH, WIN_HEIGHT
from Code.Entity import Entity
from Code.EntityFactory import EntityFactory

class Level:
    def __init__(self, window, name, game_mode, player=None):
        self.window = window
        self.name = name
        self.game_mode = game_mode

        self.entity_list: list[Entity] = []

        if self.name == 'Terrace':
            self.entity_list.extend(EntityFactory.get_entity('TerraceBG'))
        else:
            self.entity_list.extend(EntityFactory.get_entity('Level1BG'))

        if player:
            self.player = player
        else:
            self.player = EntityFactory.get_entity('Player')

        self.entity_list.append(self.player)

        self.enemies = []

        self.terrace_stop_time = None
        self.terrace_wait_time = 3000

        if self.name == 'Terrace':
            self.player.rect.x = WIN_WIDTH + 200
            self.player.rect.y = WIN_HEIGHT // 2
        else:
            self.current_wave = 1
            self.max_waves = 3

            self.wave_config = {
                1: 1,
                2: 2,
                3: 3
            }

            self.spawn_wave()

    def spawn_wave(self):
        self.enemies.clear()

        enemy_count = self.wave_config[self.current_wave]

        positions = [
            (1400, 700),
            (1700, 520),
            (1900, 850)
        ]

        for i in range(enemy_count):
            enemy = EntityFactory.get_entity('Enemy')
            enemy.rect.topleft = positions[i]
            self.enemies.append(enemy)

    def draw_hud(self, player):
        pygame.draw.rect(self.window, (20, 20, 20), (30, 30, 300, 25))
        pygame.draw.rect(
            self.window,
            (0, 120, 0),
            (30, 30, 295 * (player.life / player.max_life), 23))
        pygame.draw.rect(
            self.window,
            (34, 177, 76),
            (30, 30, 295 * (player.life / player.max_life), 20))
        pygame.draw.rect(
            self.window,
            (80, 255, 120),
            (30, 30, 295 * (player.life / player.max_life), 5))
        pygame.draw.rect(self.window, (0, 0, 0), (30, 30, 300, 25), 2)
        pygame.draw.rect(self.window, (20, 20, 20), (30, 65, 300, 20))
        pygame.draw.rect(
            self.window,
            (140, 100, 20),
            (32, 67, 295 * (player.stamina / player.max_stamina), 18))
        pygame.draw.rect(
            self.window,
            (212, 175, 55),
            (30, 65, 295 * (player.stamina / player.max_stamina), 16))
        pygame.draw.rect(
            self.window,
            (255, 220, 100),
            (30, 65, 295 * (player.stamina / player.max_stamina), 4))
        pygame.draw.rect(self.window, (0, 0, 0), (30, 65, 300, 20), 2)

        if self.name != 'Terrace':
            font = pygame.font.Font(
                './Assets/Fonte/static/Cinzel-Bold.ttf',
                28)
            wave_text = font.render(
                f'Wave {self.current_wave}/{self.max_waves}',
                True,
                (212, 175, 55))
            self.window.blit(wave_text, (30, 95))
            enemy_text = font.render(
                f'Enemies: {len(self.enemies)}',
                True,
                (180, 180, 180))
            self.window.blit(enemy_text, (30, 130))
    def run(self):
        pygame.mixer_music.load('./Assets/Level1Music.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            self.window.fill((0, 0, 0))
            player = self.player

            if self.name == 'Terrace':
                camera_x = 0
                camera_y = 0
                target_x = WIN_WIDTH // 2
                if player.rect.centerx > target_x:
                    player.facing_right = False
                    player.rect.x -= 3
                    player.moving = True
                    player.frames = player.walk_frames
                    player.animate()
                else:
                    player.moving = False
                    player.frames = player.idle_frames
                    player.animate()
                    if self.terrace_stop_time is None:
                        self.terrace_stop_time = pygame.time.get_ticks()
                    if pygame.time.get_ticks() - self.terrace_stop_time >= self.terrace_wait_time:
                        return "demo_end"
            else:
                camera_x = player.rect.centerx - WIN_WIDTH // 2
                camera_y = player.rect.centery - WIN_HEIGHT // 2
                camera_x = max(-400, min(camera_x, 400))
                camera_y = max(-400, min(camera_y, 400))
                for ent in self.entity_list:
                    ent.move()
                for enemy in self.enemies[:]:
                    enemy.move_towards_player(player)
                    if (
                        player.attacking
                        and not player.hit_done
                        and int(player.frame_index) == player.damage_frame
                        and player.rect.colliderect(enemy.rect)
                        and not enemy.dying):
                        enemy.life -= player.damage
                        player.hit_done = True
                        if enemy.life <= 0:
                            enemy.die()
                    if enemy.dead:
                        self.enemies.remove(enemy)
                if len(self.enemies) == 0:
                    self.current_wave += 1
                    if self.current_wave > self.max_waves:
                        return "level_2"
                    self.spawn_wave()
                if player.life <= 0 and not player.dying:
                    player.die()
                if player.dead:
                    return "game_over"
            for ent in self.entity_list:
                if ent == player:
                    continue
                draw_rect = ent.rect.copy()
                draw_rect.x -= camera_x
                draw_rect.y -= camera_y
                if hasattr(ent, "get_surf"):
                    self.window.blit(ent.get_surf(), draw_rect)
                else:
                    self.window.blit(ent.surf, draw_rect)
            draw_list = [player] + self.enemies
            draw_list.sort(key=lambda obj: obj.rect.bottom)
            for obj in draw_list:
                draw_rect = obj.rect.copy()
                draw_rect.x -= camera_x
                draw_rect.y -= camera_y
                if hasattr(obj, "get_surf"):
                    self.window.blit(obj.get_surf(), draw_rect)
                else:
                    self.window.blit(obj.surf, draw_rect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.draw_hud(player)
            pygame.display.flip()