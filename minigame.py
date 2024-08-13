import pygame
import random

pygame.init()

width, height = 1500, 1000
screen = pygame.display.set_mode((width, height))

texture = pygame.image.load('texture.png')

object_width, object_height = texture.get_size()

def random_position():
    x = random.randint(0, width - object_width)
    y = random.randint(0, height - object_height)
    return x, y

objects = [random_position() for _ in range(3)]


def render_one_frame():
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                return False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            for i, (obj_x, obj_y) in enumerate(objects):
                if obj_x < mouse_x < obj_x + object_width and obj_y < mouse_y < obj_y + object_height:
                    objects[i] = random_position()
                    break

    for obj_x, obj_y in objects:
        screen.blit(texture, (obj_x, obj_y))

    pygame.display.flip()

    return True


