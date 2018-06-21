import pygame
from pygame.locals import *

width = 800
height = 600

#  tạo khung hiển thị game
display_surf = pygame.display.set_mode((width, height))
pygame.display.set_caption(" Snake ")

red = (250, 0, 0)
pygame.draw.rect(display_surf, red, (10, 10, 10, 10))


fps = 200  # frame per second
fps_clock = pygame.time.Clock()


def main():
    pygame.init()

    while True:
        pygame.display.update()

        fps_clock.tick(fps)


if __name__ == '__main__':
    main()

