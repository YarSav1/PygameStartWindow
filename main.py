import pygame

import config_code
from FieldGame.main_init import main_call_point_game
from config_code import WINDOW_WIDTH, WINDOW_HEIGHT
from correction.correct_color_field import correction
from FieldSettings.main_init import main_call_point

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))  # инициализация окна
WINDOW.set_alpha(None)


def test(mouse):
    x, y, w, h = mouse[0], mouse[1], 10, 10
    pygame.draw.rect(WINDOW, (200, 200, 200), (x, y, w, h))
    if 0 < x < config_code.WINDOW_SETTINGS_GAME:
        correction(WINDOW, x, y, w, h, config_code.COLOR_SETTINGS)


CLOCK = pygame.time.Clock()
running = True
while running:
    CLOCK.tick(config_code.FPS)
    pygame.display.update()  # обновляем экран
    main_call_point_game(WINDOW)

    main_call_point(WINDOW, CLOCK)
    # mouse = pygame.mouse.get_pos()
    # test(mouse)
    for event in pygame.event.get():
        # if event.type == pygame.MOUSEMOTION:
        #     test(mouse)
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
