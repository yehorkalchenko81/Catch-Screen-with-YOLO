from minigame import render_one_frame
from aim import enable_ai_aim
import pygame


def main():
    running = True
    while running:
        running = render_one_frame()
        enable_ai_aim()

    pygame.quit()

if __name__ == '__main__':
    main()