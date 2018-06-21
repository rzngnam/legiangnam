import pygame
import random
from pygame.locals import *

width = 800
height = 600

#  tạo khung hiển thị game
display_surf = pygame.display.set_mode((width, height))
pygame.display.set_caption(" Snake ")

red = (250, 0, 0)
green = (0, 255, 0)
direction = [20, -20]

fps = 20  # frame per second
fps_clock = pygame.time.Clock()


class Apple:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(display_surf, red, (self.x, self.y, random.randrange(20, 600, 20),
                                             random.randrange(20, 600, 20)))

    def update(self, snake):
        if (self.x == snake.x) and (self.y == snake.y):
            self.x = random.randrange(20, 600, 20)
            self.y = random.randrange(20, 600, 20)


class Snake:
    body_x = [20, 40, 60]   # body_x[0] và body_y[0] là head của rắn
    body_y = [20, 20, 20]

    def __init__(self, w, h, tail, speed):
        self.w = w
        self.h = h
        self.tail = tail
        self.speed = speed

    def update(self):
        for i in range(self.tail - 1, 0, -1):
            self.body_x[i] = self.body_x[i - 1]
            self.body_y[i] = self.body_y[i - 1]

        if direction == 1:
            self.move_right()
        elif direction == 2:
            self.move_left()
        elif direction == 3:
            self.move_up()
        elif direction == 4:
            self.move_down()

    def move_right(self):
        self.body_x[0] += direction[0]*self.speed

    def move_left(self):
        self.body_x[0] += direction[1]*self.speed

    def move_up(self):
        self.body_y[0] += direction[1]*self.speed

    def move_down(self):
        self.body_y[0] += direction[0]*self.speed

    def eat(self, apple):
        if (self.body_x[0] == apple.x) and (self.body_y[0] == apple.y):
            self.tail += 1
            self.body_x.append(self.body_x[-1])  # Táo bị ăn => body dài ra
            self.body_y.append(self.body_y[-1])

    def death(self):
        for i in range(self.tail):
            if (self.body_x[0] == self.body_x[i]) and (self.body_y[0] == self.body_y[i]):
                self.tail = 1
                self.body_x = [20, 40, 60]   # reset the game
                self.body_y = [20, 20, 20]

    def hit_celling(self):
        if self.body_y[0] == 0:
            return True
        else:
            return False

    def hit_floor(self):
        if self.body_y[0] == height - self.h:
            return True
        else:
            return False

    def hit_edge(self):
        if (self.body_x[0] == 0) or (self.body_x == width - self.w):
            return True
        else:
            return False

    def draw(self):
        for i in range(self.tail):
            pygame.draw.rect(display_surf, green, (self.body_x[i], self.body_y[i], 20, 20))
